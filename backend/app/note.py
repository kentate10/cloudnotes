# FastAPI imports to define routes and handle security and errors
from fastapi import APIRouter, Depends, HTTPException, status

# SQLAlchemy session to access the DB
from sqlalchemy.orm import Session

# used to define that a response is a list of notes
from typing import List

# bring in our project files: schemas for validation, crud for DB logic, auth for JWT
from app import schemas, crud, auth, db

# bring in the User model so FastAPI knows what type current_user is
from app.models import User

# this creates a mini-router just for notes
router = APIRouter(
    prefix="/notes",       # all routes here will start with /notes
    tags=["notes"]         # used to organize routes in Swagger docs (/docs)
)
#siguiente: hacexgr funcion para crear un note   