from pydantic import BaseModel, Field
import typing as t
from datetime import date, datetime

class BookRequest(BaseModel):
    title: str
    author: str
    date_read: t.Optional[date] = None


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    date_added: datetime = Field(..., alias="dateAdded")
    date_read: t.Optional[date] = Field(..., alias="dateRead")

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True