from fastapi import FastAPI
from rinha.config import settings
from rinha.db.database import start_db
from rinha.person.router import person_router


def create_app() -> FastAPI:
    app = FastAPI(
        docs_url=None if settings.ENV == "production" else "/doc",
        redoc_url=None if settings.ENV == "production" else "/redoc",
    )
    app.include_router(person_router)
    start_db()
    return app
