from typing import Optional, List, cast
import uuid
from .version import VERSION
from hushh.hcf.Catalog import CatalogT
from hushh.hcf.Product import ProductT
from hushh.hcf.Category import CategoryT
from hushh.hcf.Embedding import EmbeddingT
from hushh.hcf.Vibe import VibeT

class Embedding(EmbeddingT):
    """
    Represents an embedding.

    Attributes
    ----------
    v : list[float] or None
        The vector embedding.
    """

    def __init__(self, v: Optional[List[float]] = None):
        if v is not None:
            self.v = v
        else:
            self.v = []


class Category(CategoryT):
    """
    Represents a category of products.

    Attributes
    ----------
    description : str
        The description of the category.
    url : str
        The URL of the category.
    embeddings : list[Embedding] or None
        The list of embeddings associated with the category.
    """

    def __init__(self, description: str, url: str, embeddings: Optional[List[Embedding]] = None):
        self.id = str(uuid.uuid1())
        self.description = description
        self.url = url

        if embeddings is not None:
            self.embeddings = embeddings
        else:
            self.embeddings = []


class Vibe(VibeT):
    """
    Represents a vibe.

    Attributes
    ----------
    id : str
        The unique identifier of the vibe.
    description : str
        The description of the vibe.
    imageBase64 : str or None
        The base64 encoded image of the vibe.
    url : str
        The URL of the vibe.
    embeddings : list[Embedding] or None
        The list of embeddings associated with the vibe.
    """

    def __init__(self, description: str, imageBase64: Optional[str], url: str, embeddings: Optional[List[Embedding]] = None):
        self.id = str(uuid.uuid1())
        self.description = description
        self.imageBase64 = imageBase64
        self.url = url

        if embeddings is not None:
            self.embeddings = embeddings
        else:
            self.embeddings = []


class Product(ProductT):
    """
    Represents a product.

    Attributes
    ----------
    id : str
        The unique identifier of the product.
    description : str
        The description of the product.
    url : str
        The URL of the product.
    categories : list[Category] or None
        The list of categories the product belongs to.
    vibes : list[Vibe] or None
        The list of vibes associated with the product.
    """

    def __init__(self, description: str, url: str, categories: Optional[List[Category]] = None, vibes: Optional[List[Vibe]] = None):
        self.id = str(uuid.uuid1())
        self.description = description
        self.url = url

        if categories is not None:
            self.categories = cast(List[CategoryT], categories)
        else:
            self.categories = []

        if vibes is not None:
            self.vibes = cast(List[VibeT], vibes)
        else:
            self.vibes = []


class Catalog(CatalogT):
    """
    Represents a catalog of products.

    Attributes
    ----------
    id : str
        The unique identifier of the catalog.
    version : str
        The version of the catalog.
    description : str
        The description of the catalog.
    products : list[Product] or None
        The list of products in the catalog.
    """

    def __init__(self, description: str, products: Optional[List[Product]] = None):
        self.id = str(uuid.uuid1())
        self.version = VERSION
        self.description = description

        if products is not None:
            self.products = cast(List[ProductT], products)
        else:
            self.products = []
