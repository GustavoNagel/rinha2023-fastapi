from datetime import date
from uuid import UUID

from pydantic import BaseModel, Field, validator


class PersonBaseSchema(BaseModel):
    apelido: str = Field(description="Nome pela qual deseja ser chamada", max_length=32)
    nome: str = Field(description="Nome real", max_length=100)
    nascimento: date = Field(description="Data de nascimento")
    stack: list[str] | None = Field(description="Tecnologias que a pessoa domina", default=None)


class PersonCreateSchema(PersonBaseSchema):
    @validator("stack")
    def check_stack(cls, stack: list[str] | None) -> list[str] | None:
        if stack and any(len(technology) > 32 for technology in stack):
            raise ValueError("Nenhuma tecnologia do stack deve ter mais de 32 caracteres")
        return stack


class PersonSchema(PersonBaseSchema):
    id: UUID = Field(description="Chave primaria")

    class Config:
        orm_mode = True
