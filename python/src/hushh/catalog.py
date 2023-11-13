from hushh.hcf.Catalog import CatalogT, EmbeddingT
from fastapi import FastAPI

class Catalog(CatalogT):
    list products :
    def __init__(self, id, version):
        self.id = id
        self.version = version


