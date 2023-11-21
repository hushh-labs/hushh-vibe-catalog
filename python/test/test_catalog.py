import flatbuffers
import numpy as np
import numpy.typing as npt

from hushh.catalog import Catalog, Category, Embedding, Product, Vibe
from hushh.hcf import Catalog as RawCatalog

builder = flatbuffers.Builder(0)


def build_raw_catalog():
    """
    builds a simple catalog to test serialization
    """
    builder = flatbuffers.Builder(0)
    id = builder.CreateString("foo")
    version = builder.CreateString("1.2.0")

    RawCatalog.Start(builder)
    RawCatalog.AddId(builder, id)
    RawCatalog.AddVersion(builder, version)
    cat = RawCatalog.CatalogEnd(builder)
    builder.Finish(cat)
    buf = builder.Output()
    return buf


def test_raw_catalog():
    buf = build_raw_catalog()
    cat = RawCatalog.Catalog.GetRootAsCatalog(buf)
    assert cat.Id() == b"foo"
    assert cat.Version() == b"1.2.0"


def test_catalog():
    cat = Catalog("test")
    cat.id = "foo"
    cat.version = "1.2.0"
    cat.products = []
    builder = flatbuffers.Builder(0)
    cat_end = cat.Pack(builder)
    builder.Finish(cat_end)
    rcat = RawCatalog.Catalog.GetRootAsCatalog(builder.Output())
    assert rcat.Id() == b"foo"
    assert rcat.Version() == b"1.2.0"


def test_embeddings():
    embedding = Embedding([1.0, 2.0, 3.0])
    inv_embedding = Embedding([3.0, 2.0, 1.0])

    categories = []
    for _ in range(0, 3):
        c = Category("category a", "na", [embedding])
        categories.append(c)

    v = Vibe(
        "test_vibe", "test_base64", "test_url", embeddings=[embedding, inv_embedding]
    )

    products = []
    for _ in range(0, 10):
        p = Product("desc", "url", categories=categories, vibes=[v])
        products.append(p)

    catalog = Catalog("test_embeddings", products)
    catalog.id = "foo"
    builder = flatbuffers.Builder(0)
    cat_end = catalog.Pack(builder)
    builder.Finish(cat_end)

    rcat = RawCatalog.Catalog.GetRootAsCatalog(builder.Output())
    assert rcat.Description() == b"test_embeddings"
    assert rcat.ProductsLength() == 10

    # product
    prod = rcat.Products(0)
    assert prod is not None
    assert prod.Id() is not None
    assert prod.Description() == b"desc"
    assert prod.CategoriesLength() == 3
    assert prod.VibesLength() == 1

    # category
    cat = prod.Categories(0)
    assert cat is not None
    assert cat.Id() is not None
    assert cat.Description() == b"category a"
    assert cat.Url() == b"na"
    assert cat.EmbeddingsLength() == 1

    # embedding
    emb = cat.Embeddings(0)
    assert emb is not None
    arr = emb.VAsNumpy()
    assert isinstance(arr, np.ndarray)
    assert arr is not None
    assert len(arr) == 3
    assert emb.VLength() == 3

    # vector
    v = emb.V(0)
    assert v is not None

    # vibe
    vibe = prod.Vibes(0)
    assert vibe is not None
    assert vibe.Id() is not None
    assert vibe.Description() == b"test_vibe"
    assert vibe.Url() == b"test_url"
    assert vibe.ImageBase64() == b"test_base64"
    assert vibe.EmbeddingsLength() == 2

    emb_v = vibe.Embeddings(0)
    assert emb_v is not None
