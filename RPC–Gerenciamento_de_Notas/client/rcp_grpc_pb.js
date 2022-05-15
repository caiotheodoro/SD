// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var rcp_pb = require('./rcp_pb.js');

function serialize_AlterarFaltasReq(arg) {
  if (!(arg instanceof rcp_pb.AlterarFaltasReq)) {
    throw new Error('Expected argument of type AlterarFaltasReq');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_AlterarFaltasReq(buffer_arg) {
  return rcp_pb.AlterarFaltasReq.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_AlterarNotaReq(arg) {
  if (!(arg instanceof rcp_pb.AlterarNotaReq)) {
    throw new Error('Expected argument of type AlterarNotaReq');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_AlterarNotaReq(buffer_arg) {
  return rcp_pb.AlterarNotaReq.deserializeBinary(new Uint8Array(buffer_arg));
}

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

function serialize_DisciplinasReq(arg) {
  if (!(arg instanceof rcp_pb.DisciplinasReq)) {
    throw new Error('Expected argument of type DisciplinasReq');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_DisciplinasReq(buffer_arg) {
  return rcp_pb.DisciplinasReq.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_DisciplinasRes(arg) {
  if (!(arg instanceof rcp_pb.DisciplinasRes)) {
    throw new Error('Expected argument of type DisciplinasRes');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_DisciplinasRes(buffer_arg) {
  return rcp_pb.DisciplinasRes.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_InserirMatriculaRes(arg) {
  if (!(arg instanceof rcp_pb.InserirMatriculaRes)) {
    throw new Error('Expected argument of type InserirMatriculaRes');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_InserirMatriculaRes(buffer_arg) {
  return rcp_pb.InserirMatriculaRes.deserializeBinary(new Uint8Array(buffer_arg));
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

function serialize_MessageRes(arg) {
  if (!(arg instanceof rcp_pb.MessageRes)) {
    throw new Error('Expected argument of type MessageRes');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_MessageRes(buffer_arg) {
  return rcp_pb.MessageRes.deserializeBinary(new Uint8Array(buffer_arg));
}


var ServicesService = exports.ServicesService = {
  inserirMatricula: {
    path: '/Services/InserirMatricula',
    requestStream: false,
    responseStream: false,
    requestType: rcp_pb.Matricula,
    responseType: rcp_pb.InserirMatriculaRes,
    requestSerialize: serialize_Matricula,
    requestDeserialize: deserialize_Matricula,
    responseSerialize: serialize_InserirMatriculaRes,
    responseDeserialize: deserialize_InserirMatriculaRes,
  },
  alterarNota: {
    path: '/Services/AlterarNota',
    requestStream: false,
    responseStream: false,
    requestType: rcp_pb.AlterarNotaReq,
    responseType: rcp_pb.MessageRes,
    requestSerialize: serialize_AlterarNotaReq,
    requestDeserialize: deserialize_AlterarNotaReq,
    responseSerialize: serialize_MessageRes,
    responseDeserialize: deserialize_MessageRes,
  },
  alterarFaltas: {
    path: '/Services/AlterarFaltas',
    requestStream: false,
    responseStream: false,
    requestType: rcp_pb.AlterarFaltasReq,
    responseType: rcp_pb.MessageRes,
    requestSerialize: serialize_AlterarFaltasReq,
    requestDeserialize: deserialize_AlterarFaltasReq,
    responseSerialize: serialize_MessageRes,
    responseDeserialize: deserialize_MessageRes,
  },
  listarDisciplinas: {
    path: '/Services/ListarDisciplinas',
    requestStream: false,
    responseStream: false,
    requestType: rcp_pb.DisciplinasReq,
    responseType: rcp_pb.DisciplinasRes,
    requestSerialize: serialize_DisciplinasReq,
    requestDeserialize: deserialize_DisciplinasReq,
    responseSerialize: serialize_DisciplinasRes,
    responseDeserialize: deserialize_DisciplinasRes,
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
