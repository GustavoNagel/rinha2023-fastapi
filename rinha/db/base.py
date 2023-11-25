from .base_class import Base  # noqa F401
# Import all the models, so that Base has them before being
# imported by Alembic
from rinha.person.models import Person  # noqa F401
