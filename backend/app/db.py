# Import required SQLAlchemy components
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL for SQLite (file-based database stored locally)
# "./cloudnotes.db" means the database file will be created in the current directory
#SQLALCHEMY_DATABASE_URL = "sqlite:///./cloudnotes.db"

# If you later switch to PostgreSQL, the format would be:
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:NkfenagaBLJzoOZIXMxKoaPGtThyiele@crossover.proxy.rlwy.net:33410/railway"

# Create the SQLAlchemy engine (connects to the database)
# The 'check_same_thread=False' option is required for SQLite when using multiple threads (like in FastAPI)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a session factory that will be used to interact with the database
# autocommit=False → you control when to commit
# autoflush=False → changes are flushed manually
# bind=engine → it connects to the database defined above
SessionLocal = sessionmaker
