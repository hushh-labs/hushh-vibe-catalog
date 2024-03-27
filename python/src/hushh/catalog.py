import uuid
from collections.abc import Iterable
from itertools import islice
from typing import Dict, List, Optional, Union

import flatbuffers
import numpy as np
import pandas as pd
import torch
from PIL import Image
from PIL.Image import Image as ImageT
from transformers import (CLIPModel, CLIPProcessor, CLIPTokenizer,
                          PreTrainedModel, PreTrainedTokenizer, ProcessorMixin)

import hushh
from hushh._version import __version__
from hushh.errors import NoEmbeddableContent, UncallableProcessor
from hushh.hcf.Brand import BrandT
from hushh.hcf.Catalog import CatalogT
from hushh.hcf.Category import CategoryT
from hushh.hcf.FlatEmbeddingBatch import FlatEmbeddingBatchT
from hushh.hcf.Product import ProductT
from hushh.hcf.ProductVibes import ProductVibesT
from hushh.hcf.Vibe import VibeT
from hushh.hcf.VibeMode import VibeMode


def _batched(iterable, n):
    """
    Batch data into tuples of length n. The last batch may be shorter.

    Parameters
    ----------
    iterable : iterable
        The iterable containing the data to be batched.
    n : int
        The desired length of each batch.

    Yields
    ------
    tuple
        A tuple containing elements from the iterable, with each tuple having
        a length of at most n.
    """
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


def read_hcf(filename: str):
    with open(filename, "rb") as fh:
        cat = hushh.hcf.Catalog.Catalog.GetRootAsCatalog(fh.read())
    return cat


class IdBase:
    id: str
    _id_base = "IDB"

    def genId(self):
        return self._id_base + "-" + str(uuid.uuid1())


class Brand(BrandT, IdBase):
    """Represents a brand

    Attributes
    ----------
    name : str
        The name of the brand.
    description : str
        The description of the brand.
    url : str
        The URL of the brand.

    Parameters
    ----------
    name : str
        The name of the brand.
    description : str
        The description of the brand.
    url : str
        The URL of the brand.
    """

    _id_base = "BRD"

    def __init__(self, name: str, description: str, url: str):
        """
        Initializes a Brand object.

        Parameters
        ----------
        name : str
            The name of the brand.
        description : str
            The description of the brand.
        url : str
            The URL of the brand.
        """
        self.id = self.genId()
        self.name = name
        self.description = description
        self.url = url


class Product(ProductT, IdBase):
    """Represents a product by a given brand.

    Attributes
    ----------
    description : str
        The description of the product.
    url : str
        The URL of the product.
    image_path : str
        The path to the image of the product.
    brand : Brand
        The brand of the product.
    textVibes : list
        A list of text vibes associated with the product.
    imageVibes : list
        A list of image vibes associated with the product.

    Parameters
    ----------
    description : str
        The description of the product.
    url : str
        The URL of the product.
    image_path : str
        The path to the image of the product.
    brand : Brand
        The brand of the product.

    Raises
    ------
    NoEmbeddableContent
        If the description is missing.
    """

    def __init__(self, description: str, url: str, image_path: str, brand: Brand):
        """
        Initializes a Product object.

        Parameters
        ----------
        description : str
            The description of the product.
        url : str
            The URL of the product.
        image_path : str
            The path to the image of the product.
        brand : Brand
            The brand of the product.

        Raises
        ------
        NoEmbeddableContent
            If the description is missing.
        """
        self.id = self.genId()
        if pd.isna(description):
            raise NoEmbeddableContent("Missing description of product")

        self.description = description
        self.url = url
        self.image_path = image_path
        self.brand = brand
        self.textVibes = []
        self.imageVibes = []

    def __repr__(self):
        """
        Returns a string representation of the Product object.

        Returns
        -------
        str
            A string representation of the Product object showing the number of text vibes and image vibes associated with it.
        """
        return f"Product(textVibes:{len(self.textVibes)}, imageVibes:{len(self.imageVibes)})"


class VibeBase(IdBase):
    _products: Dict[str, int] = {}

    def addProductTarget(self, p: Product | str):
        if isinstance(p, str):
            self._products[p] = True
        else:
            self._products[p.id] = True


class Category(CategoryT, VibeBase):
    """Represents a category of products.

    Attributes:
        description (str): A description of the category.
        url (str): The URL associated with the category.
        productIx (list): A list of indices representing products associated with this category.

    Methods:
        __init__(self, description: str, url: str): Initializes a Category instance.

    Example:
        category = Category("Electronics", "https://example.com/electronics")
    """

    _id_base = "CTG"

    def __init__(self, description: str, url: str):
        """
        Initializes a Category instance.

        Args:
            description (str): A description of the category.
            url (str): The URL associated with the category.

        Returns:
            None

        Example:
            category = Category("Electronics", "https://example.com/electronics")
        """
        self.id = self.genId()
        self.description = description
        self.url = url
        self.productIx = []


class Vibe(VibeT, VibeBase):
    """
    Represents a vibe associated with products.

    This class combines features from `VibeT` and `VibeBase`.

    Attributes:
        description (str): A description of the vibe.
        image_path (str): The path to the image associated with the vibe.
        productIdx (list): A list of indices representing products associated with this vibe.

    Methods:
        __init__(self, image_path: str, description: str): Initializes a Vibe instance.

    Example:
        vibe = Vibe("path/to/image.jpg", "Pants")
    """

    _id_base = "IVB"
    def __init__(self, image_path: str, description: str):
        """
        Initializes a Vibe instance.

        Args:
            image_path (str): The path to the image associated with the vibe.
            description (str): A description of the vibe.

        Returns:
            None

        Example:
            vibe = Vibe("path/to/image.jpg", "Trendy")
        """
        self.id = self.genId()
        self.description = description
        self.image_path = image_path
        self.productIdx = []


class FlatEmbeddingBatch(FlatEmbeddingBatchT, IdBase):
    """ Represents a batch of flat embeddings associated with products.

    This class combines features from FlatEmbeddingBatchT and IdBase.

    Attributes
    ----------
    shape : List[int]
        The shape of the flat embedding tensor.
    vibeMode : int
        The vibe mode associated with the flat embeddings.
    flatTensor : List[float]
        The flat embedding tensor.
    productIdx : List[int]
        A list of indices representing products associated with this batch of flat embeddings.

    """

    _id_base = "FEB"

    def __init__(
        self,
        shape: List[int],
        vibeMode: int,
        flatTensor: List[float],
        productIdx: List[int],
    ) -> None:
        """
        Initializes a FlatEmbeddingBatch instance.

        Parameters
        ----------
        shape : List[int]
            The shape of the flat embedding tensor.
        vibeMode : int
            The vibe mode associated with the flat embeddings.
        flatTensor : List[float]
            The flat embedding tensor.
        productIdx : List[int]
            A list of indices representing products associated with this batch of flat embeddings.

        Returns
        -------
        None

        Examples
        --------
        >>> flat_batch = FlatEmbeddingBatch([10, 10, 3], 1, [0.1, 0.2, ...], [0, 1, 2])
        """
        self.id = self.genId()
        self.shape = shape
        self.vibeMode = vibeMode
        self.flatTensor = flatTensor
        self.productIdx = productIdx


class ProductVibes(ProductVibesT, VibeBase):
    _id_base = "PVB"

    def __init__(self):
        self.id = self.genId()
        self.products = []

        self.categories = []
        self._categories = {}

        self.vibes = []
        self._vibes = {}
        self._brands = {}

        self.productTextBatches = []
        self.productImageBatches = []
        self.textBatches = []
        self.imageBatches = []
        self.brands = []


class Catalog(CatalogT, IdBase):
    """Represents a collection of products by one or more brands.

    Attributes
    ----------
    productVibes : ProductVibes
        Object containing product vibes.
    model : PreTrainedModel
        Pre-trained model for embeddings.
    processor : ProcessorMixin
        Processor for handling inputs.
    tokenizer : PreTrainedTokenizer
        Tokenizer for processing text inputs.
    """

    def __init__(
        self,
        description: str,
        batchSize: int = 10000,
        model: Union[PreTrainedModel, None] = None,
        processor: Union[ProcessorMixin, None] = None,
        tokenizer: Union[PreTrainedTokenizer, None] = None,
    ) -> None:
        """
        Initialize Catalog object.

        Parameters
        ----------
        description : str
            Description of the catalog.
        batchSize : int, optional
            Batch size for processing embeddings, by default 10000.
        model : Union[PreTrainedModel, None], optional
            Pre-trained model for embeddings, by default None.
        processor : Union[ProcessorMixin, None], optional
            Processor for handling inputs, by default None.
        tokenizer : Union[PreTrainedTokenizer, None], optional
            Tokenizer for processing text inputs, by default None.
        """
        self.id = self.genId()
        self.version = __version__
        self.description = description

        self.productTextFeatures = []
        self.productImageFeatures = []

        self.batchSize = batchSize
        self.brands = []

        if model is not None:
            self.model = model
        else:
            self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")

        self.model_name_or_path = self.model.name_or_path

        if processor is not None:
            self.processor = processor
        else:
            self.processor = CLIPProcessor.from_pretrained(
                "openai/clip-vit-base-patch32"
            )

        if tokenizer is not None:
            self.tokenizer = tokenizer
        else:
            self.tokenizer = CLIPTokenizer.from_pretrained(
                "openai/clip-vit-base-patch32"
            )

        self.modelNameOrPath = self.model.name_or_path
        self.tokenizerNameOrPath = self.tokenizer.name_or_path

        self.productVibes = ProductVibes()

    def __repr__(self) -> str:
        """
        Return a string representation of the Catalog object.
        """
        return f"Catalog(productVibes.products: {len(self.productVibes.products)})"

    def to_hcf(self, filename: str) -> None:
        """
        Convert Catalog object to HCF file format.

        Parameters
        ----------
        filename : str
            Name of the HCF file.
        """
        if not filename.endswith(".hcf"):
            filename = filename + ".hcf"
        with open(filename, "wb") as fh:
            builder = flatbuffers.Builder(0)
            cat_end = self.Pack(builder)
            builder.Finish(cat_end)
            fh.write(builder.Output())

    def renderProductFlatBatch(self) -> None:
        """
        Render product embeddings in flat batch format.
        """
        model = self.model
        with torch.no_grad():
            for i, batch in enumerate(
                _batched(self.productVibes.products, self.batchSize)
            ):
                images = []
                texts = []
                for p in batch:
                    with open(p.image_path, "rb") as fh:
                        image = np.array(Image.open(fh).convert("RGB"))
                        images.append(image)
                    texts.append(p.description)

                print(f"Collected images and text for batch {i}")

                if not texts and not images:
                    raise NoEmbeddableContent()
                inputs = None

                if callable(self.processor):
                    inputs = self.processor(
                        text=texts,
                        images=images,
                        return_tensors="pt",
                        padding=True,
                    )
                else:
                    raise UncallableProcessor()

                del images
                del texts

                print(f"Collected inputs for batch {i}")

                image_features = model.get_image_features(
                    pixel_values=inputs.pixel_values,
                )
                text_features = model.get_text_features(
                    input_ids=inputs.input_ids,
                )
                del inputs

                print(f"Collected Image and text features for batch {i}")

                image_batch = FlatEmbeddingBatch(
                    shape=image_features.shape,
                    flatTensor=image_features.flatten().tolist(),
                    vibeMode=VibeMode.ProductImage,
                    productIdx=list(range(i * self.batchSize, i + 1 * self.batchSize)),
                )
                print(f"Image embeddings collected for batch {i}")
                self.productVibes.productImageBatches.append(image_batch)

                text_batch = FlatEmbeddingBatch(
                    shape=text_features.shape,
                    flatTensor=text_features.flatten().tolist(),
                    vibeMode=VibeMode.ProductText,
                    productIdx=list(range(i * self.batchSize, i + 1 * self.batchSize)),
                )

                print(f"Text embeddings collected for batch {i}")

                self.productVibes.productTextBatches.append(text_batch)

    def Pack(self, builder) -> int:
        """
        Pack Catalog object using FlatBuffers.

        Parameters
        ----------
        builder : flatbuffers.Builder
            FlatBuffer builder object.

        Returns
        -------
        int
            Offset of the packed Catalog object.
        """
        self.renderProductFlatBatch()
        return super().Pack(builder)

    def addProduct(self, p: Product) -> None:
        """
        Add a product to the Catalog.

        Parameters
        ----------
        p : Product
            Product object to add.
        """
        if p.id in self.productVibes._products:
            raise ValueError(f"Product {p.id} already exists")
        else:
            self.productVibes._products[p.id] = len(self.productVibes.products)

        self.productVibes.products.append(p)

    def addProductCategory(self, c: Category) -> None:
        """
        Add a product category to the Catalog.

        Parameters
        ----------
        c : Category
            Category object to add.
        """
        if c.id in self.productVibes._categories:
            raise ValueError(f"Category {c.id} already exists")
        self.productVibes._categories[c.id] = len(self.productVibes.categories)
        self.productVibes.categories.append(c)

    def addProductVibe(self, v: Vibe) -> None:
        """
        Add a product vibe to the Catalog.

        Parameters
        ----------
        v : Vibe
            Vibe object to add.
        """
        if v.id in self.productVibes._vibes:
            raise ValueError(f"Vibe {v.id} already exists")
        self.productVibes._vibes[v.id] = len(self.productVibes.vibes)
        self.product

