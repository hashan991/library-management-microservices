from typing import Optional, Literal
from pydantic import BaseModel, Field

BookStatus = Literal["Available", "Out of Stock", "Inactive"]

class BookBase(BaseModel):
    book_code: str = Field(..., min_length=2, max_length=50)
    title: str = Field(..., min_length=2, max_length=200)
    author: str = Field(..., min_length=2, max_length=150)
    category: Optional[str] = Field(None, max_length=100)
    publisher: Optional[str] = Field(None, max_length=150)
    published_year: Optional[int] = Field(None, ge=1000, le=2100)
    isbn: Optional[str] = Field(None, max_length=50)
    total_copies: int = Field(..., ge=1)
    available_copies: int = Field(..., ge=0)
    shelf_location: Optional[str] = Field(None, max_length=100)
    status: BookStatus = "Available"

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    book_code: Optional[str] = Field(None, min_length=2, max_length=50)
    title: Optional[str] = Field(None, min_length=2, max_length=200)
    author: Optional[str] = Field(None, min_length=2, max_length=150)
    category: Optional[str] = Field(None, max_length=100)
    publisher: Optional[str] = Field(None, max_length=150)
    published_year: Optional[int] = Field(None, ge=1000, le=2100)
    isbn: Optional[str] = Field(None, max_length=50)
    total_copies: Optional[int] = Field(None, ge=1)
    available_copies: Optional[int] = Field(None, ge=0)
    shelf_location: Optional[str] = Field(None, max_length=100)
    status: Optional[BookStatus] = None

class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True