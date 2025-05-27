from api.app import app
from api.db import engine, Book
from fastapi.testclient import TestClient
from sqlmodel import delete, Session
import pytest

TEST_BOOK_NAME = "Test Book"
TEST_BOOK_AUTHOR = "Test Author"

@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)

def test_create_book(client):
    """Test creating a new book."""
    response = client.post(
        "/books",
        json={"title": TEST_BOOK_NAME, "author": TEST_BOOK_AUTHOR}
    )
    assert response.status_code == 201
    assert response.text == "Book created successfully"

def test_get_books(client):
    """Test fetching all books."""
    response = client.get("/books")
    assert response.status_code == 200
    books = response.json()
    assert isinstance(books, list)
    if books:
        assert "id" in books[0]
        assert "title" in books[0]
        assert "author" in books[0]
        assert "dateAdded" in books[0]


def test_cleanup():
    """Cleanup test data after tests.
    In a real application, this would be handled by a fixture or test db."""
    db = Session(engine)
    with db.begin():
        # Clear the database after tests
        statement = delete(Book).where(Book.title == TEST_BOOK_NAME, Book.author == TEST_BOOK_AUTHOR)
        db.exec(statement)
        db.commit()