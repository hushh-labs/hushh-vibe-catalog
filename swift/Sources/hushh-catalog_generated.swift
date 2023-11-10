// automatically generated by the FlatBuffers compiler, do not modify
// swiftlint:disable all
// swiftformat:disable all

import FlatBuffers

public struct hushh_hcf_ProductCharacterization: FlatBufferObject, Verifiable, ObjectAPIPacker {

  static func validateVersion() { FlatBuffersVersion_23_5_26() }
  public var __buffer: ByteBuffer! { return _accessor.bb }
  private var _accessor: Table

  private init(_ t: Table) { _accessor = t }
  public init(_ bb: ByteBuffer, o: Int32) { _accessor = Table(bb: bb, position: o) }

  private enum VTOFFSET: VOffset {
    case id = 4
    case description = 6
    case url = 8
    case productIds = 10
    var v: Int32 { Int32(self.rawValue) }
    var p: VOffset { self.rawValue }
  }

  public var id: String? { let o = _accessor.offset(VTOFFSET.id.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var idSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.id.v) }
  public var description: String? { let o = _accessor.offset(VTOFFSET.description.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var descriptionSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.description.v) }
  public var url: String? { let o = _accessor.offset(VTOFFSET.url.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var urlSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.url.v) }
  public var hasProductIds: Bool { let o = _accessor.offset(VTOFFSET.productIds.v); return o == 0 ? false : true }
  public var productIdsCount: Int32 { let o = _accessor.offset(VTOFFSET.productIds.v); return o == 0 ? 0 : _accessor.vector(count: o) }
  public func productIds(at index: Int32) -> String? { let o = _accessor.offset(VTOFFSET.productIds.v); return o == 0 ? nil : _accessor.directString(at: _accessor.vector(at: o) + index * 4) }
  public static func startProductCharacterization(_ fbb: inout FlatBufferBuilder) -> UOffset { fbb.startTable(with: 4) }
  public static func add(id: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: id, at: VTOFFSET.id.p) }
  public static func add(description: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: description, at: VTOFFSET.description.p) }
  public static func add(url: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: url, at: VTOFFSET.url.p) }
  public static func addVectorOf(productIds: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: productIds, at: VTOFFSET.productIds.p) }
  public static func endProductCharacterization(_ fbb: inout FlatBufferBuilder, start: UOffset) -> Offset { let end = Offset(offset: fbb.endTable(at: start)); return end }
  public static func createProductCharacterization(
    _ fbb: inout FlatBufferBuilder,
    idOffset id: Offset = Offset(),
    descriptionOffset description: Offset = Offset(),
    urlOffset url: Offset = Offset(),
    productIdsVectorOffset productIds: Offset = Offset()
  ) -> Offset {
    let __start = hushh_hcf_ProductCharacterization.startProductCharacterization(&fbb)
    hushh_hcf_ProductCharacterization.add(id: id, &fbb)
    hushh_hcf_ProductCharacterization.add(description: description, &fbb)
    hushh_hcf_ProductCharacterization.add(url: url, &fbb)
    hushh_hcf_ProductCharacterization.addVectorOf(productIds: productIds, &fbb)
    return hushh_hcf_ProductCharacterization.endProductCharacterization(&fbb, start: __start)
  }
  

  public mutating func unpack() -> hushh_hcf_ProductCharacterizationT {
    return hushh_hcf_ProductCharacterizationT(&self)
  }
  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout hushh_hcf_ProductCharacterizationT?) -> Offset {
    guard var obj = obj else { return Offset() }
    return pack(&builder, obj: &obj)
  }

  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout hushh_hcf_ProductCharacterizationT) -> Offset {
    let __id: Offset
    if let s = obj.id {
      __id = builder.create(string: s)
    } else {
      __id = Offset()
    }

    let __description: Offset
    if let s = obj.description {
      __description = builder.create(string: s)
    } else {
      __description = Offset()
    }

    let __url: Offset
    if let s = obj.url {
      __url = builder.create(string: s)
    } else {
      __url = Offset()
    }

    let __productIds = builder.createVector(ofStrings: obj.productIds.compactMap({ $0 }) )
    let __root = hushh_hcf_ProductCharacterization.startProductCharacterization(&builder)
    hushh_hcf_ProductCharacterization.add(id: __id, &builder)
    hushh_hcf_ProductCharacterization.add(description: __description, &builder)
    hushh_hcf_ProductCharacterization.add(url: __url, &builder)
    hushh_hcf_ProductCharacterization.addVectorOf(productIds: __productIds, &builder)
    return hushh_hcf_ProductCharacterization.endProductCharacterization(&builder, start: __root)
  }

  public static func verify<T>(_ verifier: inout Verifier, at position: Int, of type: T.Type) throws where T: Verifiable {
    var _v = try verifier.visitTable(at: position)
    try _v.visit(field: VTOFFSET.id.p, fieldName: "id", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.description.p, fieldName: "description", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.url.p, fieldName: "url", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.productIds.p, fieldName: "productIds", required: false, type: ForwardOffset<Vector<ForwardOffset<String>, String>>.self)
    _v.finish()
  }
}

public class hushh_hcf_ProductCharacterizationT: NativeObject {

  public var id: String?
  public var description: String?
  public var url: String?
  public var productIds: [String?]

  public init(_ _t: inout hushh_hcf_ProductCharacterization) {
    id = _t.id
    description = _t.description
    url = _t.url
    productIds = []
    for index in 0..<_t.productIdsCount {
        productIds.append(_t.productIds(at: index))
    }
  }

  public init() {
    productIds = []
  }

  public func serialize() -> ByteBuffer { return serialize(type: hushh_hcf_ProductCharacterization.self) }

}
public struct hushh_hcf_Product: FlatBufferObject, Verifiable, ObjectAPIPacker {

  static func validateVersion() { FlatBuffersVersion_23_5_26() }
  public var __buffer: ByteBuffer! { return _accessor.bb }
  private var _accessor: Table

  private init(_ t: Table) { _accessor = t }
  public init(_ bb: ByteBuffer, o: Int32) { _accessor = Table(bb: bb, position: o) }

  private enum VTOFFSET: VOffset {
    case id = 4
    case description = 6
    case url = 8
    case characterizationIds = 10
    var v: Int32 { Int32(self.rawValue) }
    var p: VOffset { self.rawValue }
  }

  public var id: String? { let o = _accessor.offset(VTOFFSET.id.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var idSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.id.v) }
  public var description: String? { let o = _accessor.offset(VTOFFSET.description.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var descriptionSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.description.v) }
  public var url: String? { let o = _accessor.offset(VTOFFSET.url.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var urlSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.url.v) }
  public var hasCharacterizationIds: Bool { let o = _accessor.offset(VTOFFSET.characterizationIds.v); return o == 0 ? false : true }
  public var characterizationIdsCount: Int32 { let o = _accessor.offset(VTOFFSET.characterizationIds.v); return o == 0 ? 0 : _accessor.vector(count: o) }
  public func characterizationIds(at index: Int32) -> String? { let o = _accessor.offset(VTOFFSET.characterizationIds.v); return o == 0 ? nil : _accessor.directString(at: _accessor.vector(at: o) + index * 4) }
  public static func startProduct(_ fbb: inout FlatBufferBuilder) -> UOffset { fbb.startTable(with: 4) }
  public static func add(id: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: id, at: VTOFFSET.id.p) }
  public static func add(description: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: description, at: VTOFFSET.description.p) }
  public static func add(url: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: url, at: VTOFFSET.url.p) }
  public static func addVectorOf(characterizationIds: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: characterizationIds, at: VTOFFSET.characterizationIds.p) }
  public static func endProduct(_ fbb: inout FlatBufferBuilder, start: UOffset) -> Offset { let end = Offset(offset: fbb.endTable(at: start)); return end }
  public static func createProduct(
    _ fbb: inout FlatBufferBuilder,
    idOffset id: Offset = Offset(),
    descriptionOffset description: Offset = Offset(),
    urlOffset url: Offset = Offset(),
    characterizationIdsVectorOffset characterizationIds: Offset = Offset()
  ) -> Offset {
    let __start = hushh_hcf_Product.startProduct(&fbb)
    hushh_hcf_Product.add(id: id, &fbb)
    hushh_hcf_Product.add(description: description, &fbb)
    hushh_hcf_Product.add(url: url, &fbb)
    hushh_hcf_Product.addVectorOf(characterizationIds: characterizationIds, &fbb)
    return hushh_hcf_Product.endProduct(&fbb, start: __start)
  }
  

  public mutating func unpack() -> hushh_hcf_ProductT {
    return hushh_hcf_ProductT(&self)
  }
  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout hushh_hcf_ProductT?) -> Offset {
    guard var obj = obj else { return Offset() }
    return pack(&builder, obj: &obj)
  }

  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout hushh_hcf_ProductT) -> Offset {
    let __id: Offset
    if let s = obj.id {
      __id = builder.create(string: s)
    } else {
      __id = Offset()
    }

    let __description: Offset
    if let s = obj.description {
      __description = builder.create(string: s)
    } else {
      __description = Offset()
    }

    let __url: Offset
    if let s = obj.url {
      __url = builder.create(string: s)
    } else {
      __url = Offset()
    }

    let __characterizationIds = builder.createVector(ofStrings: obj.characterizationIds.compactMap({ $0 }) )
    let __root = hushh_hcf_Product.startProduct(&builder)
    hushh_hcf_Product.add(id: __id, &builder)
    hushh_hcf_Product.add(description: __description, &builder)
    hushh_hcf_Product.add(url: __url, &builder)
    hushh_hcf_Product.addVectorOf(characterizationIds: __characterizationIds, &builder)
    return hushh_hcf_Product.endProduct(&builder, start: __root)
  }

  public static func verify<T>(_ verifier: inout Verifier, at position: Int, of type: T.Type) throws where T: Verifiable {
    var _v = try verifier.visitTable(at: position)
    try _v.visit(field: VTOFFSET.id.p, fieldName: "id", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.description.p, fieldName: "description", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.url.p, fieldName: "url", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.characterizationIds.p, fieldName: "characterizationIds", required: false, type: ForwardOffset<Vector<ForwardOffset<String>, String>>.self)
    _v.finish()
  }
}

public class hushh_hcf_ProductT: NativeObject {

  public var id: String?
  public var description: String?
  public var url: String?
  public var characterizationIds: [String?]

  public init(_ _t: inout hushh_hcf_Product) {
    id = _t.id
    description = _t.description
    url = _t.url
    characterizationIds = []
    for index in 0..<_t.characterizationIdsCount {
        characterizationIds.append(_t.characterizationIds(at: index))
    }
  }

  public init() {
    characterizationIds = []
  }

  public func serialize() -> ByteBuffer { return serialize(type: hushh_hcf_Product.self) }

}
public struct hushh_hcf_Embedding: FlatBufferObject, Verifiable, ObjectAPIPacker {

  static func validateVersion() { FlatBuffersVersion_23_5_26() }
  public var __buffer: ByteBuffer! { return _accessor.bb }
  private var _accessor: Table

  private init(_ t: Table) { _accessor = t }
  public init(_ bb: ByteBuffer, o: Int32) { _accessor = Table(bb: bb, position: o) }

  private enum VTOFFSET: VOffset {
    case v = 4
    var v: Int32 { Int32(self.rawValue) }
    var p: VOffset { self.rawValue }
  }

  public var hasV: Bool { let o = _accessor.offset(VTOFFSET.v.v); return o == 0 ? false : true }
  public var vCount: Int32 { let o = _accessor.offset(VTOFFSET.v.v); return o == 0 ? 0 : _accessor.vector(count: o) }
  public func v(at index: Int32) -> Float32 { let o = _accessor.offset(VTOFFSET.v.v); return o == 0 ? 0 : _accessor.directRead(of: Float32.self, offset: _accessor.vector(at: o) + index * 4) }
  public var v: [Float32] { return _accessor.getVector(at: VTOFFSET.v.v) ?? [] }
  public static func startEmbedding(_ fbb: inout FlatBufferBuilder) -> UOffset { fbb.startTable(with: 1) }
  public static func addVectorOf(v: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: v, at: VTOFFSET.v.p) }
  public static func endEmbedding(_ fbb: inout FlatBufferBuilder, start: UOffset) -> Offset { let end = Offset(offset: fbb.endTable(at: start)); return end }
  public static func createEmbedding(
    _ fbb: inout FlatBufferBuilder,
    vVectorOffset v: Offset = Offset()
  ) -> Offset {
    let __start = hushh_hcf_Embedding.startEmbedding(&fbb)
    hushh_hcf_Embedding.addVectorOf(v: v, &fbb)
    return hushh_hcf_Embedding.endEmbedding(&fbb, start: __start)
  }
  

  public mutating func unpack() -> hushh_hcf_EmbeddingT {
    return hushh_hcf_EmbeddingT(&self)
  }
  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout hushh_hcf_EmbeddingT?) -> Offset {
    guard var obj = obj else { return Offset() }
    return pack(&builder, obj: &obj)
  }

  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout hushh_hcf_EmbeddingT) -> Offset {
    let __v = builder.createVector(obj.v)
    let __root = hushh_hcf_Embedding.startEmbedding(&builder)
    hushh_hcf_Embedding.addVectorOf(v: __v, &builder)
    return hushh_hcf_Embedding.endEmbedding(&builder, start: __root)
  }

  public static func verify<T>(_ verifier: inout Verifier, at position: Int, of type: T.Type) throws where T: Verifiable {
    var _v = try verifier.visitTable(at: position)
    try _v.visit(field: VTOFFSET.v.p, fieldName: "v", required: false, type: ForwardOffset<Vector<Float32, Float32>>.self)
    _v.finish()
  }
}

public class hushh_hcf_EmbeddingT: NativeObject {

  public var v: [Float32]

  public init(_ _t: inout hushh_hcf_Embedding) {
    v = []
    for index in 0..<_t.vCount {
        v.append(_t.v(at: index))
    }
  }

  public init() {
    v = []
  }

  public func serialize() -> ByteBuffer { return serialize(type: hushh_hcf_Embedding.self) }

}
public struct hushh_hcf_ProductInformation: FlatBufferObject, Verifiable, ObjectAPIPacker {

  static func validateVersion() { FlatBuffersVersion_23_5_26() }
  public var __buffer: ByteBuffer! { return _accessor.bb }
  private var _accessor: Table

  private init(_ t: Table) { _accessor = t }
  public init(_ bb: ByteBuffer, o: Int32) { _accessor = Table(bb: bb, position: o) }

  private enum VTOFFSET: VOffset {
    case id = 4
    case description = 6
    case imageBase64 = 8
    case url = 10
    var v: Int32 { Int32(self.rawValue) }
    var p: VOffset { self.rawValue }
  }

  public var id: String? { let o = _accessor.offset(VTOFFSET.id.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var idSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.id.v) }
  public var description: String? { let o = _accessor.offset(VTOFFSET.description.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var descriptionSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.description.v) }
  public var imageBase64: String? { let o = _accessor.offset(VTOFFSET.imageBase64.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var imageBase64SegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.imageBase64.v) }
  public var url: String? { let o = _accessor.offset(VTOFFSET.url.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var urlSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.url.v) }
  public static func startProductInformation(_ fbb: inout FlatBufferBuilder) -> UOffset { fbb.startTable(with: 4) }
  public static func add(id: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: id, at: VTOFFSET.id.p) }
  public static func add(description: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: description, at: VTOFFSET.description.p) }
  public static func add(imageBase64: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: imageBase64, at: VTOFFSET.imageBase64.p) }
  public static func add(url: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: url, at: VTOFFSET.url.p) }
  public static func endProductInformation(_ fbb: inout FlatBufferBuilder, start: UOffset) -> Offset { let end = Offset(offset: fbb.endTable(at: start)); return end }
  public static func createProductInformation(
    _ fbb: inout FlatBufferBuilder,
    idOffset id: Offset = Offset(),
    descriptionOffset description: Offset = Offset(),
    imageBase64Offset imageBase64: Offset = Offset(),
    urlOffset url: Offset = Offset()
  ) -> Offset {
    let __start = hushh_hcf_ProductInformation.startProductInformation(&fbb)
    hushh_hcf_ProductInformation.add(id: id, &fbb)
    hushh_hcf_ProductInformation.add(description: description, &fbb)
    hushh_hcf_ProductInformation.add(imageBase64: imageBase64, &fbb)
    hushh_hcf_ProductInformation.add(url: url, &fbb)
    return hushh_hcf_ProductInformation.endProductInformation(&fbb, start: __start)
  }
  

  public mutating func unpack() -> hushh_hcf_ProductInformationT {
    return hushh_hcf_ProductInformationT(&self)
  }
  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout hushh_hcf_ProductInformationT?) -> Offset {
    guard var obj = obj else { return Offset() }
    return pack(&builder, obj: &obj)
  }

  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout hushh_hcf_ProductInformationT) -> Offset {
    let __id: Offset
    if let s = obj.id {
      __id = builder.create(string: s)
    } else {
      __id = Offset()
    }

    let __description: Offset
    if let s = obj.description {
      __description = builder.create(string: s)
    } else {
      __description = Offset()
    }

    let __imageBase64: Offset
    if let s = obj.imageBase64 {
      __imageBase64 = builder.create(string: s)
    } else {
      __imageBase64 = Offset()
    }

    let __url: Offset
    if let s = obj.url {
      __url = builder.create(string: s)
    } else {
      __url = Offset()
    }

    let __root = hushh_hcf_ProductInformation.startProductInformation(&builder)
    hushh_hcf_ProductInformation.add(id: __id, &builder)
    hushh_hcf_ProductInformation.add(description: __description, &builder)
    hushh_hcf_ProductInformation.add(imageBase64: __imageBase64, &builder)
    hushh_hcf_ProductInformation.add(url: __url, &builder)
    return hushh_hcf_ProductInformation.endProductInformation(&builder, start: __root)
  }

  public static func verify<T>(_ verifier: inout Verifier, at position: Int, of type: T.Type) throws where T: Verifiable {
    var _v = try verifier.visitTable(at: position)
    try _v.visit(field: VTOFFSET.id.p, fieldName: "id", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.description.p, fieldName: "description", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.imageBase64.p, fieldName: "imageBase64", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.url.p, fieldName: "url", required: false, type: ForwardOffset<String>.self)
    _v.finish()
  }
}

public class hushh_hcf_ProductInformationT: NativeObject {

  public var id: String?
  public var description: String?
  public var imageBase64: String?
  public var url: String?

  public init(_ _t: inout hushh_hcf_ProductInformation) {
    id = _t.id
    description = _t.description
    imageBase64 = _t.imageBase64
    url = _t.url
  }

  public init() {
  }

  public func serialize() -> ByteBuffer { return serialize(type: hushh_hcf_ProductInformation.self) }

}
public struct hushh_hcf_CharacterizationEmbeddings: FlatBufferObject, Verifiable, ObjectAPIPacker {

  static func validateVersion() { FlatBuffersVersion_23_5_26() }
  public var __buffer: ByteBuffer! { return _accessor.bb }
  private var _accessor: Table

  private init(_ t: Table) { _accessor = t }
  public init(_ bb: ByteBuffer, o: Int32) { _accessor = Table(bb: bb, position: o) }

  private enum VTOFFSET: VOffset {
    case id = 4
    case description = 6
    case url = 8
    var v: Int32 { Int32(self.rawValue) }
    var p: VOffset { self.rawValue }
  }

  public var id: String? { let o = _accessor.offset(VTOFFSET.id.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var idSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.id.v) }
  public var description: String? { let o = _accessor.offset(VTOFFSET.description.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var descriptionSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.description.v) }
  public var url: String? { let o = _accessor.offset(VTOFFSET.url.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var urlSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.url.v) }
  public static func startCharacterizationEmbeddings(_ fbb: inout FlatBufferBuilder) -> UOffset { fbb.startTable(with: 3) }
  public static func add(id: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: id, at: VTOFFSET.id.p) }
  public static func add(description: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: description, at: VTOFFSET.description.p) }
  public static func add(url: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: url, at: VTOFFSET.url.p) }
  public static func endCharacterizationEmbeddings(_ fbb: inout FlatBufferBuilder, start: UOffset) -> Offset { let end = Offset(offset: fbb.endTable(at: start)); return end }
  public static func createCharacterizationEmbeddings(
    _ fbb: inout FlatBufferBuilder,
    idOffset id: Offset = Offset(),
    descriptionOffset description: Offset = Offset(),
    urlOffset url: Offset = Offset()
  ) -> Offset {
    let __start = hushh_hcf_CharacterizationEmbeddings.startCharacterizationEmbeddings(&fbb)
    hushh_hcf_CharacterizationEmbeddings.add(id: id, &fbb)
    hushh_hcf_CharacterizationEmbeddings.add(description: description, &fbb)
    hushh_hcf_CharacterizationEmbeddings.add(url: url, &fbb)
    return hushh_hcf_CharacterizationEmbeddings.endCharacterizationEmbeddings(&fbb, start: __start)
  }
  

  public mutating func unpack() -> hushh_hcf_CharacterizationEmbeddingsT {
    return hushh_hcf_CharacterizationEmbeddingsT(&self)
  }
  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout hushh_hcf_CharacterizationEmbeddingsT?) -> Offset {
    guard var obj = obj else { return Offset() }
    return pack(&builder, obj: &obj)
  }

  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout hushh_hcf_CharacterizationEmbeddingsT) -> Offset {
    let __id: Offset
    if let s = obj.id {
      __id = builder.create(string: s)
    } else {
      __id = Offset()
    }

    let __description: Offset
    if let s = obj.description {
      __description = builder.create(string: s)
    } else {
      __description = Offset()
    }

    let __url: Offset
    if let s = obj.url {
      __url = builder.create(string: s)
    } else {
      __url = Offset()
    }

    let __root = hushh_hcf_CharacterizationEmbeddings.startCharacterizationEmbeddings(&builder)
    hushh_hcf_CharacterizationEmbeddings.add(id: __id, &builder)
    hushh_hcf_CharacterizationEmbeddings.add(description: __description, &builder)
    hushh_hcf_CharacterizationEmbeddings.add(url: __url, &builder)
    return hushh_hcf_CharacterizationEmbeddings.endCharacterizationEmbeddings(&builder, start: __root)
  }

  public static func verify<T>(_ verifier: inout Verifier, at position: Int, of type: T.Type) throws where T: Verifiable {
    var _v = try verifier.visitTable(at: position)
    try _v.visit(field: VTOFFSET.id.p, fieldName: "id", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.description.p, fieldName: "description", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.url.p, fieldName: "url", required: false, type: ForwardOffset<String>.self)
    _v.finish()
  }
}

public class hushh_hcf_CharacterizationEmbeddingsT: NativeObject {

  public var id: String?
  public var description: String?
  public var url: String?

  public init(_ _t: inout hushh_hcf_CharacterizationEmbeddings) {
    id = _t.id
    description = _t.description
    url = _t.url
  }

  public init() {
  }

  public func serialize() -> ByteBuffer { return serialize(type: hushh_hcf_CharacterizationEmbeddings.self) }

}
public struct hushh_hcf_Catalog: FlatBufferObject, Verifiable, ObjectAPIPacker {

  static func validateVersion() { FlatBuffersVersion_23_5_26() }
  public var __buffer: ByteBuffer! { return _accessor.bb }
  private var _accessor: Table

  private init(_ t: Table) { _accessor = t }
  public init(_ bb: ByteBuffer, o: Int32) { _accessor = Table(bb: bb, position: o) }

  private enum VTOFFSET: VOffset {
    case id = 4
    case version = 6
    case head = 8
    case products = 10
    case productEmbeddings = 12
    case characterizations = 14
    case characterizationEmbeddings = 16
    case productInformation = 18
    var v: Int32 { Int32(self.rawValue) }
    var p: VOffset { self.rawValue }
  }

  public var id: String? { let o = _accessor.offset(VTOFFSET.id.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var idSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.id.v) }
  public var version: String? { let o = _accessor.offset(VTOFFSET.version.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var versionSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.version.v) }
  public var head: String? { let o = _accessor.offset(VTOFFSET.head.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var headSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.head.v) }
  public var hasProducts: Bool { let o = _accessor.offset(VTOFFSET.products.v); return o == 0 ? false : true }
  public var productsCount: Int32 { let o = _accessor.offset(VTOFFSET.products.v); return o == 0 ? 0 : _accessor.vector(count: o) }
  public func products(at index: Int32) -> hushh_hcf_Product? { let o = _accessor.offset(VTOFFSET.products.v); return o == 0 ? nil : hushh_hcf_Product(_accessor.bb, o: _accessor.indirect(_accessor.vector(at: o) + index * 4)) }
  public var hasProductEmbeddings: Bool { let o = _accessor.offset(VTOFFSET.productEmbeddings.v); return o == 0 ? false : true }
  public var productEmbeddingsCount: Int32 { let o = _accessor.offset(VTOFFSET.productEmbeddings.v); return o == 0 ? 0 : _accessor.vector(count: o) }
  public func productEmbeddings(at index: Int32) -> hushh_hcf_Embedding? { let o = _accessor.offset(VTOFFSET.productEmbeddings.v); return o == 0 ? nil : hushh_hcf_Embedding(_accessor.bb, o: _accessor.indirect(_accessor.vector(at: o) + index * 4)) }
  public var hasCharacterizations: Bool { let o = _accessor.offset(VTOFFSET.characterizations.v); return o == 0 ? false : true }
  public var characterizationsCount: Int32 { let o = _accessor.offset(VTOFFSET.characterizations.v); return o == 0 ? 0 : _accessor.vector(count: o) }
  public func characterizations(at index: Int32) -> hushh_hcf_ProductCharacterization? { let o = _accessor.offset(VTOFFSET.characterizations.v); return o == 0 ? nil : hushh_hcf_ProductCharacterization(_accessor.bb, o: _accessor.indirect(_accessor.vector(at: o) + index * 4)) }
  public var hasCharacterizationEmbeddings: Bool { let o = _accessor.offset(VTOFFSET.characterizationEmbeddings.v); return o == 0 ? false : true }
  public var characterizationEmbeddingsCount: Int32 { let o = _accessor.offset(VTOFFSET.characterizationEmbeddings.v); return o == 0 ? 0 : _accessor.vector(count: o) }
  public func characterizationEmbeddings(at index: Int32) -> hushh_hcf_Embedding? { let o = _accessor.offset(VTOFFSET.characterizationEmbeddings.v); return o == 0 ? nil : hushh_hcf_Embedding(_accessor.bb, o: _accessor.indirect(_accessor.vector(at: o) + index * 4)) }
  public var hasProductInformation: Bool { let o = _accessor.offset(VTOFFSET.productInformation.v); return o == 0 ? false : true }
  public var productInformationCount: Int32 { let o = _accessor.offset(VTOFFSET.productInformation.v); return o == 0 ? 0 : _accessor.vector(count: o) }
  public func productInformation(at index: Int32) -> hushh_hcf_ProductInformation? { let o = _accessor.offset(VTOFFSET.productInformation.v); return o == 0 ? nil : hushh_hcf_ProductInformation(_accessor.bb, o: _accessor.indirect(_accessor.vector(at: o) + index * 4)) }
  public static func startCatalog(_ fbb: inout FlatBufferBuilder) -> UOffset { fbb.startTable(with: 8) }
  public static func add(id: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: id, at: VTOFFSET.id.p) }
  public static func add(version: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: version, at: VTOFFSET.version.p) }
  public static func add(head: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: head, at: VTOFFSET.head.p) }
  public static func addVectorOf(products: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: products, at: VTOFFSET.products.p) }
  public static func addVectorOf(productEmbeddings: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: productEmbeddings, at: VTOFFSET.productEmbeddings.p) }
  public static func addVectorOf(characterizations: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: characterizations, at: VTOFFSET.characterizations.p) }
  public static func addVectorOf(characterizationEmbeddings: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: characterizationEmbeddings, at: VTOFFSET.characterizationEmbeddings.p) }
  public static func addVectorOf(productInformation: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: productInformation, at: VTOFFSET.productInformation.p) }
  public static func endCatalog(_ fbb: inout FlatBufferBuilder, start: UOffset) -> Offset { let end = Offset(offset: fbb.endTable(at: start)); return end }
  public static func createCatalog(
    _ fbb: inout FlatBufferBuilder,
    idOffset id: Offset = Offset(),
    versionOffset version: Offset = Offset(),
    headOffset head: Offset = Offset(),
    productsVectorOffset products: Offset = Offset(),
    productEmbeddingsVectorOffset productEmbeddings: Offset = Offset(),
    characterizationsVectorOffset characterizations: Offset = Offset(),
    characterizationEmbeddingsVectorOffset characterizationEmbeddings: Offset = Offset(),
    productInformationVectorOffset productInformation: Offset = Offset()
  ) -> Offset {
    let __start = hushh_hcf_Catalog.startCatalog(&fbb)
    hushh_hcf_Catalog.add(id: id, &fbb)
    hushh_hcf_Catalog.add(version: version, &fbb)
    hushh_hcf_Catalog.add(head: head, &fbb)
    hushh_hcf_Catalog.addVectorOf(products: products, &fbb)
    hushh_hcf_Catalog.addVectorOf(productEmbeddings: productEmbeddings, &fbb)
    hushh_hcf_Catalog.addVectorOf(characterizations: characterizations, &fbb)
    hushh_hcf_Catalog.addVectorOf(characterizationEmbeddings: characterizationEmbeddings, &fbb)
    hushh_hcf_Catalog.addVectorOf(productInformation: productInformation, &fbb)
    return hushh_hcf_Catalog.endCatalog(&fbb, start: __start)
  }
  

  public mutating func unpack() -> hushh_hcf_CatalogT {
    return hushh_hcf_CatalogT(&self)
  }
  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout hushh_hcf_CatalogT?) -> Offset {
    guard var obj = obj else { return Offset() }
    return pack(&builder, obj: &obj)
  }

  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout hushh_hcf_CatalogT) -> Offset {
    let __id: Offset
    if let s = obj.id {
      __id = builder.create(string: s)
    } else {
      __id = Offset()
    }

    let __version: Offset
    if let s = obj.version {
      __version = builder.create(string: s)
    } else {
      __version = Offset()
    }

    let __head: Offset
    if let s = obj.head {
      __head = builder.create(string: s)
    } else {
      __head = Offset()
    }

    var __products__: [Offset] = []
    for var i in obj.products {
      __products__.append(hushh_hcf_Product.pack(&builder, obj: &i))
    }
    let __products = builder.createVector(ofOffsets: __products__)
    var __productEmbeddings__: [Offset] = []
    for var i in obj.productEmbeddings {
      __productEmbeddings__.append(hushh_hcf_Embedding.pack(&builder, obj: &i))
    }
    let __productEmbeddings = builder.createVector(ofOffsets: __productEmbeddings__)
    var __characterizations__: [Offset] = []
    for var i in obj.characterizations {
      __characterizations__.append(hushh_hcf_ProductCharacterization.pack(&builder, obj: &i))
    }
    let __characterizations = builder.createVector(ofOffsets: __characterizations__)
    var __characterizationEmbeddings__: [Offset] = []
    for var i in obj.characterizationEmbeddings {
      __characterizationEmbeddings__.append(hushh_hcf_Embedding.pack(&builder, obj: &i))
    }
    let __characterizationEmbeddings = builder.createVector(ofOffsets: __characterizationEmbeddings__)
    var __productInformation__: [Offset] = []
    for var i in obj.productInformation {
      __productInformation__.append(hushh_hcf_ProductInformation.pack(&builder, obj: &i))
    }
    let __productInformation = builder.createVector(ofOffsets: __productInformation__)
    let __root = hushh_hcf_Catalog.startCatalog(&builder)
    hushh_hcf_Catalog.add(id: __id, &builder)
    hushh_hcf_Catalog.add(version: __version, &builder)
    hushh_hcf_Catalog.add(head: __head, &builder)
    hushh_hcf_Catalog.addVectorOf(products: __products, &builder)
    hushh_hcf_Catalog.addVectorOf(productEmbeddings: __productEmbeddings, &builder)
    hushh_hcf_Catalog.addVectorOf(characterizations: __characterizations, &builder)
    hushh_hcf_Catalog.addVectorOf(characterizationEmbeddings: __characterizationEmbeddings, &builder)
    hushh_hcf_Catalog.addVectorOf(productInformation: __productInformation, &builder)
    return hushh_hcf_Catalog.endCatalog(&builder, start: __root)
  }

  public static func verify<T>(_ verifier: inout Verifier, at position: Int, of type: T.Type) throws where T: Verifiable {
    var _v = try verifier.visitTable(at: position)
    try _v.visit(field: VTOFFSET.id.p, fieldName: "id", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.version.p, fieldName: "version", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.head.p, fieldName: "head", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.products.p, fieldName: "products", required: false, type: ForwardOffset<Vector<ForwardOffset<hushh_hcf_Product>, hushh_hcf_Product>>.self)
    try _v.visit(field: VTOFFSET.productEmbeddings.p, fieldName: "productEmbeddings", required: false, type: ForwardOffset<Vector<ForwardOffset<hushh_hcf_Embedding>, hushh_hcf_Embedding>>.self)
    try _v.visit(field: VTOFFSET.characterizations.p, fieldName: "characterizations", required: false, type: ForwardOffset<Vector<ForwardOffset<hushh_hcf_ProductCharacterization>, hushh_hcf_ProductCharacterization>>.self)
    try _v.visit(field: VTOFFSET.characterizationEmbeddings.p, fieldName: "characterizationEmbeddings", required: false, type: ForwardOffset<Vector<ForwardOffset<hushh_hcf_Embedding>, hushh_hcf_Embedding>>.self)
    try _v.visit(field: VTOFFSET.productInformation.p, fieldName: "productInformation", required: false, type: ForwardOffset<Vector<ForwardOffset<hushh_hcf_ProductInformation>, hushh_hcf_ProductInformation>>.self)
    _v.finish()
  }
}

public class hushh_hcf_CatalogT: NativeObject {

  public var id: String?
  public var version: String?
  public var head: String?
  public var products: [hushh_hcf_ProductT?]
  public var productEmbeddings: [hushh_hcf_EmbeddingT?]
  public var characterizations: [hushh_hcf_ProductCharacterizationT?]
  public var characterizationEmbeddings: [hushh_hcf_EmbeddingT?]
  public var productInformation: [hushh_hcf_ProductInformationT?]

  public init(_ _t: inout hushh_hcf_Catalog) {
    id = _t.id
    version = _t.version
    head = _t.head
    products = []
    for index in 0..<_t.productsCount {
        var __v_ = _t.products(at: index)
        products.append(__v_?.unpack())
    }
    productEmbeddings = []
    for index in 0..<_t.productEmbeddingsCount {
        var __v_ = _t.productEmbeddings(at: index)
        productEmbeddings.append(__v_?.unpack())
    }
    characterizations = []
    for index in 0..<_t.characterizationsCount {
        var __v_ = _t.characterizations(at: index)
        characterizations.append(__v_?.unpack())
    }
    characterizationEmbeddings = []
    for index in 0..<_t.characterizationEmbeddingsCount {
        var __v_ = _t.characterizationEmbeddings(at: index)
        characterizationEmbeddings.append(__v_?.unpack())
    }
    productInformation = []
    for index in 0..<_t.productInformationCount {
        var __v_ = _t.productInformation(at: index)
        productInformation.append(__v_?.unpack())
    }
  }

  public init() {
    products = []
    productEmbeddings = []
    characterizations = []
    characterizationEmbeddings = []
    productInformation = []
  }

  public func serialize() -> ByteBuffer { return serialize(type: hushh_hcf_Catalog.self) }

}
