from hushh.hcf.Catalog import CatalogT
from hushh.hcf.Product import ProductT
# import numpy.typing as npt
# import numpy as np
from dataclasses import dataclass, field
from typing import Optional
from .version import VERSION


@dataclass
class Product(ProductT):
    characterization_ids : list[str] = []
    def __init__(self, id:str, url:str):
        self.id = id
        self.url = url
        self.characterization_ids = []

@dataclass
class Catalog(CatalogT):
    products : list[Product] = field(default_factory=list)
    def __init__(self, id:str, products:Optional[list[Product]]):
        self.id = id
        self.version = VERSION


