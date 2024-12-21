from fastapi import APIRouter
from fastapi import FastAPI, Depends, status, Response
from fastapi.exceptions import HTTPException
from .. import schema
from .. import models
from ..Hashing import Hash
from ..database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session, relationship
from typing import List
from ..repository import user
from datetime import datetime, timedelta, timezone
from ..JWTtoken import create_access_token



router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(
    request: schema.login, 
    db: Session = Depends(get_db)
    ):
    user = db.query(models.user).filter(models.user.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid Credentials"
        )
    if not Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Incorrect Password"
        )
    
    # generate JWT TOKEN AND RETURN IT

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}