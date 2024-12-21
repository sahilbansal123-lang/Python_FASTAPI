from fastapi import APIRouter
from fastapi import FastAPI, Depends, status, Response
from fastapi.exceptions import HTTPException
from .. import schema
from .. import models
from ..Hashing import Hash
from ..database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session, relationship
from typing import List


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def get_byid(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        return {'detail':f"Blog with the id {id} not existed"}
    return blog


def create_blog(request: schema.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete_blog(id: int, db: Session):
    ## below line is used for filtering or searchin the blog with specific id
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
       raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return {'detail':f"Blog with id {id} deleted Sucessfully"}


def update_blog(id: int, request: schema.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
       raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    blog.update( 
        {"title": request.title, "body": request.body},
        synchronize_session=False
        )
    db.commit()
    return 'Updated sucessfully'