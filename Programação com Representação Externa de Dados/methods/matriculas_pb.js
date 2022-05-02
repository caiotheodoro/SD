// source: matriculas.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {missingRequire} reports error on implicit type usages.
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!
/* eslint-disable */
// @ts-nocheck

var jspb = require('google-protobuf');
var goog = jspb;
var global = (function() { return this || window || global || self || Function('return this')(); }).call(null);

goog.exportSymbol('proto.Matricula', null, global);
goog.exportSymbol('proto.Matriculas', null, global);
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.Matricula = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.Matricula, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.Matricula.displayName = 'proto.Matricula';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.Matriculas = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.Matriculas.repeatedFields_, null);
};
goog.inherits(proto.Matriculas, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.Matriculas.displayName = 'proto.Matriculas';
}



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.Matricula.prototype.toObject = function(opt_includeInstance) {
  return proto.Matricula.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.Matricula} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.Matricula.toObject = function(includeInstance, msg) {
  var f, obj = {
    ra: jspb.Message.getFieldWithDefault(msg, 1, 0),
    codDisciplina: jspb.Message.getFieldWithDefault(msg, 2, ""),
    ano: jspb.Message.getFieldWithDefault(msg, 3, 0),
    semestre: jspb.Message.getFieldWithDefault(msg, 4, 0),
    nota: jspb.Message.getFloatingPointFieldWithDefault(msg, 5, 0.0),
    faltas: jspb.Message.getFieldWithDefault(msg, 6, 0)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.Matricula}
 */
proto.Matricula.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.Matricula;
  return proto.Matricula.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.Matricula} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.Matricula}
 */
proto.Matricula.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setRa(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setCodDisciplina(value);
      break;
    case 3:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setAno(value);
      break;
    case 4:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setSemestre(value);
      break;
    case 5:
      var value = /** @type {number} */ (reader.readFloat());
      msg.setNota(value);
      break;
    case 6:
      var value = /** @type {number} */ (reader.readInt32());
      msg.setFaltas(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.Matricula.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.Matricula.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.Matricula} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.Matricula.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getRa();
  if (f !== 0) {
    writer.writeInt32(
      1,
      f
    );
  }
  f = message.getCodDisciplina();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
  f = message.getAno();
  if (f !== 0) {
    writer.writeInt32(
      3,
      f
    );
  }
  f = message.getSemestre();
  if (f !== 0) {
    writer.writeInt32(
      4,
      f
    );
  }
  f = message.getNota();
  if (f !== 0.0) {
    writer.writeFloat(
      5,
      f
    );
  }
  f = message.getFaltas();
  if (f !== 0) {
    writer.writeInt32(
      6,
      f
    );
  }
};


/**
 * optional int32 RA = 1;
 * @return {number}
 */
proto.Matricula.prototype.getRa = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/**
 * @param {number} value
 * @return {!proto.Matricula} returns this
 */
proto.Matricula.prototype.setRa = function(value) {
  return jspb.Message.setProto3IntField(this, 1, value);
};


/**
 * optional string cod_disciplina = 2;
 * @return {string}
 */
proto.Matricula.prototype.getCodDisciplina = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/**
 * @param {string} value
 * @return {!proto.Matricula} returns this
 */
proto.Matricula.prototype.setCodDisciplina = function(value) {
  return jspb.Message.setProto3StringField(this, 2, value);
};


/**
 * optional int32 ano = 3;
 * @return {number}
 */
proto.Matricula.prototype.getAno = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 3, 0));
};


/**
 * @param {number} value
 * @return {!proto.Matricula} returns this
 */
proto.Matricula.prototype.setAno = function(value) {
  return jspb.Message.setProto3IntField(this, 3, value);
};


/**
 * optional int32 semestre = 4;
 * @return {number}
 */
proto.Matricula.prototype.getSemestre = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 4, 0));
};


/**
 * @param {number} value
 * @return {!proto.Matricula} returns this
 */
proto.Matricula.prototype.setSemestre = function(value) {
  return jspb.Message.setProto3IntField(this, 4, value);
};


/**
 * optional float nota = 5;
 * @return {number}
 */
proto.Matricula.prototype.getNota = function() {
  return /** @type {number} */ (jspb.Message.getFloatingPointFieldWithDefault(this, 5, 0.0));
};


/**
 * @param {number} value
 * @return {!proto.Matricula} returns this
 */
proto.Matricula.prototype.setNota = function(value) {
  return jspb.Message.setProto3FloatField(this, 5, value);
};


/**
 * optional int32 faltas = 6;
 * @return {number}
 */
proto.Matricula.prototype.getFaltas = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 6, 0));
};


/**
 * @param {number} value
 * @return {!proto.Matricula} returns this
 */
proto.Matricula.prototype.setFaltas = function(value) {
  return jspb.Message.setProto3IntField(this, 6, value);
};



/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.Matriculas.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.Matriculas.prototype.toObject = function(opt_includeInstance) {
  return proto.Matriculas.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.Matriculas} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.Matriculas.toObject = function(includeInstance, msg) {
  var f, obj = {
    matriculasList: jspb.Message.toObjectList(msg.getMatriculasList(),
    proto.Matricula.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.Matriculas}
 */
proto.Matriculas.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.Matriculas;
  return proto.Matriculas.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.Matriculas} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.Matriculas}
 */
proto.Matriculas.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.Matricula;
      reader.readMessage(value,proto.Matricula.deserializeBinaryFromReader);
      msg.addMatriculas(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.Matriculas.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.Matriculas.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.Matriculas} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.Matriculas.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getMatriculasList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.Matricula.serializeBinaryToWriter
    );
  }
};


/**
 * repeated Matricula matriculas = 1;
 * @return {!Array<!proto.Matricula>}
 */
proto.Matriculas.prototype.getMatriculasList = function() {
  return /** @type{!Array<!proto.Matricula>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.Matricula, 1));
};


/**
 * @param {!Array<!proto.Matricula>} value
 * @return {!proto.Matriculas} returns this
*/
proto.Matriculas.prototype.setMatriculasList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.Matricula=} opt_value
 * @param {number=} opt_index
 * @return {!proto.Matricula}
 */
proto.Matriculas.prototype.addMatriculas = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.Matricula, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.Matriculas} returns this
 */
proto.Matriculas.prototype.clearMatriculasList = function() {
  return this.setMatriculasList([]);
};


goog.object.extend(exports, proto);
