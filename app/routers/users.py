from .. import utils, schemas, models
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=['user']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user:schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}')
def get_user(id: int, db: Session = Depends(get_db), ):
    gotuser = db.query(models.User).filter(models.User.id == id).first()
    if not gotuser:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exist")
    
    return gotuser