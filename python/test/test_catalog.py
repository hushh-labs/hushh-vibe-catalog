import flatbuffers
from PIL import Image
from transformers import CLIPModel, CLIPProcessor

from hushh.catalog import Catalog, Category, Product, Vibe
from hushh.hcf import Catalog as RawCatalog

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

builder = flatbuffers.Builder(0)
dummy_image = Image.new(mode="RGB", size=(10, 10))


def build_product():
    return Product("test_product", "test_url", dummy_image, "test_imageUrl")


def test_product():
    p = build_product()
    assert p.description == "test_product"
    assert p.url == "test_url"
    image = Image.new(mode="RGB", size=(10, 10))
    base64_payload = "/9j/4AAQSk"

    assert p.imageUrl == "test_imageUrl"


def build_catalog():
    return Catalog("test_description", processor)


def test_catalog():
    c = build_catalog()
    assert c.description == "test_description"


def build_category():
    return Category("test_category", "test_url")


def test_catalog_product_category():
    c = build_catalog()
    p = build_product()
    c.addProduct(p)
    assert len(c.productVibes.products) == 1
    cgy = build_category()

    cgy.addProduct(p)
    assert p.id in cgy._products
    assert cgy.description == "test_category"
    assert cgy.url == "test_url"


def test_product_vibe_link():
    c = build_catalog()
    p = build_product()
    c.addProduct(p)
    image = Image.new(mode="RGB", size=(10, 10))
    v = Vibe(image, "test_description")
    c.addProductVibe(v)
    assert len(c.productVibes.vibes) == 1

    base64_payload = "/9j/4AAQSk"
    assert c.productVibes.vibes[0].base64[:10] == base64_payload
    assert c.productVibes.vibes[0].description == "test_description"


def test_catalog_pack():
    c = build_catalog()
    p = build_product()
    c.addProduct(p)
    image = Image.new(mode="RGB", size=(10, 10))
    v = Vibe(image, "test_description")
    c.addProductVibe(v)
    c.renderProductFlatBatch()
    pass


# def build_raw_catalog():
#     """
#     builds a simple catalog to test serialization
#     """
#     builder = flatbuffers.Builder(0)
#     id = builder.CreateString("foo")
#     version = builder.CreateString("1.2.0")

#     RawCatalog.Start(builder)
#     RawCatalog.AddId(builder, id)
#     RawCatalog.AddVersion(builder, version)
#     cat = RawCatalog.CatalogEnd(builder)
#     builder.Finish(cat)
#     buf = builder.Output()
#     return buf


# def test_raw_catalog():
#     buf = build_raw_catalog()
#     cat = RawCatalog.Catalog.GetRootAsCatalog(buf)
#     assert cat.Id() == b"foo"
#     assert cat.Version() == b"1.2.0"


# def test_catalog():
#     cat = Catalog("test")
#     cat.id = "foo"
#     cat.version = "1.2.0"
#     cat.products = []
#     builder = flatbuffers.Builder(0)
#     cat_end = cat.Pack(builder)
#     builder.Finish(cat_end)
#     rcat = RawCatalog.Catalog.GetRootAsCatalog(builder.Output())
#     assert rcat.Id() == b"foo"
#     assert rcat.Version() == b"1.2.0"


# def test_embeddings():
#     embedding = Embedding([1.0, 2.0, 3.0])
#     inv_embedding = Embedding([3.0, 2.0, 1.0])

#     categories = []
#     for _ in range(0, 3):
#         c = Category("category a", "na", [embedding])
#         categories.append(c)

#     v = Vibe(
#         "test_vibe", "test_base64", "test_url", embeddings=[embedding, inv_embedding]
#     )

#     products = []
#     for _ in range(0, 10):
#         p = Product("desc", "url", "dummy_image", "dummy_url")
#         products.append(p)

#     catalog = Catalog("test_embeddings", products)
#     catalog.id = "foo"
#     builder = flatbuffers.Builder(0)
#     cat_end = catalog.Pack(builder)
#     builder.Finish(cat_end)

#     rcat = RawCatalog.Catalog.GetRootAsCatalog(builder.Output())

#     assert rcat.Description() == b"test_embeddings"
#     assert rcat.ProductsLength() == 10

#     # product
#     prod = rcat.Products(0)
#     assert prod is not None
#     assert prod.Id() is not None
#     assert prod.Description() == b"desc"
#     assert prod.Base64() == b"dummy_image"
#     assert prod.Url() == b"dummy_url"

#     # category
#     cat = rcat.Categories(0)
#     assert cat is not None
#     assert cat.Id() is not None
#     assert cat.Description() == b"category a"
#     assert cat.Url() == b"na"

#     # embedding

#     # vibe
#     assert vibe is not None
#     assert vibe.Id() is not None
#     assert vibe.Description() == b"test_vibe"
#     assert vibe.Url() == b"test_url"
#     assert vibe.ImageBase64() == b"test_base64"
#     assert vibe.EmbeddingsLength() == 2

#     emb_v = vibe.Embeddings(0)
#     assert emb_v is not None
