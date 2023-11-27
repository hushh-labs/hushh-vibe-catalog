import uuid
from typing import Dict, List, Optional, cast

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


class VibeBase:
    _products: Dict[str, bool] = {}
    productIdx: list[int] = []


class Category(CategoryT, VibeBase):
    def __init__(self, description: str, url: str):
        self.id = str(uuid.uuid1())
        self.description = description
        self.url = url

    def addProduct(self, p: Product | str):
        if isinstance(p, str):
            self._products[p] = True
        else:
            self._products[p.id] = True


class ImageVibe(ImageVibeT, VibeBase):
    def __init__(self, description: str, base64: Optional[str]):
        self.id = str(uuid.uuid1())
        self.description = description
        self.base64 = base64 if base64 is not None else ""


class TextVibe(TextVibeT, VibeBase):
    def __init__(self, description: str, base64: Optional[str]):
        self.id = str(uuid.uuid1())
        self.description = description
        self.base64 = base64


class FlatEmbeddingBatch(FlatEmbeddingBatchT):
    def __init__(self, dim: int, type: int, flatTensor: Optional[List[float]] = None):
        self.id = str(uuid.uuid1())
        self.dim = dim
        self.type = type
        self.flatTensor = flatTensor if flatTensor is not None else []


class ProductVibes(ProductVibesT):
    def __init__(
        self,
    ):
        self.id = str(uuid.uuid1())
        self.products = []
        self.categories = []
        self.text = []
        self.image = []
        self.flatBatches = []


class Catalog(CatalogT):
    productVibes: ProductVibes

    def __init__(self, description: str, processor: ProcessorMixin):
        self.id = str(uuid.uuid1())
        self.version = VERSION
        self.description = description
        self.productVibes = ProductVibes()
        self.processor = processor

    def addProduct(self, p: Product):
        self.productVibes.products.append(p)

    def addProductCategory(self, c: Category):
        self.productVibes.categories.append(c)

    def addProductTextVibe(self, p: Product | str, t: TextVibe | str):
        if p.id not in self.productVibes._products:
            self.addProduct(p)

        self.productVibes.text.append(t)

    def addProductImageVibe(self, p: Product, i: ImageVibe | str):
        self.productVibes.image.append(i)
