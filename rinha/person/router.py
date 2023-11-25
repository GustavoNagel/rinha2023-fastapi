from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from rinha.person import models, schemas
from rinha.db.database import get_db

person_router = APIRouter()


@person_router.get("/hello")
def hello() -> dict[str, str]:
    return {"hello": "world!"}


@person_router.post("/pessoas", response_model=schemas.PersonSchema, status_code=201)
def create_person(
    request: schemas.PersonCreateSchema,
    response: Response,
    db: Session = Depends(get_db),
) -> models.Person:
    db_person = models.Person(**request.model_dump())
    db.add(db_person)
    try:
        db.commit()
    except IntegrityError:
        raise HTTPException(status_code=422, detail="Apelido precisa ser unico")
    db.refresh(db_person)
    response.headers["Location"] = f"/pessoas/{db_person.id}"
    return db_person


@person_router.get("/pessoas/{pessoa_id}", response_model=schemas.PersonSchema)
def get_person(
    pessoa_id: str,
    db: Session = Depends(get_db),
) -> models.Person | None:
    person = db.query(models.Person).get(pessoa_id)
    if not person:
        raise HTTPException(status_code=404, detail='Pessoa nao encontrada!')
    return person


@person_router.get("/pessoas", response_model=list[schemas.PersonSchema])
def list_persons(
    t: str | None = None,
    db: Session = Depends(get_db),
) -> list[models.Person]:
    if not t:
        raise HTTPException(status_code=400, detail='Parametros de busca sao obrigatorios!')
    return db.query(models.Person).filter(
        models.Person.search_field.like(f"%{t}%")
    ).limit(50).all()  # type: ignore


@person_router.get("/contagem-pessoas")
def count_persons(
    t: str | None = None,
    db: Session = Depends(get_db),
) -> int:
    if not t:
        raise HTTPException(status_code=400, detail='Parametros de busca sao obrigatorios!')
    return db.query(models.Person).filter(
        models.Person.search_field.like(f"%{t}%")
    ).count()  # type: ignore
