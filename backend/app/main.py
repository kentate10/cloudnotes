# 
from app.routers import user
app.include_router(user.router) # Import the user router from the routers module

# Import FastAPI to create the web API
from fastapi import FastAPI

# Import the Base class and engine from db.py
# Base is used to define database models, and engine connects to the database
from app.db import Base, engine

# Import the models so SQLAlchemy can register them and create the tables
import app.models

# This creates all tables in the database based on the models you've defined
# If the database file doesn't exist, it will be created automatically (dev only)
Base.metadata.create_all(bind=engine)

# Create the FastAPI app instance
app = FastAPI()

# Define a GET route at the root path "/"
# When someone visits http://localhost:8000/, this function will run
@app.get("/")
def root():
    # Returns a JSON response
    return {"message": "CloudNotes is up and running!"}
