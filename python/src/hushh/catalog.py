import uuid
from typing import List, Optional, cast

from hushh.hcf.Catalog import CatalogT
from hushh.hcf.Category import CategoryT
from hushh.hcf.FlatEmbeddingBatch import FlatEmbeddingBatchT
from hushh.hcf.ImageVibe import ImageVibeT
from hushh.hcf.Product import ProductT
from hushh.hcf.TextVibe import TextVibeT

from .version import VERSION


class FlatEmbeddingBatch(FlatEmbeddingBatchT):
    def __init__(self, dim: int, type: int, flatTensor: Optional[List[float]] = None):
        self.id = str(uuid.uuid1())
        self.dim = dim
        self.type = type
        self.flatTensor = flatTensor if flatTensor is not None else []


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


class Product(ProductT):
    def __init__(self, description: str, url: str, base64: str, imgUrl: str):
        self.id = str(uuid.uuid1())
        self.description = description
        self.url = url
        self.base64 = base64
        self.imgUrl = imgUrl


class Catalog(CatalogT):
    def __init__(
        self,
        description: str,
        products: Optional[list[Product]] = None,
        textVibes: Optional[list[TextVibe]] = None,
        imageVibes: Optional[list[ImageVibe]] = None,
        categories: Optional[list[Category]] = None,
        flatEmbeddingBatches: Optional[list[FlatEmbeddingBatch]] = None,
    ):
        self.id = str(uuid.uuid1())
        self.version = VERSION
        self.description = description

        if categories is not None:
            self.categories = cast(List[CategoryT], categories)
        else:
            self.categories = []

        if self.flatBatches is not None:
            self.flatBatches = cast(List[FlatEmbeddingBatchT], flatEmbeddingBatches)
        else:
            self.flatBatches = []

        if products is not None:
            self.products = cast(List[ProductT], products)
        else:
            self.produts = []

        if textVibes is not None:
            self.textVibes = cast(List[TextVibeT], textVibes)
        else:
            self.textVibes = []

        if imageVibes is not None:
            self.imageVibes = cast(List[ImageVibeT], textVibes)
        else:
            self.imageVibes = []
