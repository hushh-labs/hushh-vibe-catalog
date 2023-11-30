# automatically generated by the FlatBuffers compiler, do not modify

# namespace: hcf

from typing import Any, Optional

import flatbuffers
from flatbuffers.compat import import_numpy

from hushh.hcf.Category import Category
from hushh.hcf.FlatEmbeddingBatch import FlatEmbeddingBatch
from hushh.hcf.Product import Product
from hushh.hcf.Vibe import Vibe

np = import_numpy()


class ProductVibes(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAs(cls, buf, offset: int = 0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ProductVibes()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsProductVibes(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    # ProductVibes
    def Init(self, buf: bytes, pos: int):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ProductVibes
    def Id(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ProductVibes
    def Products(self, j: int) -> Optional[Product]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = Product()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ProductVibes
    def ProductsLength(self) -> int:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ProductVibes
    def ProductsIsNone(self) -> bool:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # ProductVibes
    def Categories(self, j: int) -> Optional[Category]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = Category()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ProductVibes
    def CategoriesLength(self) -> int:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ProductVibes
    def CategoriesIsNone(self) -> bool:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # ProductVibes
    def Vibes(self, j: int) -> Optional[Vibe]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = Vibe()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ProductVibes
    def VibesLength(self) -> int:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ProductVibes
    def VibesIsNone(self) -> bool:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # ProductVibes
    def FlatBatches(self, j: int) -> Optional[FlatEmbeddingBatch]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = FlatEmbeddingBatch()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ProductVibes
    def FlatBatchesLength(self) -> int:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ProductVibes
    def FlatBatchesIsNone(self) -> bool:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0


def ProductVibesStart(builder: flatbuffers.Builder):
    builder.StartObject(5)


def Start(builder: flatbuffers.Builder):
    ProductVibesStart(builder)


def ProductVibesAddId(builder: flatbuffers.Builder, id: int):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(id), 0
    )


def AddId(builder: flatbuffers.Builder, id: int):
    ProductVibesAddId(builder, id)


def ProductVibesAddProducts(builder: flatbuffers.Builder, products: int):
    builder.PrependUOffsetTRelativeSlot(
        1, flatbuffers.number_types.UOffsetTFlags.py_type(products), 0
    )


def AddProducts(builder: flatbuffers.Builder, products: int):
    ProductVibesAddProducts(builder, products)


def ProductVibesStartProductsVector(builder, numElems: int) -> int:
    return builder.StartVector(4, numElems, 4)


def StartProductsVector(builder, numElems: int) -> int:
    return ProductVibesStartProductsVector(builder, numElems)


def ProductVibesAddCategories(builder: flatbuffers.Builder, categories: int):
    builder.PrependUOffsetTRelativeSlot(
        2, flatbuffers.number_types.UOffsetTFlags.py_type(categories), 0
    )


def AddCategories(builder: flatbuffers.Builder, categories: int):
    ProductVibesAddCategories(builder, categories)


def ProductVibesStartCategoriesVector(builder, numElems: int) -> int:
    return builder.StartVector(4, numElems, 4)


def StartCategoriesVector(builder, numElems: int) -> int:
    return ProductVibesStartCategoriesVector(builder, numElems)


def ProductVibesAddVibes(builder: flatbuffers.Builder, vibes: int):
    builder.PrependUOffsetTRelativeSlot(
        3, flatbuffers.number_types.UOffsetTFlags.py_type(vibes), 0
    )


def AddVibes(builder: flatbuffers.Builder, vibes: int):
    ProductVibesAddVibes(builder, vibes)


def ProductVibesStartVibesVector(builder, numElems: int) -> int:
    return builder.StartVector(4, numElems, 4)


def StartVibesVector(builder, numElems: int) -> int:
    return ProductVibesStartVibesVector(builder, numElems)


def ProductVibesAddFlatBatches(builder: flatbuffers.Builder, flatBatches: int):
    builder.PrependUOffsetTRelativeSlot(
        4, flatbuffers.number_types.UOffsetTFlags.py_type(flatBatches), 0
    )


def AddFlatBatches(builder: flatbuffers.Builder, flatBatches: int):
    ProductVibesAddFlatBatches(builder, flatBatches)


def ProductVibesStartFlatBatchesVector(builder, numElems: int) -> int:
    return builder.StartVector(4, numElems, 4)


def StartFlatBatchesVector(builder, numElems: int) -> int:
    return ProductVibesStartFlatBatchesVector(builder, numElems)


def ProductVibesEnd(builder: flatbuffers.Builder) -> int:
    return builder.EndObject()


def End(builder: flatbuffers.Builder) -> int:
    return ProductVibesEnd(builder)


import hushh.hcf.Category
import hushh.hcf.FlatEmbeddingBatch
import hushh.hcf.Product
import hushh.hcf.Vibe

try:
    from typing import List
except:
    pass


class ProductVibesT(object):
    # ProductVibesT
    def __init__(self):
        self.id = None  # type: str
        self.products = None  # type: List[hushh.hcf.Product.ProductT]
        self.categories = None  # type: List[hushh.hcf.Category.CategoryT]
        self.vibes = None  # type: List[hushh.hcf.Vibe.VibeT]
        self.flatBatches = (
            None
        )  # type: List[hushh.hcf.FlatEmbeddingBatch.FlatEmbeddingBatchT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        productVibes = ProductVibes()
        productVibes.Init(buf, pos)
        return cls.InitFromObj(productVibes)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos + n)

    @classmethod
    def InitFromObj(cls, productVibes):
        x = ProductVibesT()
        x._UnPack(productVibes)
        return x

    # ProductVibesT
    def _UnPack(self, productVibes):
        if productVibes is None:
            return
        self.id = productVibes.Id()
        if not productVibes.ProductsIsNone():
            self.products = []
            for i in range(productVibes.ProductsLength()):
                if productVibes.Products(i) is None:
                    self.products.append(None)
                else:
                    product_ = hushh.hcf.Product.ProductT.InitFromObj(
                        productVibes.Products(i)
                    )
                    self.products.append(product_)
        if not productVibes.CategoriesIsNone():
            self.categories = []
            for i in range(productVibes.CategoriesLength()):
                if productVibes.Categories(i) is None:
                    self.categories.append(None)
                else:
                    category_ = hushh.hcf.Category.CategoryT.InitFromObj(
                        productVibes.Categories(i)
                    )
                    self.categories.append(category_)
        if not productVibes.VibesIsNone():
            self.vibes = []
            for i in range(productVibes.VibesLength()):
                if productVibes.Vibes(i) is None:
                    self.vibes.append(None)
                else:
                    vibe_ = hushh.hcf.Vibe.VibeT.InitFromObj(productVibes.Vibes(i))
                    self.vibes.append(vibe_)
        if not productVibes.FlatBatchesIsNone():
            self.flatBatches = []
            for i in range(productVibes.FlatBatchesLength()):
                if productVibes.FlatBatches(i) is None:
                    self.flatBatches.append(None)
                else:
                    flatEmbeddingBatch_ = (
                        hushh.hcf.FlatEmbeddingBatch.FlatEmbeddingBatchT.InitFromObj(
                            productVibes.FlatBatches(i)
                        )
                    )
                    self.flatBatches.append(flatEmbeddingBatch_)

    # ProductVibesT
    def Pack(self, builder):
        if self.id is not None:
            id = builder.CreateString(self.id)
        if self.products is not None:
            productslist = []
            for i in range(len(self.products)):
                productslist.append(self.products[i].Pack(builder))
            ProductVibesStartProductsVector(builder, len(self.products))
            for i in reversed(range(len(self.products))):
                builder.PrependUOffsetTRelative(productslist[i])
            products = builder.EndVector()
        if self.categories is not None:
            categorieslist = []
            for i in range(len(self.categories)):
                categorieslist.append(self.categories[i].Pack(builder))
            ProductVibesStartCategoriesVector(builder, len(self.categories))
            for i in reversed(range(len(self.categories))):
                builder.PrependUOffsetTRelative(categorieslist[i])
            categories = builder.EndVector()
        if self.vibes is not None:
            vibeslist = []
            for i in range(len(self.vibes)):
                vibeslist.append(self.vibes[i].Pack(builder))
            ProductVibesStartVibesVector(builder, len(self.vibes))
            for i in reversed(range(len(self.vibes))):
                builder.PrependUOffsetTRelative(vibeslist[i])
            vibes = builder.EndVector()
        if self.flatBatches is not None:
            flatBatcheslist = []
            for i in range(len(self.flatBatches)):
                flatBatcheslist.append(self.flatBatches[i].Pack(builder))
            ProductVibesStartFlatBatchesVector(builder, len(self.flatBatches))
            for i in reversed(range(len(self.flatBatches))):
                builder.PrependUOffsetTRelative(flatBatcheslist[i])
            flatBatches = builder.EndVector()
        ProductVibesStart(builder)
        if self.id is not None:
            ProductVibesAddId(builder, id)
        if self.products is not None:
            ProductVibesAddProducts(builder, products)
        if self.categories is not None:
            ProductVibesAddCategories(builder, categories)
        if self.vibes is not None:
            ProductVibesAddVibes(builder, vibes)
        if self.flatBatches is not None:
            ProductVibesAddFlatBatches(builder, flatBatches)
        productVibes = ProductVibesEnd(builder)
        return productVibes
