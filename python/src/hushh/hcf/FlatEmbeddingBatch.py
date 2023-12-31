# automatically generated by the FlatBuffers compiler, do not modify

# namespace: hcf

import flatbuffers
from flatbuffers.compat import import_numpy
from typing import Any
from typing import Optional
np = import_numpy()

class FlatEmbeddingBatch(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset: int = 0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FlatEmbeddingBatch()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFlatEmbeddingBatch(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # FlatEmbeddingBatch
    def Init(self, buf: bytes, pos: int):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FlatEmbeddingBatch
    def Id(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # FlatEmbeddingBatch
    def Shape(self, j: int):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # FlatEmbeddingBatch
    def ShapeAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # FlatEmbeddingBatch
    def ShapeLength(self) -> int:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FlatEmbeddingBatch
    def ShapeIsNone(self) -> bool:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # FlatEmbeddingBatch
    def VibeMode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # FlatEmbeddingBatch
    def FlatTensor(self, j: int):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # FlatEmbeddingBatch
    def FlatTensorAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Float32Flags, o)
        return 0

    # FlatEmbeddingBatch
    def FlatTensorLength(self) -> int:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FlatEmbeddingBatch
    def FlatTensorIsNone(self) -> bool:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # FlatEmbeddingBatch
    def ProductIndex(self, j: int):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # FlatEmbeddingBatch
    def ProductIndexAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # FlatEmbeddingBatch
    def ProductIndexLength(self) -> int:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FlatEmbeddingBatch
    def ProductIndexIsNone(self) -> bool:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

def FlatEmbeddingBatchStart(builder: flatbuffers.Builder):
    builder.StartObject(5)

def Start(builder: flatbuffers.Builder):
    FlatEmbeddingBatchStart(builder)

def FlatEmbeddingBatchAddId(builder: flatbuffers.Builder, id: int):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)

def AddId(builder: flatbuffers.Builder, id: int):
    FlatEmbeddingBatchAddId(builder, id)

def FlatEmbeddingBatchAddShape(builder: flatbuffers.Builder, shape: int):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(shape), 0)

def AddShape(builder: flatbuffers.Builder, shape: int):
    FlatEmbeddingBatchAddShape(builder, shape)

def FlatEmbeddingBatchStartShapeVector(builder, numElems: int) -> int:
    return builder.StartVector(4, numElems, 4)

def StartShapeVector(builder, numElems: int) -> int:
    return FlatEmbeddingBatchStartShapeVector(builder, numElems)

def FlatEmbeddingBatchAddVibeMode(builder: flatbuffers.Builder, vibeMode: int):
    builder.PrependInt8Slot(2, vibeMode, 0)

def AddVibeMode(builder: flatbuffers.Builder, vibeMode: int):
    FlatEmbeddingBatchAddVibeMode(builder, vibeMode)

def FlatEmbeddingBatchAddFlatTensor(builder: flatbuffers.Builder, flatTensor: int):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(flatTensor), 0)

def AddFlatTensor(builder: flatbuffers.Builder, flatTensor: int):
    FlatEmbeddingBatchAddFlatTensor(builder, flatTensor)

def FlatEmbeddingBatchStartFlatTensorVector(builder, numElems: int) -> int:
    return builder.StartVector(4, numElems, 4)

def StartFlatTensorVector(builder, numElems: int) -> int:
    return FlatEmbeddingBatchStartFlatTensorVector(builder, numElems)

def FlatEmbeddingBatchAddProductIndex(builder: flatbuffers.Builder, productIndex: int):
    builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(productIndex), 0)

def AddProductIndex(builder: flatbuffers.Builder, productIndex: int):
    FlatEmbeddingBatchAddProductIndex(builder, productIndex)

def FlatEmbeddingBatchStartProductIndexVector(builder, numElems: int) -> int:
    return builder.StartVector(4, numElems, 4)

def StartProductIndexVector(builder, numElems: int) -> int:
    return FlatEmbeddingBatchStartProductIndexVector(builder, numElems)

def FlatEmbeddingBatchEnd(builder: flatbuffers.Builder) -> int:
    return builder.EndObject()

def End(builder: flatbuffers.Builder) -> int:
    return FlatEmbeddingBatchEnd(builder)

try:
    from typing import List
except:
    pass

class FlatEmbeddingBatchT(object):

    # FlatEmbeddingBatchT
    def __init__(self):
        self.id = None  # type: str
        self.shape = None  # type: List[int]
        self.vibeMode = 0  # type: int
        self.flatTensor = None  # type: List[float]
        self.productIndex = None  # type: List[int]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        flatEmbeddingBatch = FlatEmbeddingBatch()
        flatEmbeddingBatch.Init(buf, pos)
        return cls.InitFromObj(flatEmbeddingBatch)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, flatEmbeddingBatch):
        x = FlatEmbeddingBatchT()
        x._UnPack(flatEmbeddingBatch)
        return x

    # FlatEmbeddingBatchT
    def _UnPack(self, flatEmbeddingBatch):
        if flatEmbeddingBatch is None:
            return
        self.id = flatEmbeddingBatch.Id()
        if not flatEmbeddingBatch.ShapeIsNone():
            if np is None:
                self.shape = []
                for i in range(flatEmbeddingBatch.ShapeLength()):
                    self.shape.append(flatEmbeddingBatch.Shape(i))
            else:
                self.shape = flatEmbeddingBatch.ShapeAsNumpy()
        self.vibeMode = flatEmbeddingBatch.VibeMode()
        if not flatEmbeddingBatch.FlatTensorIsNone():
            if np is None:
                self.flatTensor = []
                for i in range(flatEmbeddingBatch.FlatTensorLength()):
                    self.flatTensor.append(flatEmbeddingBatch.FlatTensor(i))
            else:
                self.flatTensor = flatEmbeddingBatch.FlatTensorAsNumpy()
        if not flatEmbeddingBatch.ProductIndexIsNone():
            if np is None:
                self.productIndex = []
                for i in range(flatEmbeddingBatch.ProductIndexLength()):
                    self.productIndex.append(flatEmbeddingBatch.ProductIndex(i))
            else:
                self.productIndex = flatEmbeddingBatch.ProductIndexAsNumpy()

    # FlatEmbeddingBatchT
    def Pack(self, builder):
        if self.id is not None:
            id = builder.CreateString(self.id)
        if self.shape is not None:
            if np is not None and type(self.shape) is np.ndarray:
                shape = builder.CreateNumpyVector(self.shape)
            else:
                FlatEmbeddingBatchStartShapeVector(builder, len(self.shape))
                for i in reversed(range(len(self.shape))):
                    builder.PrependInt32(self.shape[i])
                shape = builder.EndVector()
        if self.flatTensor is not None:
            if np is not None and type(self.flatTensor) is np.ndarray:
                flatTensor = builder.CreateNumpyVector(self.flatTensor)
            else:
                FlatEmbeddingBatchStartFlatTensorVector(builder, len(self.flatTensor))
                for i in reversed(range(len(self.flatTensor))):
                    builder.PrependFloat32(self.flatTensor[i])
                flatTensor = builder.EndVector()
        if self.productIndex is not None:
            if np is not None and type(self.productIndex) is np.ndarray:
                productIndex = builder.CreateNumpyVector(self.productIndex)
            else:
                FlatEmbeddingBatchStartProductIndexVector(builder, len(self.productIndex))
                for i in reversed(range(len(self.productIndex))):
                    builder.PrependInt32(self.productIndex[i])
                productIndex = builder.EndVector()
        FlatEmbeddingBatchStart(builder)
        if self.id is not None:
            FlatEmbeddingBatchAddId(builder, id)
        if self.shape is not None:
            FlatEmbeddingBatchAddShape(builder, shape)
        FlatEmbeddingBatchAddVibeMode(builder, self.vibeMode)
        if self.flatTensor is not None:
            FlatEmbeddingBatchAddFlatTensor(builder, flatTensor)
        if self.productIndex is not None:
            FlatEmbeddingBatchAddProductIndex(builder, productIndex)
        flatEmbeddingBatch = FlatEmbeddingBatchEnd(builder)
        return flatEmbeddingBatch
