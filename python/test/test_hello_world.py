import flatbuffers

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

    v = Vibe("test_vibe", "", "", embeddings = [embedding, inv_embedding])

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
