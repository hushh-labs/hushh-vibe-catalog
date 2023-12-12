import flatbuffers
from PIL import Image

from hushh.catalog import Catalog, Category, Product, Vibe
from hushh.hcf import Catalog as RawCatalog

builder = flatbuffers.Builder(0)


def create_image():
    image = Image.new("RGB", (512, 512))
    return image


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

    image = create_image()
    p = Product("desc", "url", image)
    cat.addProduct(p)
    builder = flatbuffers.Builder(0)

    cat_end = cat.Pack(builder)

    builder.Finish(cat_end)
    rcat = RawCatalog.Catalog.GetRootAsCatalog(builder.Output())
    assert rcat.Id() == b"foo"
    assert rcat.Version() == b"1.2.0"


def test_embeddings():
    embedding = [1.0, 2.0, 3.0]
    inv_embedding = [3.0, 2.0, 1.0]

    categories = []
    for _ in range(0, 3):
        c = Category("category a", "test_url")
        categories.append(c)

    catalog = Catalog("test_embeddings")
    catalog.id = "foo"
    for _ in range(0, 10):
        p = Product("desc", "url", create_image())
        catalog.addProduct(p)

    builder = flatbuffers.Builder(0)
    cat_end = catalog.Pack(builder)
    builder.Finish(cat_end)

    rcat = RawCatalog.Catalog.GetRootAsCatalog(builder.Output())

    assert rcat.Description() == b"test_embeddings"
