from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class Aluno(_message.Message):
    __slots__ = ["RA", "cod_curso", "nome", "periodo"]
    COD_CURSO_FIELD_NUMBER: ClassVar[int]
    NOME_FIELD_NUMBER: ClassVar[int]
    PERIODO_FIELD_NUMBER: ClassVar[int]
    RA: int
    RA_FIELD_NUMBER: ClassVar[int]
    cod_curso: int
    nome: str
    periodo: int
    def __init__(self, RA: Optional[int] = ..., nome: Optional[str] = ..., periodo: Optional[int] = ..., cod_curso: Optional[int] = ...) -> None: ...

class CrudAluno(_message.Message):
    __slots__ = ["aluno", "type"]
    ALUNO_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    aluno: Aluno
    type: int
    def __init__(self, type: Optional[int] = ..., aluno: Optional[Union[Aluno, Mapping]] = ...) -> None: ...
