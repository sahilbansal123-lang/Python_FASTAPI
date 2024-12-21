from fastapi import APIRouter
from fastapi import FastAPI, Depends, status, Response
from fastapi.exceptions import HTTPException
from .. import schema
from .. import models
from ..Hashing import Hash
from ..database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session, relationship
from typing import List
from ..repository import user

router = APIRouter(
     prefix="/user",
     tags=['User']
)


@router.post('/', response_model=schema.showUser)
def create_user(request: schema.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get('/{id}', response_model=schema.showUser)
def show_User(id: int, db: Session = Depends(get_db)):
    return user.show_user(id, db)

    