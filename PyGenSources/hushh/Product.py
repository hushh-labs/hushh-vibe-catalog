# automatically generated by the FlatBuffers compiler, do not modify

# namespace: hushh

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Product(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Product()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsProduct(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Product
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Product
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Product
    def Description(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Product
    def Url(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Product
    def CharacterizationIds(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # Product
    def CharacterizationIdsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Product
    def CharacterizationIdsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

def ProductStart(builder):
    builder.StartObject(4)

def Start(builder):
    ProductStart(builder)

def ProductAddId(builder, id):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)

def AddId(builder, id):
    ProductAddId(builder, id)

def ProductAddDescription(builder, description):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(description), 0)

def AddDescription(builder, description):
    ProductAddDescription(builder, description)

def ProductAddUrl(builder, url):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(url), 0)

def AddUrl(builder, url):
    ProductAddUrl(builder, url)

def ProductAddCharacterizationIds(builder, characterizationIds):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(characterizationIds), 0)

def AddCharacterizationIds(builder, characterizationIds):
    ProductAddCharacterizationIds(builder, characterizationIds)

def ProductStartCharacterizationIdsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartCharacterizationIdsVector(builder, numElems: int) -> int:
    return ProductStartCharacterizationIdsVector(builder, numElems)

def ProductEnd(builder):
    return builder.EndObject()

def End(builder):
    return ProductEnd(builder)
