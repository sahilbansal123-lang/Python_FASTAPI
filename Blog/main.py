from fastapi import FastAPI, Depends, status, Response
from fastapi.exceptions import HTTPException
from . import schema
from . import models
from .Hashing import Hash
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List




app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schema.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
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



@app.put('/blog/{id}', status_code= status.HTTP_202_ACCEPTED)
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



@app.get('/blog', response_model=List[schema.showBlog])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs



@app.get('/blog/{id}', status_code=200, response_model=schema.showBlog)
def read(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail':f"Blog with the id {id} not existed"}
    return blog



@app.post('/user', response_model=schema.showUser)
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

@app.get('/user/{id}', response_model=schema.showUser)
def show_User(id, response: Response, db: Session = Depends(get_db)):
    user = db.query(models.user).filter(models.user.id == id).first()
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail':f"Blog with the id {id} not existed"}
    return user

    