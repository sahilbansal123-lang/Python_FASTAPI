from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get('/')
def index():
    return {'data': 'BLOG LIST'}

## here it works fine
@app.get('/blog/unpublished')
def unpublished():  ## defining the type
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):  ## defining the type
    return {'data': id }


## gives error because fast api read line by line
# ## so it reads id first and gives error
# @app.get('/blog/unpublished')
# def unpublished():  ## defining the type
#     return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}/comments')
def commets(id):
    return {'data': {'1', '2'}}  

### MODEL THAT IS CREATED FOR API
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def createBlog(blog: Blog):
    return {'data': f"blog is created with title as {blog.title}"}

