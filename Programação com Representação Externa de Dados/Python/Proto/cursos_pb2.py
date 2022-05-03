from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class Curso(_message.Message):
    __slots__ = ["codigo", "nome"]
    CODIGO_FIELD_NUMBER: ClassVar[int]
    NOME_FIELD_NUMBER: ClassVar[int]
    codigo: str
    nome: str
    def __init__(self, codigo: Optional[str] = ..., nome: Optional[str] = ...) -> None: ...
    
class CrudCurso(_message.Message):
    __slots__ = ["curso", "type"]
    CURSO_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    curso: Curso
    type: int
    def __init__(self, type: Optional[int] = ..., curso: Optional[Union[Curso, Mapping]] = ...) -> None: ...

