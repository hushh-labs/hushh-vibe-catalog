# automatically generated by the FlatBuffers compiler, do not modify

# namespace: hcf

import flatbuffers
from flatbuffers.compat import import_numpy
from typing import Any
from hushh.hcf.Embedding import Embedding
from hushh.hcf.Product import Product
from hushh.hcf.ProductCharacterization import ProductCharacterization
from hushh.hcf.ProductMetadata import ProductMetadata
from typing import Optional
np = import_numpy()

class Catalog(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset: int = 0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Catalog()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCatalog(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Catalog
    def Init(self, buf: bytes, pos: int):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Catalog
    def Id(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Catalog
    def Version(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Catalog
    def Products(self, j: int) -> Optional[Product]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = Product()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Catalog
    def ProductsLength(self) -> int:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Catalog
    def ProductsIsNone(self) -> bool:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # Catalog
    def ProductMetadata(self, j: int) -> Optional[ProductMetadata]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = ProductMetadata()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Catalog
    def ProductMetadataLength(self) -> int:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Catalog
    def ProductMetadataIsNone(self) -> bool:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # Catalog
    def ProductEmbeddings(self, j: int) -> Optional[Embedding]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = Embedding()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Catalog
    def ProductEmbeddingsLength(self) -> int:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Catalog
    def ProductEmbeddingsIsNone(self) -> bool:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # Catalog
    def Characterizations(self, j: int) -> Optional[ProductCharacterization]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = ProductCharacterization()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Catalog
    def CharacterizationsLength(self) -> int:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Catalog
    def CharacterizationsIsNone(self) -> bool:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # Catalog
    def CharacterizationEmbeddings(self, j: int) -> Optional[Embedding]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = Embedding()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Catalog
    def CharacterizationEmbeddingsLength(self) -> int:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Catalog
    def CharacterizationEmbeddingsIsNone(self) -> bool:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        return o == 0

def CatalogStart(builder: flatbuffers.Builder):
    builder.StartObject(7)

def Start(builder: flatbuffers.Builder):
    CatalogStart(builder)

def CatalogAddId(builder: flatbuffers.Builder, id: int):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)

def AddId(builder: flatbuffers.Builder, id: int):
    CatalogAddId(builder, id)

def CatalogAddVersion(builder: flatbuffers.Builder, version: int):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(version), 0)

def AddVersion(builder: flatbuffers.Builder, version: int):
    CatalogAddVersion(builder, version)

def CatalogAddProducts(builder: flatbuffers.Builder, products: int):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(products), 0)

def AddProducts(builder: flatbuffers.Builder, products: int):
    CatalogAddProducts(builder, products)

def CatalogStartProductsVector(builder, numElems: int) -> int:
    return builder.StartVector(4, numElems, 4)

def StartProductsVector(builder, numElems: int) -> int:
    return CatalogStartProductsVector(builder, numElems)

def CatalogAddProductMetadata(builder: flatbuffers.Builder, productMetadata: int):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(productMetadata), 0)

def AddProductMetadata(builder: flatbuffers.Builder, productMetadata: int):
    CatalogAddProductMetadata(builder, productMetadata)

def CatalogStartProductMetadataVector(builder, numElems: int) -> int:
    return builder.StartVector(4, numElems, 4)

def StartProductMetadataVector(builder, numElems: int) -> int:
    return CatalogStartProductMetadataVector(builder, numElems)

def CatalogAddProductEmbeddings(builder: flatbuffers.Builder, productEmbeddings: int):
    builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(productEmbeddings), 0)

def AddProductEmbeddings(builder: flatbuffers.Builder, productEmbeddings: int):
    CatalogAddProductEmbeddings(builder, productEmbeddings)

def CatalogStartProductEmbeddingsVector(builder, numElems: int) -> int:
    return builder.StartVector(4, numElems, 4)

def StartProductEmbeddingsVector(builder, numElems: int) -> int:
    return CatalogStartProductEmbeddingsVector(builder, numElems)

def CatalogAddCharacterizations(builder: flatbuffers.Builder, characterizations: int):
    builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(characterizations), 0)

def AddCharacterizations(builder: flatbuffers.Builder, characterizations: int):
    CatalogAddCharacterizations(builder, characterizations)

def CatalogStartCharacterizationsVector(builder, numElems: int) -> int:
    return builder.StartVector(4, numElems, 4)

def StartCharacterizationsVector(builder, numElems: int) -> int:
    return CatalogStartCharacterizationsVector(builder, numElems)

def CatalogAddCharacterizationEmbeddings(builder: flatbuffers.Builder, characterizationEmbeddings: int):
    builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(characterizationEmbeddings), 0)

def AddCharacterizationEmbeddings(builder: flatbuffers.Builder, characterizationEmbeddings: int):
    CatalogAddCharacterizationEmbeddings(builder, characterizationEmbeddings)

def CatalogStartCharacterizationEmbeddingsVector(builder, numElems: int) -> int:
    return builder.StartVector(4, numElems, 4)

def StartCharacterizationEmbeddingsVector(builder, numElems: int) -> int:
    return CatalogStartCharacterizationEmbeddingsVector(builder, numElems)

def CatalogEnd(builder: flatbuffers.Builder) -> int:
    return builder.EndObject()

def End(builder: flatbuffers.Builder) -> int:
    return CatalogEnd(builder)

import hushh.hcf.Embedding
import hushh.hcf.Product
import hushh.hcf.ProductCharacterization
import hushh.hcf.ProductMetadata
try:
    from typing import List
except:
    pass

class CatalogT(object):

    # CatalogT
    def __init__(self):
        self.id = None  # type: str
        self.version = None  # type: str
        self.products = None  # type: List[hushh.hcf.Product.ProductT]
        self.productMetadata = None  # type: List[hushh.hcf.ProductMetadata.ProductMetadataT]
        self.productEmbeddings = None  # type: List[hushh.hcf.Embedding.EmbeddingT]
        self.characterizations = None  # type: List[hushh.hcf.ProductCharacterization.ProductCharacterizationT]
        self.characterizationEmbeddings = None  # type: List[hushh.hcf.Embedding.EmbeddingT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        catalog = Catalog()
        catalog.Init(buf, pos)
        return cls.InitFromObj(catalog)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, catalog):
        x = CatalogT()
        x._UnPack(catalog)
        return x

    # CatalogT
    def _UnPack(self, catalog):
        if catalog is None:
            return
        self.id = catalog.Id()
        self.version = catalog.Version()
        if not catalog.ProductsIsNone():
            self.products = []
            for i in range(catalog.ProductsLength()):
                if catalog.Products(i) is None:
                    self.products.append(None)
                else:
                    product_ = hushh.hcf.Product.ProductT.InitFromObj(catalog.Products(i))
                    self.products.append(product_)
        if not catalog.ProductMetadataIsNone():
            self.productMetadata = []
            for i in range(catalog.ProductMetadataLength()):
                if catalog.ProductMetadata(i) is None:
                    self.productMetadata.append(None)
                else:
                    productMetadata_ = hushh.hcf.ProductMetadata.ProductMetadataT.InitFromObj(catalog.ProductMetadata(i))
                    self.productMetadata.append(productMetadata_)
        if not catalog.ProductEmbeddingsIsNone():
            self.productEmbeddings = []
            for i in range(catalog.ProductEmbeddingsLength()):
                if catalog.ProductEmbeddings(i) is None:
                    self.productEmbeddings.append(None)
                else:
                    embedding_ = hushh.hcf.Embedding.EmbeddingT.InitFromObj(catalog.ProductEmbeddings(i))
                    self.productEmbeddings.append(embedding_)
        if not catalog.CharacterizationsIsNone():
            self.characterizations = []
            for i in range(catalog.CharacterizationsLength()):
                if catalog.Characterizations(i) is None:
                    self.characterizations.append(None)
                else:
                    productCharacterization_ = hushh.hcf.ProductCharacterization.ProductCharacterizationT.InitFromObj(catalog.Characterizations(i))
                    self.characterizations.append(productCharacterization_)
        if not catalog.CharacterizationEmbeddingsIsNone():
            self.characterizationEmbeddings = []
            for i in range(catalog.CharacterizationEmbeddingsLength()):
                if catalog.CharacterizationEmbeddings(i) is None:
                    self.characterizationEmbeddings.append(None)
                else:
                    embedding_ = hushh.hcf.Embedding.EmbeddingT.InitFromObj(catalog.CharacterizationEmbeddings(i))
                    self.characterizationEmbeddings.append(embedding_)

    # CatalogT
    def Pack(self, builder):
        if self.id is not None:
            id = builder.CreateString(self.id)
        if self.version is not None:
            version = builder.CreateString(self.version)
        if self.products is not None:
            productslist = []
            for i in range(len(self.products)):
                productslist.append(self.products[i].Pack(builder))
            CatalogStartProductsVector(builder, len(self.products))
            for i in reversed(range(len(self.products))):
                builder.PrependUOffsetTRelative(productslist[i])
            products = builder.EndVector()
        if self.productMetadata is not None:
            productMetadatalist = []
            for i in range(len(self.productMetadata)):
                productMetadatalist.append(self.productMetadata[i].Pack(builder))
            CatalogStartProductMetadataVector(builder, len(self.productMetadata))
            for i in reversed(range(len(self.productMetadata))):
                builder.PrependUOffsetTRelative(productMetadatalist[i])
            productMetadata = builder.EndVector()
        if self.productEmbeddings is not None:
            productEmbeddingslist = []
            for i in range(len(self.productEmbeddings)):
                productEmbeddingslist.append(self.productEmbeddings[i].Pack(builder))
            CatalogStartProductEmbeddingsVector(builder, len(self.productEmbeddings))
            for i in reversed(range(len(self.productEmbeddings))):
                builder.PrependUOffsetTRelative(productEmbeddingslist[i])
            productEmbeddings = builder.EndVector()
        if self.characterizations is not None:
            characterizationslist = []
            for i in range(len(self.characterizations)):
                characterizationslist.append(self.characterizations[i].Pack(builder))
            CatalogStartCharacterizationsVector(builder, len(self.characterizations))
            for i in reversed(range(len(self.characterizations))):
                builder.PrependUOffsetTRelative(characterizationslist[i])
            characterizations = builder.EndVector()
        if self.characterizationEmbeddings is not None:
            characterizationEmbeddingslist = []
            for i in range(len(self.characterizationEmbeddings)):
                characterizationEmbeddingslist.append(self.characterizationEmbeddings[i].Pack(builder))
            CatalogStartCharacterizationEmbeddingsVector(builder, len(self.characterizationEmbeddings))
            for i in reversed(range(len(self.characterizationEmbeddings))):
                builder.PrependUOffsetTRelative(characterizationEmbeddingslist[i])
            characterizationEmbeddings = builder.EndVector()
        CatalogStart(builder)
        if self.id is not None:
            CatalogAddId(builder, id)
        if self.version is not None:
            CatalogAddVersion(builder, version)
        if self.products is not None:
            CatalogAddProducts(builder, products)
        if self.productMetadata is not None:
            CatalogAddProductMetadata(builder, productMetadata)
        if self.productEmbeddings is not None:
            CatalogAddProductEmbeddings(builder, productEmbeddings)
        if self.characterizations is not None:
            CatalogAddCharacterizations(builder, characterizations)
        if self.characterizationEmbeddings is not None:
            CatalogAddCharacterizationEmbeddings(builder, characterizationEmbeddings)
        catalog = CatalogEnd(builder)
        return catalog