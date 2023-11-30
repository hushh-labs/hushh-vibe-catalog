# automatically generated by the FlatBuffers compiler, do not modify

# namespace: hcf

import flatbuffers
from flatbuffers.compat import import_numpy
from typing import Any
from typing import Optional
np = import_numpy()

class Vibe(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset: int = 0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Vibe()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsVibe(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Vibe
    def Init(self, buf: bytes, pos: int):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Vibe
    def Id(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Vibe
    def Base64(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Vibe
    def Description(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Vibe
    def ImageUrl(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Vibe
    def ProductIdx(self, j: int):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # Vibe
    def ProductIdxAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # Vibe
    def ProductIdxLength(self) -> int:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Vibe
    def ProductIdxIsNone(self) -> bool:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

def VibeStart(builder: flatbuffers.Builder):
    builder.StartObject(5)

def Start(builder: flatbuffers.Builder):
    VibeStart(builder)

def VibeAddId(builder: flatbuffers.Builder, id: int):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)

def AddId(builder: flatbuffers.Builder, id: int):
    VibeAddId(builder, id)

def VibeAddBase64(builder: flatbuffers.Builder, base64: int):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(base64), 0)

def AddBase64(builder: flatbuffers.Builder, base64: int):
    VibeAddBase64(builder, base64)

def VibeAddDescription(builder: flatbuffers.Builder, description: int):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(description), 0)

def AddDescription(builder: flatbuffers.Builder, description: int):
    VibeAddDescription(builder, description)

def VibeAddImageUrl(builder: flatbuffers.Builder, imageUrl: int):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(imageUrl), 0)

def AddImageUrl(builder: flatbuffers.Builder, imageUrl: int):
    VibeAddImageUrl(builder, imageUrl)

def VibeAddProductIdx(builder: flatbuffers.Builder, productIdx: int):
    builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(productIdx), 0)

def AddProductIdx(builder: flatbuffers.Builder, productIdx: int):
    VibeAddProductIdx(builder, productIdx)

def VibeStartProductIdxVector(builder, numElems: int) -> int:
    return builder.StartVector(4, numElems, 4)

def StartProductIdxVector(builder, numElems: int) -> int:
    return VibeStartProductIdxVector(builder, numElems)

def VibeEnd(builder: flatbuffers.Builder) -> int:
    return builder.EndObject()

def End(builder: flatbuffers.Builder) -> int:
    return VibeEnd(builder)

try:
    from typing import List
except:
    pass

class VibeT(object):

    # VibeT
    def __init__(self):
        self.id = None  # type: str
        self.base64 = None  # type: str
        self.description = None  # type: str
        self.imageUrl = None  # type: str
        self.productIdx = None  # type: List[int]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        vibe = Vibe()
        vibe.Init(buf, pos)
        return cls.InitFromObj(vibe)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, vibe):
        x = VibeT()
        x._UnPack(vibe)
        return x

    # VibeT
    def _UnPack(self, vibe):
        if vibe is None:
            return
        self.id = vibe.Id()
        self.base64 = vibe.Base64()
        self.description = vibe.Description()
        self.imageUrl = vibe.ImageUrl()
        if not vibe.ProductIdxIsNone():
            if np is None:
                self.productIdx = []
                for i in range(vibe.ProductIdxLength()):
                    self.productIdx.append(vibe.ProductIdx(i))
            else:
                self.productIdx = vibe.ProductIdxAsNumpy()

    # VibeT
    def Pack(self, builder):
        if self.id is not None:
            id = builder.CreateString(self.id)
        if self.base64 is not None:
            base64 = builder.CreateString(self.base64)
        if self.description is not None:
            description = builder.CreateString(self.description)
        if self.imageUrl is not None:
            imageUrl = builder.CreateString(self.imageUrl)
        if self.productIdx is not None:
            if np is not None and type(self.productIdx) is np.ndarray:
                productIdx = builder.CreateNumpyVector(self.productIdx)
            else:
                VibeStartProductIdxVector(builder, len(self.productIdx))
                for i in reversed(range(len(self.productIdx))):
                    builder.PrependInt32(self.productIdx[i])
                productIdx = builder.EndVector()
        VibeStart(builder)
        if self.id is not None:
            VibeAddId(builder, id)
        if self.base64 is not None:
            VibeAddBase64(builder, base64)
        if self.description is not None:
            VibeAddDescription(builder, description)
        if self.imageUrl is not None:
            VibeAddImageUrl(builder, imageUrl)
        if self.productIdx is not None:
            VibeAddProductIdx(builder, productIdx)
        vibe = VibeEnd(builder)
        return vibe
