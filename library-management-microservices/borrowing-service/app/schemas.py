from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class BorrowingCreate(BaseModel):
    member_id: int
    book_id: int
    borrow_date: date
    due_date: date
    return_date: Optional[date] = None
    status: str = "borrowed"


class BorrowingUpdate(BaseModel):
    member_id: Optional[int] = None
    book_id: Optional[int] = None
    borrow_date: Optional[date] = None
    due_date: Optional[date] = None
    return_date: Optional[date] = None
    status: Optional[str] = None


class BorrowingResponse(BaseModel):
    borrowing_id: int
    member_id: int
    book_id: int
    borrow_date: date
    due_date: date
    return_date: Optional[date] = None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True