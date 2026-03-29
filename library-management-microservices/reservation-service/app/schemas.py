from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date


class ReservationCreate(BaseModel):
    member_id: int
    book_id: int
    reservation_date: date
    status: str = "active"


class ReservationUpdate(BaseModel):
    member_id: Optional[int] = None
    book_id: Optional[int] = None
    reservation_date: Optional[date] = None
    status: Optional[str] = None


class ReservationResponse(BaseModel):
    reservation_id: int
    member_id: int
    book_id: int
    reservation_date: date
    status: str
    created_at: datetime

    class Config:
        from_attributes = True