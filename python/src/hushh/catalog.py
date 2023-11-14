from hushh.hcf.Catalog import CatalogT
from hushh.hcf.Product import ProductT
from hushh.hcf.ProductComposition import ProductCompositionT
from hushh.hcf.ProductMetadata import ProductMetadataT
from hushh.hcf.CharacterizationEmbeddings import CharacterizationEmbeddingsT

# import numpy.typing as npt
# import numpy as np
from typing import Optional
import uuid
from .version import VERSION


class ProductComposition(ProductCompositionT):
    product_ids: list[str]

    def __init__(self, description: str, url: str, product_ids: Optional[list[str]]):
        self.description = description
        self.url = url
        if product_ids is not None:
            self.product_ids = product_ids
        else:
            self.product_ids = []


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

    def __init__(self, products: Optional[list[Product]]):
        self.id = str(uuid.uuid1())
        self.version = VERSION
        if products is not None:
            self.products = products
        else:
            self.products = []


class ProductMetadata(ProductMetadataT):
    def __init__(self, description: str, image_base_64: Optional[str], url: str):
        self.id = str(uuid.uuid1())
        self.description = description
        self.image_base_64 = image_base_64
        self.url = url


class CharacterizationEmbeddings(CharacterizationEmbeddingsT):
    def __init__(self, description: str, image_base_64: Optional[str], url: str):
        self.description = description
        self.image_base_64 = image_base_64
        self.url = url

