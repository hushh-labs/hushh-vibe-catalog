// automatically generated by the FlatBuffers compiler, do not modify
// swiftlint:disable all
// swiftformat:disable all

import FlatBuffers

public struct hushh_hcf_CompositionMetadata: FlatBufferObject, Verifiable, ObjectAPIPacker {

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
  public static func startCompositionMetadata(_ fbb: inout FlatBufferBuilder) -> UOffset { fbb.startTable(with: 4) }
  public static func add(id: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: id, at: VTOFFSET.id.p) }
  public static func add(description: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: description, at: VTOFFSET.description.p) }
  public static func add(url: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: url, at: VTOFFSET.url.p) }
  public static func addVectorOf(productIds: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: productIds, at: VTOFFSET.productIds.p) }
  public static func endCompositionMetadata(_ fbb: inout FlatBufferBuilder, start: UOffset) -> Offset { let end = Offset(offset: fbb.endTable(at: start)); return end }
  public static func createCompositionMetadata(
    _ fbb: inout FlatBufferBuilder,
    idOffset id: Offset = Offset(),
    descriptionOffset description: Offset = Offset(),
    urlOffset url: Offset = Offset(),
    productIdsVectorOffset productIds: Offset = Offset()
  ) -> Offset {
    let __start = hushh_hcf_CompositionMetadata.startCompositionMetadata(&fbb)
    hushh_hcf_CompositionMetadata.add(id: id, &fbb)
    hushh_hcf_CompositionMetadata.add(description: description, &fbb)
    hushh_hcf_CompositionMetadata.add(url: url, &fbb)
    hushh_hcf_CompositionMetadata.addVectorOf(productIds: productIds, &fbb)
    return hushh_hcf_CompositionMetadata.endCompositionMetadata(&fbb, start: __start)
  }
  

  public mutating func unpack() -> hushh_hcf_CompositionMetadataT {
    return hushh_hcf_CompositionMetadataT(&self)
  }
  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout hushh_hcf_CompositionMetadataT?) -> Offset {
    guard var obj = obj else { return Offset() }
    return pack(&builder, obj: &obj)
  }

  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout hushh_hcf_CompositionMetadataT) -> Offset {
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
    let __root = hushh_hcf_CompositionMetadata.startCompositionMetadata(&builder)
    hushh_hcf_CompositionMetadata.add(id: __id, &builder)
    hushh_hcf_CompositionMetadata.add(description: __description, &builder)
    hushh_hcf_CompositionMetadata.add(url: __url, &builder)
    hushh_hcf_CompositionMetadata.addVectorOf(productIds: __productIds, &builder)
    return hushh_hcf_CompositionMetadata.endCompositionMetadata(&builder, start: __root)
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

extension hushh_hcf_CompositionMetadata: Encodable {

  enum CodingKeys: String, CodingKey {
    case id = "id"
    case description = "description"
    case url = "url"
    case productIds = "product_ids"
  }
  public func encode(to encoder: Encoder) throws {
    var container = encoder.container(keyedBy: CodingKeys.self)
    try container.encodeIfPresent(id, forKey: .id)
    try container.encodeIfPresent(description, forKey: .description)
    try container.encodeIfPresent(url, forKey: .url)
    if productIdsCount > 0 {
      var contentEncoder = container.nestedUnkeyedContainer(forKey: .productIds)
      for index in 0..<productIdsCount {
        guard let type = productIds(at: index) else { continue }
        try contentEncoder.encode(type)
      }
    }
  }
}

public class hushh_hcf_CompositionMetadataT: NativeObject {

  public var id: String?
  public var description: String?
  public var url: String?
  public var productIds: [String?]

  public init(_ _t: inout hushh_hcf_CompositionMetadata) {
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

  public func serialize() -> ByteBuffer { return serialize(type: hushh_hcf_CompositionMetadata.self) }

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
    var v: Int32 { Int32(self.rawValue) }
    var p: VOffset { self.rawValue }
  }

  public var id: String? { let o = _accessor.offset(VTOFFSET.id.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var idSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.id.v) }
  public var description: String? { let o = _accessor.offset(VTOFFSET.description.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var descriptionSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.description.v) }
  public var url: String? { let o = _accessor.offset(VTOFFSET.url.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var urlSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.url.v) }
  public static func startProduct(_ fbb: inout FlatBufferBuilder) -> UOffset { fbb.startTable(with: 3) }
  public static func add(id: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: id, at: VTOFFSET.id.p) }
  public static func add(description: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: description, at: VTOFFSET.description.p) }
  public static func add(url: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: url, at: VTOFFSET.url.p) }
  public static func endProduct(_ fbb: inout FlatBufferBuilder, start: UOffset) -> Offset { let end = Offset(offset: fbb.endTable(at: start)); return end }
  public static func createProduct(
    _ fbb: inout FlatBufferBuilder,
    idOffset id: Offset = Offset(),
    descriptionOffset description: Offset = Offset(),
    urlOffset url: Offset = Offset()
  ) -> Offset {
    let __start = hushh_hcf_Product.startProduct(&fbb)
    hushh_hcf_Product.add(id: id, &fbb)
    hushh_hcf_Product.add(description: description, &fbb)
    hushh_hcf_Product.add(url: url, &fbb)
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

    let __root = hushh_hcf_Product.startProduct(&builder)
    hushh_hcf_Product.add(id: __id, &builder)
    hushh_hcf_Product.add(description: __description, &builder)
    hushh_hcf_Product.add(url: __url, &builder)
    return hushh_hcf_Product.endProduct(&builder, start: __root)
  }

  public static func verify<T>(_ verifier: inout Verifier, at position: Int, of type: T.Type) throws where T: Verifiable {
    var _v = try verifier.visitTable(at: position)
    try _v.visit(field: VTOFFSET.id.p, fieldName: "id", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.description.p, fieldName: "description", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.url.p, fieldName: "url", required: false, type: ForwardOffset<String>.self)
    _v.finish()
  }
}

extension hushh_hcf_Product: Encodable {

  enum CodingKeys: String, CodingKey {
    case id = "id"
    case description = "description"
    case url = "url"
  }
  public func encode(to encoder: Encoder) throws {
    var container = encoder.container(keyedBy: CodingKeys.self)
    try container.encodeIfPresent(id, forKey: .id)
    try container.encodeIfPresent(description, forKey: .description)
    try container.encodeIfPresent(url, forKey: .url)
  }
}

public class hushh_hcf_ProductT: NativeObject {

  public var id: String?
  public var description: String?
  public var url: String?

  public init(_ _t: inout hushh_hcf_Product) {
    id = _t.id
    description = _t.description
    url = _t.url
  }

  public init() {
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

extension hushh_hcf_Embedding: Encodable {

  enum CodingKeys: String, CodingKey {
    case v = "v"
  }
  public func encode(to encoder: Encoder) throws {
    var container = encoder.container(keyedBy: CodingKeys.self)
    if vCount > 0 {
      try container.encodeIfPresent(v, forKey: .v)
    }
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
public struct hushh_hcf_VibeMetadata: FlatBufferObject, Verifiable, ObjectAPIPacker {

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
    case compositionIds = 12
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
  public var hasCompositionIds: Bool { let o = _accessor.offset(VTOFFSET.compositionIds.v); return o == 0 ? false : true }
  public var compositionIdsCount: Int32 { let o = _accessor.offset(VTOFFSET.compositionIds.v); return o == 0 ? 0 : _accessor.vector(count: o) }
  public func compositionIds(at index: Int32) -> String? { let o = _accessor.offset(VTOFFSET.compositionIds.v); return o == 0 ? nil : _accessor.directString(at: _accessor.vector(at: o) + index * 4) }
  public static func startVibeMetadata(_ fbb: inout FlatBufferBuilder) -> UOffset { fbb.startTable(with: 5) }
  public static func add(id: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: id, at: VTOFFSET.id.p) }
  public static func add(description: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: description, at: VTOFFSET.description.p) }
  public static func add(imageBase64: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: imageBase64, at: VTOFFSET.imageBase64.p) }
  public static func add(url: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: url, at: VTOFFSET.url.p) }
  public static func addVectorOf(compositionIds: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: compositionIds, at: VTOFFSET.compositionIds.p) }
  public static func endVibeMetadata(_ fbb: inout FlatBufferBuilder, start: UOffset) -> Offset { let end = Offset(offset: fbb.endTable(at: start)); return end }
  public static func createVibeMetadata(
    _ fbb: inout FlatBufferBuilder,
    idOffset id: Offset = Offset(),
    descriptionOffset description: Offset = Offset(),
    imageBase64Offset imageBase64: Offset = Offset(),
    urlOffset url: Offset = Offset(),
    compositionIdsVectorOffset compositionIds: Offset = Offset()
  ) -> Offset {
    let __start = hushh_hcf_VibeMetadata.startVibeMetadata(&fbb)
    hushh_hcf_VibeMetadata.add(id: id, &fbb)
    hushh_hcf_VibeMetadata.add(description: description, &fbb)
    hushh_hcf_VibeMetadata.add(imageBase64: imageBase64, &fbb)
    hushh_hcf_VibeMetadata.add(url: url, &fbb)
    hushh_hcf_VibeMetadata.addVectorOf(compositionIds: compositionIds, &fbb)
    return hushh_hcf_VibeMetadata.endVibeMetadata(&fbb, start: __start)
  }
  

  public mutating func unpack() -> hushh_hcf_VibeMetadataT {
    return hushh_hcf_VibeMetadataT(&self)
  }
  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout hushh_hcf_VibeMetadataT?) -> Offset {
    guard var obj = obj else { return Offset() }
    return pack(&builder, obj: &obj)
  }

  public static func pack(_ builder: inout FlatBufferBuilder, obj: inout hushh_hcf_VibeMetadataT) -> Offset {
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

    let __compositionIds = builder.createVector(ofStrings: obj.compositionIds.compactMap({ $0 }) )
    let __root = hushh_hcf_VibeMetadata.startVibeMetadata(&builder)
    hushh_hcf_VibeMetadata.add(id: __id, &builder)
    hushh_hcf_VibeMetadata.add(description: __description, &builder)
    hushh_hcf_VibeMetadata.add(imageBase64: __imageBase64, &builder)
    hushh_hcf_VibeMetadata.add(url: __url, &builder)
    hushh_hcf_VibeMetadata.addVectorOf(compositionIds: __compositionIds, &builder)
    return hushh_hcf_VibeMetadata.endVibeMetadata(&builder, start: __root)
  }

  public static func verify<T>(_ verifier: inout Verifier, at position: Int, of type: T.Type) throws where T: Verifiable {
    var _v = try verifier.visitTable(at: position)
    try _v.visit(field: VTOFFSET.id.p, fieldName: "id", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.description.p, fieldName: "description", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.imageBase64.p, fieldName: "imageBase64", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.url.p, fieldName: "url", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.compositionIds.p, fieldName: "compositionIds", required: false, type: ForwardOffset<Vector<ForwardOffset<String>, String>>.self)
    _v.finish()
  }
}

extension hushh_hcf_VibeMetadata: Encodable {

  enum CodingKeys: String, CodingKey {
    case id = "id"
    case description = "description"
    case imageBase64 = "image_base64"
    case url = "url"
    case compositionIds = "composition_ids"
  }
  public func encode(to encoder: Encoder) throws {
    var container = encoder.container(keyedBy: CodingKeys.self)
    try container.encodeIfPresent(id, forKey: .id)
    try container.encodeIfPresent(description, forKey: .description)
    try container.encodeIfPresent(imageBase64, forKey: .imageBase64)
    try container.encodeIfPresent(url, forKey: .url)
    if compositionIdsCount > 0 {
      var contentEncoder = container.nestedUnkeyedContainer(forKey: .compositionIds)
      for index in 0..<compositionIdsCount {
        guard let type = compositionIds(at: index) else { continue }
        try contentEncoder.encode(type)
      }
    }
  }
}

public class hushh_hcf_VibeMetadataT: NativeObject {

  public var id: String?
  public var description: String?
  public var imageBase64: String?
  public var url: String?
  public var compositionIds: [String?]

  public init(_ _t: inout hushh_hcf_VibeMetadata) {
    id = _t.id
    description = _t.description
    imageBase64 = _t.imageBase64
    url = _t.url
    compositionIds = []
    for index in 0..<_t.compositionIdsCount {
        compositionIds.append(_t.compositionIds(at: index))
    }
  }

  public init() {
    compositionIds = []
  }

  public func serialize() -> ByteBuffer { return serialize(type: hushh_hcf_VibeMetadata.self) }

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
    case products = 8
    case vibeMetadata = 10
    case vibeEmbeddings = 12
    case compositionMetadata = 14
    case compositionEmbedding = 16
    var v: Int32 { Int32(self.rawValue) }
    var p: VOffset { self.rawValue }
  }

  public var id: String? { let o = _accessor.offset(VTOFFSET.id.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var idSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.id.v) }
  public var version: String? { let o = _accessor.offset(VTOFFSET.version.v); return o == 0 ? nil : _accessor.string(at: o) }
  public var versionSegmentArray: [UInt8]? { return _accessor.getVector(at: VTOFFSET.version.v) }
  public var hasProducts: Bool { let o = _accessor.offset(VTOFFSET.products.v); return o == 0 ? false : true }
  public var productsCount: Int32 { let o = _accessor.offset(VTOFFSET.products.v); return o == 0 ? 0 : _accessor.vector(count: o) }
  public func products(at index: Int32) -> hushh_hcf_Product? { let o = _accessor.offset(VTOFFSET.products.v); return o == 0 ? nil : hushh_hcf_Product(_accessor.bb, o: _accessor.indirect(_accessor.vector(at: o) + index * 4)) }
  public var hasVibeMetadata: Bool { let o = _accessor.offset(VTOFFSET.vibeMetadata.v); return o == 0 ? false : true }
  public var vibeMetadataCount: Int32 { let o = _accessor.offset(VTOFFSET.vibeMetadata.v); return o == 0 ? 0 : _accessor.vector(count: o) }
  public func vibeMetadata(at index: Int32) -> hushh_hcf_VibeMetadata? { let o = _accessor.offset(VTOFFSET.vibeMetadata.v); return o == 0 ? nil : hushh_hcf_VibeMetadata(_accessor.bb, o: _accessor.indirect(_accessor.vector(at: o) + index * 4)) }
  public var hasVibeEmbeddings: Bool { let o = _accessor.offset(VTOFFSET.vibeEmbeddings.v); return o == 0 ? false : true }
  public var vibeEmbeddingsCount: Int32 { let o = _accessor.offset(VTOFFSET.vibeEmbeddings.v); return o == 0 ? 0 : _accessor.vector(count: o) }
  public func vibeEmbeddings(at index: Int32) -> hushh_hcf_Embedding? { let o = _accessor.offset(VTOFFSET.vibeEmbeddings.v); return o == 0 ? nil : hushh_hcf_Embedding(_accessor.bb, o: _accessor.indirect(_accessor.vector(at: o) + index * 4)) }
  public var hasCompositionMetadata: Bool { let o = _accessor.offset(VTOFFSET.compositionMetadata.v); return o == 0 ? false : true }
  public var compositionMetadataCount: Int32 { let o = _accessor.offset(VTOFFSET.compositionMetadata.v); return o == 0 ? 0 : _accessor.vector(count: o) }
  public func compositionMetadata(at index: Int32) -> hushh_hcf_CompositionMetadata? { let o = _accessor.offset(VTOFFSET.compositionMetadata.v); return o == 0 ? nil : hushh_hcf_CompositionMetadata(_accessor.bb, o: _accessor.indirect(_accessor.vector(at: o) + index * 4)) }
  public var hasCompositionEmbedding: Bool { let o = _accessor.offset(VTOFFSET.compositionEmbedding.v); return o == 0 ? false : true }
  public var compositionEmbeddingCount: Int32 { let o = _accessor.offset(VTOFFSET.compositionEmbedding.v); return o == 0 ? 0 : _accessor.vector(count: o) }
  public func compositionEmbedding(at index: Int32) -> hushh_hcf_Embedding? { let o = _accessor.offset(VTOFFSET.compositionEmbedding.v); return o == 0 ? nil : hushh_hcf_Embedding(_accessor.bb, o: _accessor.indirect(_accessor.vector(at: o) + index * 4)) }
  public static func startCatalog(_ fbb: inout FlatBufferBuilder) -> UOffset { fbb.startTable(with: 7) }
  public static func add(id: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: id, at: VTOFFSET.id.p) }
  public static func add(version: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: version, at: VTOFFSET.version.p) }
  public static func addVectorOf(products: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: products, at: VTOFFSET.products.p) }
  public static func addVectorOf(vibeMetadata: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: vibeMetadata, at: VTOFFSET.vibeMetadata.p) }
  public static func addVectorOf(vibeEmbeddings: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: vibeEmbeddings, at: VTOFFSET.vibeEmbeddings.p) }
  public static func addVectorOf(compositionMetadata: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: compositionMetadata, at: VTOFFSET.compositionMetadata.p) }
  public static func addVectorOf(compositionEmbedding: Offset, _ fbb: inout FlatBufferBuilder) { fbb.add(offset: compositionEmbedding, at: VTOFFSET.compositionEmbedding.p) }
  public static func endCatalog(_ fbb: inout FlatBufferBuilder, start: UOffset) -> Offset { let end = Offset(offset: fbb.endTable(at: start)); return end }
  public static func createCatalog(
    _ fbb: inout FlatBufferBuilder,
    idOffset id: Offset = Offset(),
    versionOffset version: Offset = Offset(),
    productsVectorOffset products: Offset = Offset(),
    vibeMetadataVectorOffset vibeMetadata: Offset = Offset(),
    vibeEmbeddingsVectorOffset vibeEmbeddings: Offset = Offset(),
    compositionMetadataVectorOffset compositionMetadata: Offset = Offset(),
    compositionEmbeddingVectorOffset compositionEmbedding: Offset = Offset()
  ) -> Offset {
    let __start = hushh_hcf_Catalog.startCatalog(&fbb)
    hushh_hcf_Catalog.add(id: id, &fbb)
    hushh_hcf_Catalog.add(version: version, &fbb)
    hushh_hcf_Catalog.addVectorOf(products: products, &fbb)
    hushh_hcf_Catalog.addVectorOf(vibeMetadata: vibeMetadata, &fbb)
    hushh_hcf_Catalog.addVectorOf(vibeEmbeddings: vibeEmbeddings, &fbb)
    hushh_hcf_Catalog.addVectorOf(compositionMetadata: compositionMetadata, &fbb)
    hushh_hcf_Catalog.addVectorOf(compositionEmbedding: compositionEmbedding, &fbb)
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

    var __products__: [Offset] = []
    for var i in obj.products {
      __products__.append(hushh_hcf_Product.pack(&builder, obj: &i))
    }
    let __products = builder.createVector(ofOffsets: __products__)
    var __vibeMetadata__: [Offset] = []
    for var i in obj.vibeMetadata {
      __vibeMetadata__.append(hushh_hcf_VibeMetadata.pack(&builder, obj: &i))
    }
    let __vibeMetadata = builder.createVector(ofOffsets: __vibeMetadata__)
    var __vibeEmbeddings__: [Offset] = []
    for var i in obj.vibeEmbeddings {
      __vibeEmbeddings__.append(hushh_hcf_Embedding.pack(&builder, obj: &i))
    }
    let __vibeEmbeddings = builder.createVector(ofOffsets: __vibeEmbeddings__)
    var __compositionMetadata__: [Offset] = []
    for var i in obj.compositionMetadata {
      __compositionMetadata__.append(hushh_hcf_CompositionMetadata.pack(&builder, obj: &i))
    }
    let __compositionMetadata = builder.createVector(ofOffsets: __compositionMetadata__)
    var __compositionEmbedding__: [Offset] = []
    for var i in obj.compositionEmbedding {
      __compositionEmbedding__.append(hushh_hcf_Embedding.pack(&builder, obj: &i))
    }
    let __compositionEmbedding = builder.createVector(ofOffsets: __compositionEmbedding__)
    let __root = hushh_hcf_Catalog.startCatalog(&builder)
    hushh_hcf_Catalog.add(id: __id, &builder)
    hushh_hcf_Catalog.add(version: __version, &builder)
    hushh_hcf_Catalog.addVectorOf(products: __products, &builder)
    hushh_hcf_Catalog.addVectorOf(vibeMetadata: __vibeMetadata, &builder)
    hushh_hcf_Catalog.addVectorOf(vibeEmbeddings: __vibeEmbeddings, &builder)
    hushh_hcf_Catalog.addVectorOf(compositionMetadata: __compositionMetadata, &builder)
    hushh_hcf_Catalog.addVectorOf(compositionEmbedding: __compositionEmbedding, &builder)
    return hushh_hcf_Catalog.endCatalog(&builder, start: __root)
  }

  public static func verify<T>(_ verifier: inout Verifier, at position: Int, of type: T.Type) throws where T: Verifiable {
    var _v = try verifier.visitTable(at: position)
    try _v.visit(field: VTOFFSET.id.p, fieldName: "id", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.version.p, fieldName: "version", required: false, type: ForwardOffset<String>.self)
    try _v.visit(field: VTOFFSET.products.p, fieldName: "products", required: false, type: ForwardOffset<Vector<ForwardOffset<hushh_hcf_Product>, hushh_hcf_Product>>.self)
    try _v.visit(field: VTOFFSET.vibeMetadata.p, fieldName: "vibeMetadata", required: false, type: ForwardOffset<Vector<ForwardOffset<hushh_hcf_VibeMetadata>, hushh_hcf_VibeMetadata>>.self)
    try _v.visit(field: VTOFFSET.vibeEmbeddings.p, fieldName: "vibeEmbeddings", required: false, type: ForwardOffset<Vector<ForwardOffset<hushh_hcf_Embedding>, hushh_hcf_Embedding>>.self)
    try _v.visit(field: VTOFFSET.compositionMetadata.p, fieldName: "compositionMetadata", required: false, type: ForwardOffset<Vector<ForwardOffset<hushh_hcf_CompositionMetadata>, hushh_hcf_CompositionMetadata>>.self)
    try _v.visit(field: VTOFFSET.compositionEmbedding.p, fieldName: "compositionEmbedding", required: false, type: ForwardOffset<Vector<ForwardOffset<hushh_hcf_Embedding>, hushh_hcf_Embedding>>.self)
    _v.finish()
  }
}

extension hushh_hcf_Catalog: Encodable {

  enum CodingKeys: String, CodingKey {
    case id = "id"
    case version = "version"
    case products = "products"
    case vibeMetadata = "vibe_metadata"
    case vibeEmbeddings = "vibe_embeddings"
    case compositionMetadata = "composition_metadata"
    case compositionEmbedding = "composition_embedding"
  }
  public func encode(to encoder: Encoder) throws {
    var container = encoder.container(keyedBy: CodingKeys.self)
    try container.encodeIfPresent(id, forKey: .id)
    try container.encodeIfPresent(version, forKey: .version)
    if productsCount > 0 {
      var contentEncoder = container.nestedUnkeyedContainer(forKey: .products)
      for index in 0..<productsCount {
        guard let type = products(at: index) else { continue }
        try contentEncoder.encode(type)
      }
    }
    if vibeMetadataCount > 0 {
      var contentEncoder = container.nestedUnkeyedContainer(forKey: .vibeMetadata)
      for index in 0..<vibeMetadataCount {
        guard let type = vibeMetadata(at: index) else { continue }
        try contentEncoder.encode(type)
      }
    }
    if vibeEmbeddingsCount > 0 {
      var contentEncoder = container.nestedUnkeyedContainer(forKey: .vibeEmbeddings)
      for index in 0..<vibeEmbeddingsCount {
        guard let type = vibeEmbeddings(at: index) else { continue }
        try contentEncoder.encode(type)
      }
    }
    if compositionMetadataCount > 0 {
      var contentEncoder = container.nestedUnkeyedContainer(forKey: .compositionMetadata)
      for index in 0..<compositionMetadataCount {
        guard let type = compositionMetadata(at: index) else { continue }
        try contentEncoder.encode(type)
      }
    }
    if compositionEmbeddingCount > 0 {
      var contentEncoder = container.nestedUnkeyedContainer(forKey: .compositionEmbedding)
      for index in 0..<compositionEmbeddingCount {
        guard let type = compositionEmbedding(at: index) else { continue }
        try contentEncoder.encode(type)
      }
    }
  }
}

public class hushh_hcf_CatalogT: NativeObject {

  public var id: String?
  public var version: String?
  public var products: [hushh_hcf_ProductT?]
  public var vibeMetadata: [hushh_hcf_VibeMetadataT?]
  public var vibeEmbeddings: [hushh_hcf_EmbeddingT?]
  public var compositionMetadata: [hushh_hcf_CompositionMetadataT?]
  public var compositionEmbedding: [hushh_hcf_EmbeddingT?]

  public init(_ _t: inout hushh_hcf_Catalog) {
    id = _t.id
    version = _t.version
    products = []
    for index in 0..<_t.productsCount {
        var __v_ = _t.products(at: index)
        products.append(__v_?.unpack())
    }
    vibeMetadata = []
    for index in 0..<_t.vibeMetadataCount {
        var __v_ = _t.vibeMetadata(at: index)
        vibeMetadata.append(__v_?.unpack())
    }
    vibeEmbeddings = []
    for index in 0..<_t.vibeEmbeddingsCount {
        var __v_ = _t.vibeEmbeddings(at: index)
        vibeEmbeddings.append(__v_?.unpack())
    }
    compositionMetadata = []
    for index in 0..<_t.compositionMetadataCount {
        var __v_ = _t.compositionMetadata(at: index)
        compositionMetadata.append(__v_?.unpack())
    }
    compositionEmbedding = []
    for index in 0..<_t.compositionEmbeddingCount {
        var __v_ = _t.compositionEmbedding(at: index)
        compositionEmbedding.append(__v_?.unpack())
    }
  }

  public init() {
    products = []
    vibeMetadata = []
    vibeEmbeddings = []
    compositionMetadata = []
    compositionEmbedding = []
  }

  public func serialize() -> ByteBuffer { return serialize(type: hushh_hcf_Catalog.self) }

}
