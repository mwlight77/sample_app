#### Assignment ####
# Please create a simple application with a Python back end.
# The back end should offer a RESTful API endpoint which in turn
# communicates with a database of your choice to persists some
# data received in the RESTful call. We would like to see automated tests,
# input sanitization. Consider error handling and observability.
# Create a local Git repository for this project. We do not expect perfection,
# but would like to see confidence and good practices.
# Please share the code with us only via a GitHub link.


# During our interview: You will walk us through the code, and
# we will ask you follow-up questions, ask you to modify the code
# or add a simple feature (60 minutes). Please make sure you can share
# your screen with where we can see the code in your IDE and the app running.
#### Assignment ####

#### Description ####
# A simple FastAPI application with a RESTful API endpoint.
# The application uses SQLite as the database to persist data.
# The application will be a simple reading list application.

import typing as t

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends
from sqlmodel import Session, select

from api.db import get_db, Book
from api.models import BookRequest, BookResponse
from api.axa_logging import get_axa_logger


app = FastAPI(title="axa", description="API for axa", version="0.1.0")
axa_logger = get_axa_logger()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/books")
async def create_book(book: BookRequest, db: Session = Depends(get_db)):
    """Create a new book record in the database."""
    axa_logger.info(f"Creating a new book: {book.title} by {book.author}")
    try:
        book_record = Book(**book.model_dump())
        with db.begin():
            db.add(book_record)
            db.commit()
        return HTMLResponse(status_code=201, content="Book created successfully")
    except Exception as e:
        axa_logger.error(f"Error creating book: {e}")
        return HTMLResponse(status_code=500, content="Internal Server Error")

@app.get("/books")
async def get_books(db: Session = Depends(get_db)) -> t.List[BookResponse]:
    """Fetch all books from the database"""
    axa_logger.info("Fetching all books from the database")
    try:
        statement = select(Book)
        results = db.exec(statement).fetchall()
        books = [BookResponse(**x.model_dump()) for x in results]
        return books
    except Exception as e:
        axa_logger.error(f"Error fetching books: {e}")
        return HTMLResponse(status_code=500, content="Internal Server Error")
