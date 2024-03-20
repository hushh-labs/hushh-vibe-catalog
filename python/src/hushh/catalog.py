import uuid
from collections.abc import Iterable
from itertools import islice
from typing import Dict, List, Optional

import flatbuffers
import numpy as np
import pandas as pd
import torch
from PIL import Image
from PIL.Image import Image as ImageT
from transformers import (CLIPModel, CLIPProcessor, CLIPTokenizer,
                          PreTrainedModel, PreTrainedTokenizer, ProcessorMixin)

import hushh
from hushh._version import __version__
from hushh.errors import NoEmbeddableContent, UncallableProcessor
from hushh.hcf.Brand import BrandT
from hushh.hcf.Catalog import CatalogT
from hushh.hcf.Category import CategoryT
from hushh.hcf.FlatEmbeddingBatch import FlatEmbeddingBatchT
from hushh.hcf.Product import ProductT
from hushh.hcf.ProductVibes import ProductVibesT
from hushh.hcf.Vibe import VibeT
from hushh.hcf.VibeMode import VibeMode


def batched(iterable, n):
    "Batch data into tuples of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


def read_hcf(filename: str):
    with open(filename, "rb") as fh:
        cat = hushh.hcf.Catalog.Catalog.GetRootAsCatalog(fh.read())
    return cat


class IdBase:
    id: str
    _id_base = "IDB"

    def genId(self):
        return self._id_base + "-" + str(uuid.uuid1())


class Brand(BrandT, IdBase):
    _id_base = "BRD"

    def __init__(self, name: str, description: str, url: str):
        self.id = self.genId()
        self.name = name
        self.description = description
        self.url = url


class Product(ProductT, IdBase):
    def __init__(self, description: str, url: str, image: ImageT | str, brand: Brand):
        self.id = self.genId()
        if pd.isna(description):
            raise NoEmbeddableContent("Missing description of product")

        self.description = description
        self.url = url

        if isinstance(image, str):
            self._image = np.array(Image.open(image).convert("RGB"))
        else:
            self._image = np.array(image.convert("RGB"))

        self.brand = brand

        self.textVibes = []
        self.imageVibes = []

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
    _id_base = "CTG"

    def __init__(self, description: str, url: str):
        self.id = self.genId()
        self.description = description
        self.url = url
        self.productIx = []


class Vibe(VibeT, VibeBase):
    _id_base = "IVB"

    def __init__(self, image: ImageT | str, description: str):
        self.id = self.genId()
        self.description = description

        if isinstance(image, str):
            self._image = np.array(Image.open(image).convert("RGB"))
        else:
            self._image = np.array(image.convert("RGB"))

        self.productIdx = []


class FlatEmbeddingBatch(FlatEmbeddingBatchT, IdBase):
    _id_base = "FEB"

    def __init__(
        self,
        shape: List[int],
        vibeMode: int,
        flatTensor: List[float],
        productIdx: List[int],
    ):
        self.id = self.genId()
        self.shape = shape
        self.vibeMode = vibeMode
        self.flatTensor = flatTensor
        self.productIdx = productIdx


class ProductVibes(ProductVibesT, VibeBase):
    _id_base = "PVB"

    def __init__(self):
        self.id = self.genId()
        self.products = []

        self.categories = []
        self._categories = {}

        self.vibes = []
        self._vibes = {}
        self._brands = {}

        self.productTextBatches = []
        self.productImageBatches = []
        self.textBatches = []
        self.imageBatches = []
        self.brands = []


class Catalog(CatalogT, IdBase):
    productVibes: ProductVibes
    model: PreTrainedModel
    processor: ProcessorMixin
    tokenizer: PreTrainedTokenizer
    _id_base = "CLG"

    def __init__(
        self,
        description: str,
        batchSize=10000,
        model: PreTrainedModel | None = None,
        processor: ProcessorMixin | None = None,
        tokenizer: PreTrainedTokenizer | None = None,
    ):
        self.id = self.genId()
        self.version = __version__
        self.description = description

        self.productTextFeatures = []
        self.productImageFeatures = []

        self.batchSize = batchSize
        self.brands = []

        if model is not None:
            self.model = model
        else:
            self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")

        self.model_name_or_path = self.model.name_or_path

        if processor is not None:
            self.processor = processor
        else:
            self.processor = CLIPProcessor.from_pretrained(
                "openai/clip-vit-base-patch32"
            )

        if tokenizer is not None:
            self.tokenizer = tokenizer
        else:
            self.tokenizer = CLIPTokenizer.from_pretrained(
                "openai/clip-vit-base-patch32"
            )

        self.modelNameOrPath = self.model.name_or_path
        self.tokenizerNameOrPath = self.tokenizer.name_or_path

        self.productVibes = ProductVibes()

    def __repr__(self):
        return f"Catalog(productVibes.products: {len(self.productVibes.products)})"

    def to_hcf(self, filename: str):
        builder = flatbuffers.Builder(0)
        cat_end = self.Pack(builder)
        builder.Finish(cat_end)
        if not filename.endswith(".hcf"):
            filename = filename + ".hcf"
        with open(filename, "wb") as fh:
            fh.write(builder.Output())

    def renderProductFlatBatch(self):
        model = self.model
        with torch.no_grad():
            for i, batch in enumerate(
                batched(self.productVibes.products, self.batchSize)
            ):
                images = []
                texts = []
                for p in batch:
                    images.append(p._image)
                    texts.append(p.description)
                    del p._image

                print(f"Collected images and text for batch {i}")

                if not texts and not images:
                    raise NoEmbeddableContent()
                inputs = None

                if callable(self.processor):
                    inputs = self.processor(
                        text=texts,
                        images=images,
                        return_tensors="pt",
                        padding=True,
                    )
                else:
                    raise UncallableProcessor()

                print(f"Collected inputs for batch {i}")

                image_features = model.get_image_features(
                    pixel_values=inputs.pixel_values,
                )
                text_features = model.get_text_features(
                    input_ids=inputs.input_ids,
                )
                del inputs

                print(f"Collected Image and text features for batch {i}")

                image_batch = FlatEmbeddingBatch(
                    shape=image_features.shape,
                    flatTensor=image_features.flatten().tolist(),
                    vibeMode=VibeMode.ProductImage,
                    productIdx=list(range(i * self.batchSize, i + 1 * self.batchSize)),
                )
                print(f"Image embeddings collected for batch {i}")
                self.productVibes.productImageBatches.append(image_batch)

                text_batch = FlatEmbeddingBatch(
                    shape=text_features.shape,
                    flatTensor=text_features.flatten().tolist(),
                    vibeMode=VibeMode.ProductText,
                    productIdx=list(range(i * self.batchSize, i + 1 * self.batchSize)),
                )

                print(f"Text embeddings collected for batch {i}")

                self.productVibes.productTextBatches.append(text_batch)

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
