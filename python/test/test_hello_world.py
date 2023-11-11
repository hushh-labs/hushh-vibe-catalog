import flatbuffers
from hushh.hcf import Catalog as RawCatalog
from hushh.hcf.Catalog import CatalogT
builder = flatbuffers.Builder(0)

def build_raw_catalog():
    """
    builds a simple catalog to test serialization
    """
    builder = flatbuffers.Builder(0)
    id = builder.CreateString("foo")
    head = builder.CreateString("bar")
    version = builder.CreateString("1.2.0")

    RawCatalog.Start(builder)
    RawCatalog.AddId(builder, id)
    RawCatalog.AddHead(builder, head)
    RawCatalog.AddVersion(builder, version)
    cat = RawCatalog.CatalogEnd(builder)
    builder.Finish(cat)
    buf = builder.Output()
    return buf


def test_raw_catalog():
    buf = build_raw_catalog()
    cat = RawCatalog.Catalog.GetRootAsCatalog(buf)
    assert cat.Id() == b"foo"
    assert cat.Head() == b"bar"
    assert cat.Version() == b"1.2.0"


class Catalog(CatalogT):
    pass

def test_catalog():
    cat = Catalog()
    cat.id = "foo"
    cat.head = "bar"
    cat.version = "1.2.0"
    builder = flatbuffers.Builder(0)
    cat_end =  cat.Pack(builder)
    builder.Finish(cat_end)
    rcat = RawCatalog.Catalog.GetRootAsCatalog(builder.Output())
    assert rcat.Id() == b"foo"
    assert rcat.Head() == b"bar"
    assert rcat.Version() == b"1.2.0"



