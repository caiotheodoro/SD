from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class Matricula(_message.Message):
    __slots__ = ["RA", "ano", "cod_disciplina", "faltas", "nota", "semestre"]
    ANO_FIELD_NUMBER: ClassVar[int]
    COD_DISCIPLINA_FIELD_NUMBER: ClassVar[int]
    FALTAS_FIELD_NUMBER: ClassVar[int]
    NOTA_FIELD_NUMBER: ClassVar[int]
    RA: int
    RA_FIELD_NUMBER: ClassVar[int]
    SEMESTRE_FIELD_NUMBER: ClassVar[int]
    ano: int
    cod_disciplina: str
    faltas: int
    nota: float
    semestre: int
    def __init__(self, RA: Optional[int] = ..., cod_disciplina: Optional[str] = ..., ano: Optional[int] = ..., semestre: Optional[int] = ..., nota: Optional[float] = ..., faltas: Optional[int] = ...) -> None: ...
    
class CrudMatricula(_message.Message):
    __slots__ = ["matricula", "type"]
    MATRICULA_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    matricula: Matricula
    type: int
    def __init__(self, type: Optional[int] = ..., matricula: Optional[Union[Matricula, Mapping]] = ...) -> None: ...

