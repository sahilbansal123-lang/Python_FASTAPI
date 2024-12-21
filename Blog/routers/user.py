from fastapi import APIRouter
from fastapi import FastAPI, Depends, status, Response
from fastapi.exceptions import HTTPException
from .. import schema
from .. import models
from ..Hashing import Hash
from ..database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session, relationship
from typing import List

router = APIRouter()


@router.post('/user', response_model=schema.showUser, tags=['User'])
def create_user(request: schema.User, db: Session = Depends(get_db)):
    new_User = models.user(
        name=request.name, 
        email=request.email, 
        password=Hash.bcrypt
        (request.password))
    db.add(new_User)
    db.commit()
    db.refresh(new_User)
    return new_User

@router.get('/user/{id}', response_model=schema.showUser, tags=['User'])
def show_User(id, response: Response, db: Session = Depends(get_db)):
    user = db.query(models.user).filter(models.user.id == id).first()
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail':f"Blog with the id {id} not existed"}
    return user

    