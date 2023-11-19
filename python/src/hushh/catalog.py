from hushh.hcf.Catalog import CatalogT
from hushh.hcf.Product import ProductT
from hushh.hcf.Category import CategoryT
from hushh.hcf.Embedding import EmbeddingT
from hushh.hcf.Vibe import VibeT

from typing import Optional, cast
import uuid
from .version import VERSION

"""
This module provides classes for creating and managing a catalog of products, categories, and vibes.

Classes:
- Embedding: Represents an embedding.
- Category: Represents a category of products with a description, URL, and vibes.
- Product: Represents a product with a description, URL, and categories.
- Catalog: Represents a catalog of products with a description and a list of products.
- Vibe: Represents a vibe with a description, image, URL, and embeddings.
"""
class Embedding(EmbeddingT):
    """
    Represents an embedding.

    Attributes:
    - id: The unique identifier of the embedding.
    - description: The description of the embedding.
    - value: The value of the embedding.
    """
    def __init__(self, v : Optional[list[float]]):
        if v is not None:
            self.v = v
        else:
            v = []


class Category(CategoryT):
    """
    Represents a category of products.

    Attributes:
    - description: The description of the category.
    - url: The URL of the category.
    - vibes: The list of vibes associated with the category.
    """

    def __init__(self, description: str, url: str, embeddings: list):
        """
        Initialize a new Category instance.

        Parameters:
        - description: The description of the category.
        - url: The URL of the category.
        - vibes: The list of vibes associated with the category.
        """
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

    Attributes:
    - id: The unique identifier of the vibe.
    - description: The description of the vibe.
    - imageBase64: The base64 encoded image of the vibe.
    - url: The URL of the vibe.
    - embeddings: The list of embeddings associated with the vibe.
    """

    def __init__(self, description: str, imageBase64: Optional[str], url: str, embeddings: Optional[list[EmbeddingT]]):
        """
        Initialize a new Vibe instance.

        Parameters:
        - description: The description of the vibe.
        - imageBase64: The base64 encoded image of the vibe.
        - url: The URL of the vibe.
        - embeddings: The list of embeddings associated with the vibe.
        """
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

    Attributes:
    - id: The unique identifier of the product.
    - description: The description of the product.
    - url: The URL of the product.
    - categories: The list of categories the product belongs to.
    """

    def __init__(self, description: str, url: str, categories: Optional[list[Category]] = None, vibes: Optional[list[Vibe]] = None):
        """
        Initialize a new Product instance.

        Parameters:
        - description: The description of the product.
        - url: The URL of the product.
        - categories: The list of categories the product belongs to.
        """
        self.id = str(uuid.uuid1())
        self.description = description
        self.url = url

        if categories is not None:
            self.categories = cast(list[CategoryT], categories)
        else:
            self.categories = []

        if vibes is not None:
            self.vibes = cast(list[VibeT], vibes)
        else:
            self.vibes = []


class Catalog(CatalogT):
    """
    Represents a catalog of products.

    Attributes:
    - id: The unique identifier of the catalog.
    - version: The version of the catalog.
    - description: The description of the catalog.
    - products: The list of products in the catalog.
    """

    products: list[Product]
    id : str

    def __init__(self, description: str, products: Optional[list[Product]] = None):
        """
        Initialize a new Catalog instance.

        Parameters:
        - description: The description of the catalog.
        - products: The list of products in the catalog.
        """
        self.id = str(uuid.uuid1())
        self.version = VERSION
        self.description = description
        if products is not None:
            self.products = products
        else:
            self.products = []


