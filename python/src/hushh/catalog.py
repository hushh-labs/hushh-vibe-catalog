from hushh.hcf.Catalog import CatalogT
from hushh.hcf.Product import ProductT
from hushh.hcf.Category import CategoryT
from hushh.hcf.Embedding import EmbeddingT
from hushh.hcf.Vibe import VibeT

# import numpy.typing as npt
# import numpy as np
from typing import Optional
import uuid
from .version import VERSION


class Embedding(EmbeddingT):
    pass

class Category(CategoryT):
    def __init__(self, description: str, url: str, embeddings: Optional[list[EmbeddingT]]):
        self.description = description
        self.url = url
        if embeddings is not None:
            self.embeddings = embeddings
        else:
            self.embeddings = []


class Product(ProductT):
    characterization_ids: list[str]

    def __init__(self, url: str, characterization_ids: Optional[list[str]]):
        self.id = str(uuid.uuid1())
        self.url = url
        if characterization_ids is not None:
            self.characterization_ids = characterization_ids
        else:
            self.characterization_ids = []


class Catalog(CatalogT):
    products: list[Product]

    def __init__(self, description: str, products: Optional[list[Product]] = None):
        self.id = str(uuid.uuid1())
        self.version = VERSION
        self.description = description
        if products is not None:
            self.products = products
        else:
            self.products = []


class Vibe(VibeT):
    def __init__(self, description: str, image_base_64: Optional[str], url: str, embeddings: Optional[list[EmbeddingT]]):
        self.id = str(uuid.uuid1())

        self.description = description
        self.image_base_64 = image_base_64
        self.url = url
        if embeddings is not None:
            self.embeddings = embeddings
        else:
            self.embeddings = []

