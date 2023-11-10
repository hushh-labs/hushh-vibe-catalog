# automatically generated by the FlatBuffers compiler, do not modify

# namespace: hushh

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CharacterizationEmbeddings(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CharacterizationEmbeddings()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCharacterizationEmbeddings(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CharacterizationEmbeddings
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CharacterizationEmbeddings
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterizationEmbeddings
    def Description(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # CharacterizationEmbeddings
    def Url(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def CharacterizationEmbeddingsStart(builder):
    builder.StartObject(3)

def Start(builder):
    CharacterizationEmbeddingsStart(builder)

def CharacterizationEmbeddingsAddId(builder, id):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)

def AddId(builder, id):
    CharacterizationEmbeddingsAddId(builder, id)

def CharacterizationEmbeddingsAddDescription(builder, description):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(description), 0)

def AddDescription(builder, description):
    CharacterizationEmbeddingsAddDescription(builder, description)

def CharacterizationEmbeddingsAddUrl(builder, url):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(url), 0)

def AddUrl(builder, url):
    CharacterizationEmbeddingsAddUrl(builder, url)

def CharacterizationEmbeddingsEnd(builder):
    return builder.EndObject()

def End(builder):
    return CharacterizationEmbeddingsEnd(builder)