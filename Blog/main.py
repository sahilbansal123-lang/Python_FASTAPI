from fastapi import FastAPI
from . import schema
from . import models
from .database import engine


app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post('/blog')
def create(request: schema.Blog):
    return request

