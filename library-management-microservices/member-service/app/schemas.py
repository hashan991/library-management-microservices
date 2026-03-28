from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class MemberCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: Optional[str] = None
    role: str = "member"


class MemberUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    role: Optional[str] = None
    status: Optional[str] = None


class MemberResponse(BaseModel):
    member_id: int
    name: str
    email: EmailStr
    phone: str
    address: Optional[str] = None
    role: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True