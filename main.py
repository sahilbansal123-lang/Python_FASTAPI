from fastapi import FastAPI

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