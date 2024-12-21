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


@router.get('/blog', response_model=List[schema.showBlog], tags=['blogs'])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(request: schema.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
def delete(id, db: Session = Depends(get_db)):
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


@router.put('/blog/{id}', status_code= status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id, request: schema.Blog, db: Session = Depends(get_db)):
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


@router.get('/blog/{id}', status_code=200, response_model=schema.showBlog, tags=['blogs'])
def read(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail':f"Blog with the id {id} not existed"}
    return blog
