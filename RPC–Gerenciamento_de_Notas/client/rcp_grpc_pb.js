// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var rcp_pb = require('./rcp_pb.js');

function serialize_AlunosReq(arg) {
  if (!(arg instanceof rcp_pb.AlunosReq)) {
    throw new Error('Expected argument of type AlunosReq');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_AlunosReq(buffer_arg) {
  return rcp_pb.AlunosReq.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_AlunosRes(arg) {
  if (!(arg instanceof rcp_pb.AlunosRes)) {
    throw new Error('Expected argument of type AlunosRes');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_AlunosRes(buffer_arg) {
  return rcp_pb.AlunosRes.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_CrudMatricula(arg) {
  if (!(arg instanceof rcp_pb.CrudMatricula)) {
    throw new Error('Expected argument of type CrudMatricula');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_CrudMatricula(buffer_arg) {
  return rcp_pb.CrudMatricula.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_Matricula(arg) {
  if (!(arg instanceof rcp_pb.Matricula)) {
    throw new Error('Expected argument of type Matricula');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_Matricula(buffer_arg) {
  return rcp_pb.Matricula.deserializeBinary(new Uint8Array(buffer_arg));
}


var ServicesService = exports.ServicesService = {
  inserirMatricula: {
    path: '/Services/InserirMatricula',
    requestStream: false,
    responseStream: false,
    requestType: rcp_pb.Matricula,
    responseType: rcp_pb.CrudMatricula,
    requestSerialize: serialize_Matricula,
    requestDeserialize: deserialize_Matricula,
    responseSerialize: serialize_CrudMatricula,
    responseDeserialize: deserialize_CrudMatricula,
  },
  alterarMatricula: {
    path: '/Services/AlterarMatricula',
    requestStream: false,
    responseStream: false,
    requestType: rcp_pb.Matricula,
    responseType: rcp_pb.CrudMatricula,
    requestSerialize: serialize_Matricula,
    requestDeserialize: deserialize_Matricula,
    responseSerialize: serialize_CrudMatricula,
    responseDeserialize: deserialize_CrudMatricula,
  },
  listarDisciplinas: {
    path: '/Services/ListarDisciplinas',
    requestStream: false,
    responseStream: false,
    requestType: rcp_pb.Matricula,
    responseType: rcp_pb.CrudMatricula,
    requestSerialize: serialize_Matricula,
    requestDeserialize: deserialize_Matricula,
    responseSerialize: serialize_CrudMatricula,
    responseDeserialize: deserialize_CrudMatricula,
  },
  listarAlunos: {
    path: '/Services/ListarAlunos',
    requestStream: false,
    responseStream: false,
    requestType: rcp_pb.AlunosReq,
    responseType: rcp_pb.AlunosRes,
    requestSerialize: serialize_AlunosReq,
    requestDeserialize: deserialize_AlunosReq,
    responseSerialize: serialize_AlunosRes,
    responseDeserialize: deserialize_AlunosRes,
  },
};

exports.ServicesClient = grpc.makeGenericClientConstructor(ServicesService);
