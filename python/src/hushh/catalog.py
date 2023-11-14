from hushh.hcf.Catalog import CatalogT
from hushh.hcf.Product import ProductT
from hushh.hcf.ProductCharacterization import ProductCharacterizationT

# import numpy.typing as npt
# import numpy as np
from typing import Optional
import uuid
from .version import VERSION


class ProductCharacterization(ProductCharacterizationT):
    product_ids: list[str]


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
