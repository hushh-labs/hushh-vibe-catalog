# automatically generated by the FlatBuffers compiler, do not modify

# namespace: hcf

import flatbuffers
from flatbuffers.compat import import_numpy
from typing import Any
from typing import Optional
np = import_numpy()

class ProductInformation(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset: int = 0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ProductInformation()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsProductInformation(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ProductInformation
    def Init(self, buf: bytes, pos: int):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ProductInformation
    def Id(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ProductInformation
    def Description(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ProductInformation
    def ImageBase64(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ProductInformation
    def Url(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def ProductInformationStart(builder: flatbuffers.Builder):
    builder.StartObject(4)

def Start(builder: flatbuffers.Builder):
    ProductInformationStart(builder)

def ProductInformationAddId(builder: flatbuffers.Builder, id: int):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)

def AddId(builder: flatbuffers.Builder, id: int):
    ProductInformationAddId(builder, id)

def ProductInformationAddDescription(builder: flatbuffers.Builder, description: int):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(description), 0)

def AddDescription(builder: flatbuffers.Builder, description: int):
    ProductInformationAddDescription(builder, description)

def ProductInformationAddImageBase64(builder: flatbuffers.Builder, imageBase64: int):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(imageBase64), 0)

def AddImageBase64(builder: flatbuffers.Builder, imageBase64: int):
    ProductInformationAddImageBase64(builder, imageBase64)

def ProductInformationAddUrl(builder: flatbuffers.Builder, url: int):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(url), 0)

def AddUrl(builder: flatbuffers.Builder, url: int):
    ProductInformationAddUrl(builder, url)

def ProductInformationEnd(builder: flatbuffers.Builder) -> int:
    return builder.EndObject()

def End(builder: flatbuffers.Builder) -> int:
    return ProductInformationEnd(builder)


class ProductInformationT(object):

    # ProductInformationT
    def __init__(self):
        self.id = None  # type: str
        self.description = None  # type: str
        self.imageBase64 = None  # type: str
        self.url = None  # type: str

    @classmethod
    def InitFromBuf(cls, buf, pos):
        productInformation = ProductInformation()
        productInformation.Init(buf, pos)
        return cls.InitFromObj(productInformation)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, productInformation):
        x = ProductInformationT()
        x._UnPack(productInformation)
        return x

    # ProductInformationT
    def _UnPack(self, productInformation):
        if productInformation is None:
            return
        self.id = productInformation.Id()
        self.description = productInformation.Description()
        self.imageBase64 = productInformation.ImageBase64()
        self.url = productInformation.Url()

    # ProductInformationT
    def Pack(self, builder):
        if self.id is not None:
            id = builder.CreateString(self.id)
        if self.description is not None:
            description = builder.CreateString(self.description)
        if self.imageBase64 is not None:
            imageBase64 = builder.CreateString(self.imageBase64)
        if self.url is not None:
            url = builder.CreateString(self.url)
        ProductInformationStart(builder)
        if self.id is not None:
            ProductInformationAddId(builder, id)
        if self.description is not None:
            ProductInformationAddDescription(builder, description)
        if self.imageBase64 is not None:
            ProductInformationAddImageBase64(builder, imageBase64)
        if self.url is not None:
            ProductInformationAddUrl(builder, url)
        productInformation = ProductInformationEnd(builder)
        return productInformation