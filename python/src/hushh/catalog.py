import uuid
from typing import Any, List, Optional, cast

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


class Category(CategoryT):
    def __init__(self, description: str, url: str, productIdx: Optional[list[int]]):
        self.id = str(uuid.uuid1())
        self.description = description
        self.url = url
        self.productIdx = productIdx if productIdx is not None else []


class ImageVibe(ImageVibeT):
    def __init__(
        self, description: str, base64: Optional[str], productIdx: Optional[list[int]]
    ):
        self.id = str(uuid.uuid1())
        self.description = description
        self.base64 = base64 if base64 is not None else ""
        self.productIdx = productIdx if productIdx is not None else []


class TextVibe(TextVibeT):
    def __init__(
        self, description: str, base64: Optional[str], productIdx: Optional[list[int]]
    ):
        self.id = str(uuid.uuid1())
        self.description = description
        self.base64 = base64
        self.productIdx = productIdx if productIdx is not None else []


class FlatEmbeddingBatch(FlatEmbeddingBatchT):
    def __init__(self, dim: int, type: int, flatTensor: Optional[List[float]] = None):
        self.id = str(uuid.uuid1())
        self.dim = dim
        self.type = type
        self.flatTensor = flatTensor if flatTensor is not None else []


class ProductVibes(ProductVibesT):
    def __init__(
        self,
        products: Optional[list[Product]] = None,
        categories: Optional[list[Category]] = None,
        text: Optional[list[TextVibe]] = None,
        image: Optional[list[ImageVibe]] = None,
        flatBatches: Optional[list[FlatEmbeddingBatch]] = None,
    ):
        self.id = str(uuid.uuid1())

        if products is not None:
            self.products = cast(List[ProductT], products)
        else:
            self.produts = []

        if categories is not None:
            self.categories = cast(List[CategoryT], categories)
        else:
            self.categories = []

        if text is not None:
            self.textVibes = cast(List[TextVibeT], text)
        else:
            self.textVibes = []

        if image is not None:
            self.imageVibes = cast(List[ImageVibeT], image)
        else:
            self.imageVibes = []

        if self.flatBatches is not None:
            self.flatBatches = cast(List[FlatEmbeddingBatchT], flatBatches)
        else:
            self.flatBatches = []


class ImageEncoder:
    def encode(self, a: Any):
        pass


class Catalog(CatalogT):
    def __init__(self, description: str, imageEncoder: ImageEncoder):
        self.id = str(uuid.uuid1())
        self.version = VERSION
        self.description = description
        self.productVibes = ProductVibes()
        self.imageEncoder = imageEncoder

    def addProduct(self, p: Product):
        self.productVibes.products.append(p)
        self.imageEncoder.encode(p.base64)
        pass
