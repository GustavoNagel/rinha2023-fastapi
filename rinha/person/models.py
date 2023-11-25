import uuid

from rinha.db.base_class import Base
from sqlalchemy import ARRAY, Column, Date, String
from sqlalchemy.dialects.postgresql import UUID


class Person(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    apelido = Column(String(32), unique=True, index=True)
    nome = Column(String(100))
    nascimento = Column(Date)
    stack = Column(ARRAY(String(32)), nullable=True)
