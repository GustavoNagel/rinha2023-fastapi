from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from rinha.person import models, schemas
from rinha.db.database import get_db

person_router = APIRouter()


@person_router.get("/hello")
def hello() -> dict[str, str]:
    return {"hello": "world!"}


@person_router.post("/pessoas", response_model=schemas.PersonSchema)
def create_person(
    request: schemas.PersonCreateSchema,
    db: Session = Depends(get_db),
) -> models.Person:
    db_person = models.Person(**request.model_dump())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


@person_router.get("/pessoas/{pessoa_id}", response_model=schemas.PersonSchema)
def get_person(
    pessoa_id: str,
    db: Session = Depends(get_db),
) -> models.Person | None:
    return db.query(models.Person).get(models.Person.id == pessoa_id)


@person_router.get("/pessoas", response_model=list[schemas.PersonSchema])
def list_persons(
    t: str | None = None,
    db: Session = Depends(get_db),
) -> list[models.Person]:
    print(t)
    return db.query(models.Person).limit(50).all()  # type: ignore


@person_router.get("/contagem-pessoas")
def count_persons(
    t: str | None = None,
    db: Session = Depends(get_db),
) -> int:
    print(t)
    return db.query(models.Person).count()  # type: ignore
