from fastapi import APIRouter
from fastapi import FastAPI, Depends, status, Response
from fastapi.exceptions import HTTPException
from .. import schema
from .. import models
from ..Hashing import Hash
from ..database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session, relationship
from typing import List
from ..repository import blog
from ..oauth2 import get_current_user


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@router.get('/', response_model=List[schema.showBlog])
def all(
    db: Session = Depends(get_db), 
    current_user: schema.User = Depends(get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(
    request: schema.Blog, 
    db: Session = Depends(get_db),
    current_user: schema.User = Depends(get_current_user)):
    return blog.create_blog(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int, 
    db: Session = Depends(get_db),
    current_user: schema.User = Depends(get_current_user)):
    return blog.delete_blog(id, db)


@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def update(
    id: int, 
    request: schema.Blog, 
    db: Session = Depends(get_db),
    current_user: schema.User = Depends(get_current_user)):
    return blog.update_blog(id, request, db)


@router.get('/{id}', status_code=200, response_model=schema.showBlog)
def read(
    id: int, 
    db: Session = Depends(get_db),
    current_user: schema.User = Depends(get_current_user)):
    return blog.get_byid(id, db)