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


app = FastAPI(title="axa", description="API for axa", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/books")
async def create_book(book: BookRequest, db: Session = Depends(get_db)):
    book_record = Book(**book.model_dump())
    with db.begin():
        db.add(book_record)
        db.commit()
    return HTMLResponse(status_code=201, content="Book created successfully")

@app.get("/books")
async def get_books(db: Session = Depends(get_db)) -> t.List[BookResponse]:
    statement = select(Book)
    results = db.exec(statement).fetchall()
    books = [BookResponse(**x.model_dump()) for x in results]
    return books