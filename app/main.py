from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
from . import models, schemas, oauth2
from .database import engine
from sqlalchemy.orm import Session
from .routers import posts, users, auth, votes
from .config import BaseSettings

models.Base.metadata.create_all(bind=engine)

# The name of the app is "app"
app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(votes.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"Hello": "Welcome to my API"}