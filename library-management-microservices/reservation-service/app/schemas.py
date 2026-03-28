from datetime import date
from pydantic import BaseModel, Field


class ReservationBase(BaseModel):
    member_id: int = Field(..., example=101)
    book_id: int = Field(..., example=5001)
    reservation_date: date = Field(..., example="2026-03-28")
    expiry_date: date = Field(..., example="2026-04-02")


class ReservationCreate(ReservationBase):
    pass


class ReservationUpdate(BaseModel):
    member_id: int | None = None
    book_id: int | None = None
    reservation_date: date | None = None
    expiry_date: date | None = None
    status: str | None = None


class ReservationResponse(ReservationBase):
    reservation_id: int
    status: str

    class Config:
        from_attributes = True