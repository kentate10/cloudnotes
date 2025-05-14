from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

# this is what we expect when someone wants to register
class UserCreate(BaseModel):
    email: EmailStr  # makes sure it's a valid email
    password: str
    full_name: str

# this is what we return when we send user data (we never send the password)
class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str

    class Config:
        orm_mode = True  # needed so we can return SQLAlchemy models as JSON


# for creating a new note
class NoteCreate(BaseModel):
    title: str
    content: Optional[str] = None  # content can be empty


# this is what we return when showing a note
class NoteOut(BaseModel):
    id: int
    title: str
    content: Optional[str] = None
    timestamp: datetime
    owner_id: int

    class Config:
        orm_mode = True


# if we want to return a user with their notes included
class UserWithNotes(UserOut):
    notes: List[NoteOut] = []  # list of notes this user owns
