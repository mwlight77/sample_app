from api.app import app
from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)

def test_create_book(client):
    """Test creating a new book."""
    response = client.post(
        "/books",
        json={"title": "Test Book", "author": "Test Author"}
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