import uuid

from rinha.db.base_class import Base
from sqlalchemy import ARRAY, Column, Date, String
from sqlalchemy.dialects.postgresql import UUID


def set_params_together(context):
    params = context.get_current_parameters()
    search_field = params['apelido']
    if params['nome']:
        search_field += f";{params['nome']}"
    if params['stack']:
        search_field += f";{';'.join(params['stack'])}"
    return search_field


class Person(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    apelido = Column(String(32), unique=True, index=True)
    nome = Column(String(100))
    nascimento = Column(Date)
    stack = Column(ARRAY(String(32)), nullable=True)
    search_field = Column(String, default=set_params_together, index=True)
