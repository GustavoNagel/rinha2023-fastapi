from typing import Generator

import logging

from rinha.db.base import Base
from rinha.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

logger = logging.getLogger(__name__)
engine = create_engine(settings.DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        logger.info('URI:', settings.DATABASE_URI, settings.SECRET_KEY)
        db = SessionLocal()
        yield db
    finally:
        db.close()


def start_db():
    """Temporary method to start db."""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
