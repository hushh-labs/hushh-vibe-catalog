import base64
import copy
import json
import uuid
from collections.abc import Iterable
from io import BytesIO
from typing import Dict, List, Optional

import flatbuffers
import numpy as np
import pandas as pd
from PIL import Image
from PIL.Image import Image as ImageT
from transformers import CLIPModel, CLIPProcessor, ProcessorMixin

import hushh
from hushh.errors import NoEmbeddableContent, UncallableProcessor
from hushh.hcf.Catalog import CatalogT
from hushh.hcf.Category import CategoryT
from hushh.hcf.FlatEmbeddingBatch import FlatEmbeddingBatchT
from hushh.hcf.Product import ProductT
from hushh.hcf.ProductVibes import ProductVibesT
from hushh.hcf.Vibe import VibeT
from hushh.hcf.VibeMode import VibeMode

from .version import VERSION

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")

Processor = ProcessorMixin


class IdBase:
    id: str
    base = ""

    def genId(self):
        return self.base + "-" + str(uuid.uuid1())


class Product(ProductT, IdBase):
    def __init__(self, description: str, url: str, image: ImageT | str):
        self.id = self.genId()
        if pd.isna(description):
            raise NoEmbeddableContent("Missing description of product")

        self.description = description
        self.url = url

        if isinstance(image, str):
            self.image = np.array(Image.open(image))
        else:
            self.image = np.array(image)

    def __repr__(self):
        return f"Product(textVibes:{len(self.textVibes)}, imageVibes:{len(self.imageVibes)})"


class VibeBase(IdBase):
    _products: Dict[str, int] = {}

    def addProductTarget(self, p: Product | str):
        if isinstance(p, str):
            self._products[p] = True
        else:
            self._products[p.id] = True


class Category(CategoryT, VibeBase):
    def __init__(self, description: str, url: str):
        self.base = "CTG"
        self.id = self.genId()
        self.description = description
        self.url = url
        self.productIx = []


class Vibe(VibeT, VibeBase):
    def __init__(self, image: ImageT | str, description: str):
        self.base = "IVB"
        self.id = self.genId()
        self.description = description

        if not isinstance(image, ImageT):
            self.image = Image.open(BytesIO(base64.b64decode(image)))
        else:
            self.image = image

        self.productIdx = []


class FlatEmbeddingBatch(FlatEmbeddingBatchT, IdBase):
    def __init__(
        self,
        shape: Iterable[int],
        type: int,
        flatTensor: Optional[List[float]] = None,
    ):
        self.base = "FEB"
        self.id = self.genId()
        self.shape = shape
        self.type = type
        self.flatTensor = flatTensor if flatTensor is not None else []


class ProductVibes(ProductVibesT, VibeBase):
    def __init__(self):
        self.base = "PVB"
        self.id = self.genId()
        self.products = []

        self.categories = []
        self._categories = {}

        self.vibes = []
        self._vibes = {}

        self.flatBatches = []


class Catalog(CatalogT, IdBase):
    productVibes: ProductVibes
    processor: Processor

    def __init__(self, description: str, processor: Processor = None):
        self.base = "CLG"
        self.id = self.genId()
        self.version = VERSION
        self.description = description

        self.productTextFeatures = []
        self.productImageFeatures = []

        if processor is not None:
            self.processor = processor
        else:
            self.processor = CLIPProcessor.from_pretrained(
                "openai/clip-vit-base-patch32"
            )

        self.productVibes = ProductVibes()

    def __repr__(self):
        return f"Catalog(productVibes.products: {len(self.productVibes.products)})"

    def toJSON(self):
        self.renderProductFlatBatch()
        return json.dumps(self.productVibes.flatBatches, default=lambda o: o.__dict__)

    def readHCF(self, filename: str):
        with open(filename, "rb") as fh:
            cat = hushh.hcf.Catalog.Catalog.GetRootAsCatalog(fh.read())
        return cat

    def toHCF(self, filename: str):
        builder = flatbuffers.Builder(0)
        cat_end = self.Pack(builder)
        builder.Finish(cat_end)
        if not filename.endswith(".hcf"):
            filename = filename + ".hcf"
        with open(filename, "wb") as fh:
            fh.write(builder.Output())

    def renderProductFlatBatch(self):
        images = []
        texts = []

        for p in self.productVibes.products:
            images.append(p.image)
            texts.append(p.description)

        if not texts and not images:
            raise NoEmbeddableContent()

        if callable(self.processor):
            inputs = self.processor(
                text=texts,
                images=images,
                return_tensors="pt",
                padding=True,
            )
        else:
            raise UncallableProcessor()

        image_features = model.get_image_features(
            pixel_values=inputs.pixel_values,
        )

        image_batch = FlatEmbeddingBatch(
            shape=image_features.shape,
            flatTensor=image_features.flatten().tolist(),
            type=VibeMode.ProductImage,
        )
        self.productVibes.flatBatches.append(image_batch)

        text_features = model.get_text_features(
            input_ids=inputs.input_ids,
        )
        text_batch = FlatEmbeddingBatch(
            shape=text_features.shape,
            flatTensor=text_features.flatten().tolist(),
            type=VibeMode.ProductText,
        )
        self.productVibes.flatBatches.append(text_batch)

    def Pack(self, builder):
        self.renderProductFlatBatch()
        return super().Pack(builder)

    def addProduct(self, p: Product):
        if p.id in self.productVibes._products:
            raise ValueError(f"Product {p.id} already exists")
        else:
            self.productVibes._products[p.id] = len(self.productVibes.products)

        self.productVibes.products.append(p)

    def addProductCategory(self, c: Category):
        if c.id in self.productVibes._categories:
            raise ValueError(f"Category {c.id} already exists")
        self.productVibes._categories[c.id] = len(self.productVibes.categories)
        self.productVibes.categories.append(c)

    def addProductVibe(self, v: Vibe):
        if v.id in self.productVibes._vibes:
            raise ValueError(f"Vibe {v.id} already exists")
        self.productVibes._vibes[v.id] = len(self.productVibes.vibes)
        self.productVibes.vibes.append(v)

    def linkProductCategory(self, p_id: str, c_id: str):
        if p_id not in self.productVibes._products:
            raise ValueError(f"Product {p_id} does not exist in Catalog")
        if c_id not in self.productVibes._categories:
            raise ValueError(f"Category {c_id} does not exist in Catalog")

        c_idx = self.productVibes._categories[c_id]
        p_idx = self.productVibes._products[p_id]
        self.productVibes.categories[c_idx].productIdx.append(p_idx)

    def linkProductVibe(self, p_id: str, v_id: str):
        if v_id not in self.productVibes._vibes:
            raise ValueError(f"Vibe {v_id} does not exist in Catalog")

        p_idx = self.productVibes._products[p_id]
        v_idx = self.productVibes._vibes[v_id]
        self.productVibes.vibes[v_idx].productIdx.append(p_idx)
