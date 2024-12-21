from .. import schema
from .. import models
from ..Hashing import Hash
from sqlalchemy.orm import Session

def create_user(request: schema.User, db: Session):
    new_User = models.user(
        name=request.name, 
        email=request.email, 
        password=Hash.bcrypt
        (request.password))
    db.add(new_User)
    db.commit()
    db.refresh(new_User)
    return new_User

def show_user(id: int, db: Session):
    user = db.query(models.user).filter(models.user.id == id).first()
    if not user:
        return {'detail':f"Blog with the id {id} not existed"}
    return user
