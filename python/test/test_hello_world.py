import flatbuffers
from hushh.hcf import Catalog
builder = flatbuffers.Builder(0)

def test_product():
    builder = flatbuffers.Builder(0)
    id = builder.CreateString("foo")
    head = builder.CreateString("bar")
    version = builder.CreateString("1.2.0")

    Catalog.Start(builder)
    Catalog.AddId(builder, id)
    Catalog.AddHead(builder, head)
    Catalog.AddVersion(builder, version)
    cat = Catalog.CatalogEnd(builder)
    builder.Finish(cat)
    buf = builder.Output()
    cat = Catalog.Catalog.GetRootAsCatalog(buf)
    assert cat.Id() == b"foo"
    assert cat.Head() == b"bar"
    assert cat.Version() == b"1.2.0"


