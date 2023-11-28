import uuid
from typing import Dict, List, Optional

from PIL import Image
from transformers import ProcessorMixin

from hushh.hcf.Catalog import CatalogT
from hushh.hcf.Category import CategoryT
from hushh.hcf.FlatEmbeddingBatch import FlatEmbeddingBatchT
from hushh.hcf.ImageVibe import ImageVibeT
from hushh.hcf.Product import ProductT
from hushh.hcf.ProductVibes import ProductVibesT
from hushh.hcf.TextVibe import TextVibeT

from .version import VERSION


class Product(ProductT):
    def __init__(self, description: str, url: str, base64: str, imgUrl: str):
        self.id = str(uuid.uuid1())
        self.description = description
        self.url = url
        self.base64 = base64
        self.imgUrl = imgUrl
        self.textVibes = []
        self.imageVibes = []


class IdBase:
    id: str
    base = ""

    def genId(self):
        return self.base + "-" + str(uuid.uuid1())


class VibeBase(IdBase):
    _products: Dict[str, int] = {}

    def addProduct(self, p: Product | str):
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


class ImageVibe(ImageVibeT, VibeBase):
    def __init__(self, image: Image, description: str):
        self.base = "IVB"
        self.id = str(uuid.uuid1())
        self.description = description
        # self.base64 = base64 if base64 is not None else ""
        self.productIdx = []


class TextVibe(TextVibeT, VibeBase):
    def __init__(self, text: str, description: Optional[str] = None):
        self.base = "TVB"
        self.id = self.genId()
        self.description = description
        self.text = text
        self.productIdx = []


class FlatEmbeddingBatch(FlatEmbeddingBatchT, IdBase):
    def __init__(self, dim: int, type: int, flatTensor: Optional[List[float]] = None):
        self.base = "FEB"
        self.id = self.genId()
        self.dim = dim
        self.type = type
        self.flatTensor = flatTensor if flatTensor is not None else []


class ProductVibes(ProductVibesT, VibeBase):
    def __init__(self):
        self.base = "PVB"
        self.id = self.genId()
        self.products = []

        self.categories = []
        self._categories = {}

        self.text = []
        self._text = {}

        self.image = []
        self._image = {}

        self.flatBatches = []


class Catalog(CatalogT, IdBase):
    productVibes: ProductVibes

    def __init__(self, description: str, processor: ProcessorMixin):
        self.base = "CLG"
        self.id = self.genId()
        self.version = VERSION
        self.description = description
        self.productVibes = ProductVibes()
        self.processor = processor

    def addProduct(self, p: Product):
        if p.id in self.productVibes._products:
            raise ValueError(f"Product {p.id} already exists")
        self.productVibes._products[p.id] = len(self.productVibes.products)
        self.productVibes.products.append(p)

    def addProductCategory(self, c: Category):
        if c.id in self.productVibes._categories:
            raise ValueError(f"Category {c.id} already exists")
        self.productVibes._categories[c.id] = len(self.productVibes.categories)
        self.productVibes.categories.append(c)

    def addProductImageVibe(self, iv: ImageVibe):
        if iv.id in self.productVibes._image:
            raise ValueError(f"ImageVibe {iv.id} already exists")
        self.productVibes._image[iv.id] = len(self.productVibes.text)
        self.productVibes.image.append(iv)

    def addProductTextVibe(self, tv: TextVibe):
        if tv.id in self.productVibes._text:
            raise ValueError(f"TextVibe {tv.id} already exists")
        self.productVibes._text[tv.id] = len(self.productVibes.text)
        self.productVibes.text.append(tv)

    def linkProductCategory(self, p_id: str, c_id: str):
        if p_id not in self.productVibes._products:
            raise ValueError(f"Product {p_id} does not exist in Catalog")
        if c_id not in self.productVibes._categories:
            raise ValueError(f"Category {c_id} does not exist in Catalog")

        c_idx = self.productVibes._categories[c_id]
        p_idx = self.productVibes._products[p_id]
        self.productVibes.categories[c_idx].productIdx.append(p_idx)

    def linkProductTextVibe(self, p_id: str, tv_id: str):
        if p_id not in self.productVibes._products:
            raise ValueError(f"Product {p_id} does not exist in Catalog")
        if tv_id not in self.productVibes._text:
            raise ValueError(f"TextVibe {tv_id} does not exist in Catalog")

        p_idx = self.productVibes._products[p_id]
        tv_idx = self.productVibes._text[tv_id]
        self.productVibes.text[tv_idx].productIdx.append(p_idx)

    def linkProductImageVibe(self, p_id: str, iv_id: str):
        if p_id not in self.productVibes._products:
            raise ValueError(f"Product {p_id} does not exist in Catalog")
        if iv_id not in self.productVibes._text:
            raise ValueError(f"ImageVibe {iv_id} does not exist in Catalog")

        p_idx = self.productVibes._products[p_id]
        iv_idx = self.productVibes._text[iv_id]
        self.productVibes.text[iv_idx].productIdx.append(p_idx)
