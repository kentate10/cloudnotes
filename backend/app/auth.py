# we import these to help us build the JWT token
from datetime import datetime, timedelta  # datetime: current time | timedelta: add/subtract time
from jose import JWTError, jwt  # jose is a lib to create and decode JWTs safely
from fastapi import Depends, HTTPException, status  # tools for handling security and errors
from fastapi.security import OAuth2PasswordBearer  # lets us extract token from requests
from sqlalchemy.orm import Session  # to talk to the database
from app import models, db, crud  # bring in your database models, connection and logic


# this is the secret used to sign the tokens
# IMPORTANT: don't share this key, and store it in an .env file in real apps
SECRET_KEY = "supersecretkeyjustforcloudnotes"

# this is the algorithm used to encrypt/decrypt the JWT
# HS256 is standard and works great for most cases
ALGORITHM = "HS256"

# how long the token stays valid (in minutes)
# here we say: "token lasts for 1 hour"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


# FastAPI built-in tool to extract tokens from requests
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# creates a JWT token from the user data (usually just the user ID)
def create_access_token(data: dict, expires_delta: timedelta = None):
    # make a copy of the data so we don't change the original
    to_encode = data.copy()

    # calculate when the token should expire
    # if no time is passed, we use the default (60 minutes)
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))

    # add the expiration time to the token payload
    to_encode.update({"exp": expire})

    # use the SECRET_KEY and ALGORITHM to create the actual JWT
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    # return the final token as a string
    return encoded_jwt


#No entendi un carajao como funciona este get curren user pero funciona 

# this gets called in protected routes to find out who's the current user
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(db.SessionLocal)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token or credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise credentials_exception

    return user
