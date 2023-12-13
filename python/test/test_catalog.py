import flatbuffers
from PIL import Image

from hushh.catalog import Catalog, Category, Product
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


def test_catalog_type_with_products():
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
    pvibes = rcat.ProductVibes()
    assert pvibes is not None

    # There are two flatbatches... one for text and one for images.
    assert pvibes.FlatBatchesLength() == 2


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


def test_image_catalog():
    cat = Image.open("assets/cat.jpg")
    dog = Image.open("assets/dog.jpg")
    bird = Image.open("assets/bird.jpg")

    catalog = Catalog("image_test")

    cat_product = Product("cat", "test_url", cat)
    dog_product = Product("dog", "test_url", dog)
    bird_product = Product("bird", "test_url", bird)

    catalog.addProduct(cat_product)
    catalog.addProduct(dog_product)
    catalog.addProduct(bird_product)

    builder = flatbuffers.Builder(0)
    cat_end = catalog.Pack(builder)
    builder.Finish(cat_end)

    rcat = RawCatalog.Catalog.GetRootAsCatalog(builder.Output())
    vibes = rcat.ProductVibes()
    assert vibes is not None

    assert vibes.FlatBatchesLength() > 0
