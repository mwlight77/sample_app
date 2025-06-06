from pydantic import BaseModel, Field, ConfigDict
import typing as t
from datetime import date, datetime

class BookRequest(BaseModel):
    """Model for creating a new book request."""
    title: str = Field(..., min_length=5, max_length=100)
    author: str = Field(..., min_length=5, max_length=100)


class BookResponse(BaseModel):
    """Model for returning book details."""
    id: int
    title: str
    author: str
    date_added: datetime = Field(..., alias="dateAdded")

    model_config = ConfigDict(
        populate_by_name=True
    )
