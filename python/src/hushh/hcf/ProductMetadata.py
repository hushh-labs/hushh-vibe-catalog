# automatically generated by the FlatBuffers compiler, do not modify

# namespace: hcf

import flatbuffers
from flatbuffers.compat import import_numpy
from typing import Any
from typing import Optional
np = import_numpy()

class ProductMetadata(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset: int = 0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ProductMetadata()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsProductMetadata(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ProductMetadata
    def Init(self, buf: bytes, pos: int):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ProductMetadata
    def Id(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ProductMetadata
    def Description(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ProductMetadata
    def ImageBase64(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ProductMetadata
    def Url(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def ProductMetadataStart(builder: flatbuffers.Builder):
    builder.StartObject(4)

def Start(builder: flatbuffers.Builder):
    ProductMetadataStart(builder)

def ProductMetadataAddId(builder: flatbuffers.Builder, id: int):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)

def AddId(builder: flatbuffers.Builder, id: int):
    ProductMetadataAddId(builder, id)

def ProductMetadataAddDescription(builder: flatbuffers.Builder, description: int):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(description), 0)

def AddDescription(builder: flatbuffers.Builder, description: int):
    ProductMetadataAddDescription(builder, description)

def ProductMetadataAddImageBase64(builder: flatbuffers.Builder, imageBase64: int):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(imageBase64), 0)

def AddImageBase64(builder: flatbuffers.Builder, imageBase64: int):
    ProductMetadataAddImageBase64(builder, imageBase64)

def ProductMetadataAddUrl(builder: flatbuffers.Builder, url: int):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(url), 0)

def AddUrl(builder: flatbuffers.Builder, url: int):
    ProductMetadataAddUrl(builder, url)

def ProductMetadataEnd(builder: flatbuffers.Builder) -> int:
    return builder.EndObject()

def End(builder: flatbuffers.Builder) -> int:
    return ProductMetadataEnd(builder)


class ProductMetadataT(object):

    # ProductMetadataT
    def __init__(self):
        self.id = None  # type: str
        self.description = None  # type: str
        self.imageBase64 = None  # type: str
        self.url = None  # type: str

    @classmethod
    def InitFromBuf(cls, buf, pos):
        productMetadata = ProductMetadata()
        productMetadata.Init(buf, pos)
        return cls.InitFromObj(productMetadata)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, productMetadata):
        x = ProductMetadataT()
        x._UnPack(productMetadata)
        return x

    # ProductMetadataT
    def _UnPack(self, productMetadata):
        if productMetadata is None:
            return
        self.id = productMetadata.Id()
        self.description = productMetadata.Description()
        self.imageBase64 = productMetadata.ImageBase64()
        self.url = productMetadata.Url()

    # ProductMetadataT
    def Pack(self, builder):
        if self.id is not None:
            id = builder.CreateString(self.id)
        if self.description is not None:
            description = builder.CreateString(self.description)
        if self.imageBase64 is not None:
            imageBase64 = builder.CreateString(self.imageBase64)
        if self.url is not None:
            url = builder.CreateString(self.url)
        ProductMetadataStart(builder)
        if self.id is not None:
            ProductMetadataAddId(builder, id)
        if self.description is not None:
            ProductMetadataAddDescription(builder, description)
        if self.imageBase64 is not None:
            ProductMetadataAddImageBase64(builder, imageBase64)
        if self.url is not None:
            ProductMetadataAddUrl(builder, url)
        productMetadata = ProductMetadataEnd(builder)
        return productMetadata