import sqlite3
from sqlmodel import SQLModel, Field, create_engine, Session, func, DATETIME, DATE, Column
import typing as t
from datetime import datetime, date


# Database connection
DATABASE_URL = "sqlite:///./readingList.db"

engine = create_engine(DATABASE_URL)

# Define Tables
class Book(SQLModel, table=True):
    __tablename__ = "books"
    id: int = Field(default=None, primary_key=True)
    date_added: datetime = Field(sa_column=Column(DATETIME, default=func.now()))
    title: str
    author: str

# Create the database tables
SQLModel.metadata.create_all(engine)

# Create a database session
def get_db():
    """Provides a database session for dependency injection."""
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
