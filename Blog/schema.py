from pydantic import BaseModel

## Creating api request for data
class Blog(BaseModel):
    title:str
    body:str


class showBlog(BaseModel):
    title: str
    body: str
    class Config():
        orm_mode= True
