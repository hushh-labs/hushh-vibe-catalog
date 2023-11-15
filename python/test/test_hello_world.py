import flatbuffers
from hushh.hcf import Catalog as RawCatalog
from hushh.catalog import Catalog
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
    builder = flatbuffers.Builder(0)
    cat_end =  cat.Pack(builder)
    builder.Finish(cat_end)
    rcat = RawCatalog.Catalog.GetRootAsCatalog(builder.Output())
    assert rcat.Id() == b"foo"
    assert rcat.Version() == b"1.2.0"

def test_embeddings():
    # for i in 0...10:
    #     p = Product("")
    # cat = Catalog("test2")
    # cat.id = "foo"
    # cat.version = "1.2.0"
    # cat.
    pass


