from pydoc import classname
from typing import Optional
from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validate_titulo(cls, value):
        palavras = len(value.split(' '))
        if palavras < 3:
            raise ValueError('o Título deve ter pelo menos 3 palavras')
        return value
