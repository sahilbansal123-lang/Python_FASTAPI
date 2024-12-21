from pydantic import BaseModel
from typing import List

## Creating api request for data
class Blog(BaseModel):
    title:str
    body:str

    class Config():
        orm_mode= True

class User(BaseModel):
    name: str
    email: str
    password: str

class showUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]

    class Config():
        orm_mode= True


class showBlog(BaseModel):
    title: str
    body: str
    creator: showUser

    class Config():
        orm_mode= True

class login(BaseModel):
    username: str
    password: str

    class Config():
        orm_mode= True
