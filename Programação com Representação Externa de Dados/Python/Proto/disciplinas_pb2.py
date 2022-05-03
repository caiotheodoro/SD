from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class Disciplina(_message.Message):
    __slots__ = ["cod_curso", "codigo", "nome", "professor"]
    CODIGO_FIELD_NUMBER: ClassVar[int]
    COD_CURSO_FIELD_NUMBER: ClassVar[int]
    NOME_FIELD_NUMBER: ClassVar[int]
    PROFESSOR_FIELD_NUMBER: ClassVar[int]
    cod_curso: int
    codigo: str
    nome: str
    professor: str
    def __init__(self, codigo: Optional[str] = ..., nome: Optional[str] = ..., professor: Optional[str] = ..., cod_curso: Optional[int] = ...) -> None: ...
    
class CrudDisciplina(_message.Message):
    __slots__ = ["disciplina", "type"]
    DISCIPLINA_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    disciplina: Disciplina
    type: int
    def __init__(self, type: Optional[int] = ..., disciplina: Optional[Union[Disciplina, Mapping]] = ...) -> None: ...

