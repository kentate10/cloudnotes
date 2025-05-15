from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db import Base

# this is the user model, basically the table for storing users
class User(Base):
    __tablename__ = "users"  # this is how the table will be named in the DB

    id = Column(Integer, primary_key=True, index=True)  # unique user id
    email = Column(String, unique=True, index=True, nullable=False)  # has to be unique and not null
    hashed_password = Column(String, nullable=False)  # we store the encrypted password here
    full_name = Column(String)  # optional full name

    # one user can have many notes
    notes = relationship("Note", back_populates="owner")


# this is the note model, every note belongs to a user
class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)  # note title, can't be empty
    content = Column(Text)  # the note content, can be short or long or empty
    timestamp = Column(DateTime, default=datetime.utcnow)  # gets auto-filled when the note is created
    owner_id = Column(Integer, ForeignKey("users.id"))  # the user who owns the note

    # back reference to the user who created this note
    owner = relationship("User", back_populates="notes")
