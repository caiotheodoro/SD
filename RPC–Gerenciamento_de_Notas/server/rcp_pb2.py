# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/rcp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fproto/rcp.proto\"I\n\x0fListaDisciplina\x12\n\n\x02RA\x18\x01 \x01(\x05\x12\x0c\n\x04nome\x18\x02 \x01(\t\x12\x0c\n\x04nota\x18\x03 \x01(\x02\x12\x0e\n\x06\x66\x61ltas\x18\x04 \x01(\x05\"/\n\x0e\x44isciplinasReq\x12\x0b\n\x03\x61no\x18\x01 \x01(\x05\x12\x10\n\x08semestre\x18\x02 \x01(\x05\"H\n\x0e\x44isciplinasRes\x12%\n\x0b\x64isciplinas\x18\x01 \x03(\x0b\x32\x10.ListaDisciplina\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1d\n\nMessageRes\x12\x0f\n\x07message\x18\x01 \x01(\t\"B\n\x0e\x41lterarNotaReq\x12\n\n\x02RA\x18\x01 \x01(\x05\x12\x16\n\x0e\x63od_disciplina\x18\x02 \x01(\t\x12\x0c\n\x04nota\x18\x03 \x01(\x02\"F\n\x10\x41lterarFaltasReq\x12\n\n\x02RA\x18\x01 \x01(\x05\x12\x16\n\x0e\x63od_disciplina\x18\x02 \x01(\t\x12\x0e\n\x06\x66\x61ltas\x18\x03 \x01(\x05\"l\n\tMatricula\x12\n\n\x02RA\x18\x01 \x01(\x05\x12\x16\n\x0e\x63od_disciplina\x18\x02 \x01(\t\x12\x0b\n\x03\x61no\x18\x03 \x01(\x05\x12\x10\n\x08semestre\x18\x04 \x01(\x05\x12\x0c\n\x04nota\x18\x05 \x01(\x02\x12\x0e\n\x06\x66\x61ltas\x18\x06 \x01(\x05\"E\n\x13InserirMatriculaRes\x12\x1d\n\tmatricula\x18\x02 \x01(\x0b\x32\n.Matricula\x12\x0f\n\x07message\x18\x03 \x01(\t\"B\n\tAlunosReq\x12\x16\n\x0e\x63od_disciplina\x18\x01 \x01(\t\x12\x0b\n\x03\x61no\x18\x02 \x01(\x05\x12\x10\n\x08semestre\x18\x03 \x01(\x05\"4\n\tAlunosRes\x12\x16\n\x06\x61lunos\x18\x01 \x03(\x0b\x32\x06.Aluno\x12\x0f\n\x07message\x18\x02 \x01(\t\"E\n\x05\x41luno\x12\n\n\x02RA\x18\x01 \x01(\x05\x12\x0c\n\x04nome\x18\x02 \x01(\t\x12\x0f\n\x07periodo\x18\x03 \x01(\x05\x12\x11\n\tcod_curso\x18\x04 \x01(\x05\x32\x87\x02\n\x08Services\x12\x36\n\x10InserirMatricula\x12\n.Matricula\x1a\x14.InserirMatriculaRes\"\x00\x12-\n\x0b\x41lterarNota\x12\x0f.AlterarNotaReq\x1a\x0b.MessageRes\"\x00\x12\x31\n\rAlterarFaltas\x12\x11.AlterarFaltasReq\x1a\x0b.MessageRes\"\x00\x12\x37\n\x11ListarDisciplinas\x12\x0f.DisciplinasReq\x1a\x0f.DisciplinasRes\"\x00\x12(\n\x0cListarAlunos\x12\n.AlunosReq\x1a\n.AlunosRes\"\x00\x42$\xca\x02\tApp\\Proto\xe2\x02\x15\x41pp\\Proto\\GPBMetadatab\x06proto3')



_LISTADISCIPLINA = DESCRIPTOR.message_types_by_name['ListaDisciplina']
_DISCIPLINASREQ = DESCRIPTOR.message_types_by_name['DisciplinasReq']
_DISCIPLINASRES = DESCRIPTOR.message_types_by_name['DisciplinasRes']
_MESSAGERES = DESCRIPTOR.message_types_by_name['MessageRes']
_ALTERARNOTAREQ = DESCRIPTOR.message_types_by_name['AlterarNotaReq']
_ALTERARFALTASREQ = DESCRIPTOR.message_types_by_name['AlterarFaltasReq']
_MATRICULA = DESCRIPTOR.message_types_by_name['Matricula']
_INSERIRMATRICULARES = DESCRIPTOR.message_types_by_name['InserirMatriculaRes']
_ALUNOSREQ = DESCRIPTOR.message_types_by_name['AlunosReq']
_ALUNOSRES = DESCRIPTOR.message_types_by_name['AlunosRes']
_ALUNO = DESCRIPTOR.message_types_by_name['Aluno']
ListaDisciplina = _reflection.GeneratedProtocolMessageType('ListaDisciplina', (_message.Message,), {
  'DESCRIPTOR' : _LISTADISCIPLINA,
  '__module__' : 'proto.rcp_pb2'
  # @@protoc_insertion_point(class_scope:ListaDisciplina)
  })
_sym_db.RegisterMessage(ListaDisciplina)

DisciplinasReq = _reflection.GeneratedProtocolMessageType('DisciplinasReq', (_message.Message,), {
  'DESCRIPTOR' : _DISCIPLINASREQ,
  '__module__' : 'proto.rcp_pb2'
  # @@protoc_insertion_point(class_scope:DisciplinasReq)
  })
_sym_db.RegisterMessage(DisciplinasReq)

DisciplinasRes = _reflection.GeneratedProtocolMessageType('DisciplinasRes', (_message.Message,), {
  'DESCRIPTOR' : _DISCIPLINASRES,
  '__module__' : 'proto.rcp_pb2'
  # @@protoc_insertion_point(class_scope:DisciplinasRes)
  })
_sym_db.RegisterMessage(DisciplinasRes)

MessageRes = _reflection.GeneratedProtocolMessageType('MessageRes', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGERES,
  '__module__' : 'proto.rcp_pb2'
  # @@protoc_insertion_point(class_scope:MessageRes)
  })
_sym_db.RegisterMessage(MessageRes)

AlterarNotaReq = _reflection.GeneratedProtocolMessageType('AlterarNotaReq', (_message.Message,), {
  'DESCRIPTOR' : _ALTERARNOTAREQ,
  '__module__' : 'proto.rcp_pb2'
  # @@protoc_insertion_point(class_scope:AlterarNotaReq)
  })
_sym_db.RegisterMessage(AlterarNotaReq)

AlterarFaltasReq = _reflection.GeneratedProtocolMessageType('AlterarFaltasReq', (_message.Message,), {
  'DESCRIPTOR' : _ALTERARFALTASREQ,
  '__module__' : 'proto.rcp_pb2'
  # @@protoc_insertion_point(class_scope:AlterarFaltasReq)
  })
_sym_db.RegisterMessage(AlterarFaltasReq)

Matricula = _reflection.GeneratedProtocolMessageType('Matricula', (_message.Message,), {
  'DESCRIPTOR' : _MATRICULA,
  '__module__' : 'proto.rcp_pb2'
  # @@protoc_insertion_point(class_scope:Matricula)
  })
_sym_db.RegisterMessage(Matricula)

InserirMatriculaRes = _reflection.GeneratedProtocolMessageType('InserirMatriculaRes', (_message.Message,), {
  'DESCRIPTOR' : _INSERIRMATRICULARES,
  '__module__' : 'proto.rcp_pb2'
  # @@protoc_insertion_point(class_scope:InserirMatriculaRes)
  })
_sym_db.RegisterMessage(InserirMatriculaRes)

AlunosReq = _reflection.GeneratedProtocolMessageType('AlunosReq', (_message.Message,), {
  'DESCRIPTOR' : _ALUNOSREQ,
  '__module__' : 'proto.rcp_pb2'
  # @@protoc_insertion_point(class_scope:AlunosReq)
  })
_sym_db.RegisterMessage(AlunosReq)

AlunosRes = _reflection.GeneratedProtocolMessageType('AlunosRes', (_message.Message,), {
  'DESCRIPTOR' : _ALUNOSRES,
  '__module__' : 'proto.rcp_pb2'
  # @@protoc_insertion_point(class_scope:AlunosRes)
  })
_sym_db.RegisterMessage(AlunosRes)

Aluno = _reflection.GeneratedProtocolMessageType('Aluno', (_message.Message,), {
  'DESCRIPTOR' : _ALUNO,
  '__module__' : 'proto.rcp_pb2'
  # @@protoc_insertion_point(class_scope:Aluno)
  })
_sym_db.RegisterMessage(Aluno)

_SERVICES = DESCRIPTOR.services_by_name['Services']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\312\002\tApp\\Proto\342\002\025App\\Proto\\GPBMetadata'
  _LISTADISCIPLINA._serialized_start=19
  _LISTADISCIPLINA._serialized_end=92
  _DISCIPLINASREQ._serialized_start=94
  _DISCIPLINASREQ._serialized_end=141
  _DISCIPLINASRES._serialized_start=143
  _DISCIPLINASRES._serialized_end=215
  _MESSAGERES._serialized_start=217
  _MESSAGERES._serialized_end=246
  _ALTERARNOTAREQ._serialized_start=248
  _ALTERARNOTAREQ._serialized_end=314
  _ALTERARFALTASREQ._serialized_start=316
  _ALTERARFALTASREQ._serialized_end=386
  _MATRICULA._serialized_start=388
  _MATRICULA._serialized_end=496
  _INSERIRMATRICULARES._serialized_start=498
  _INSERIRMATRICULARES._serialized_end=567
  _ALUNOSREQ._serialized_start=569
  _ALUNOSREQ._serialized_end=635
  _ALUNOSRES._serialized_start=637
  _ALUNOSRES._serialized_end=689
  _ALUNO._serialized_start=691
  _ALUNO._serialized_end=760
  _SERVICES._serialized_start=763
  _SERVICES._serialized_end=1026
# @@protoc_insertion_point(module_scope)
