import re
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import datetime


class MemberCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: Optional[str] = None
    role: str = "member"

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value: str):
        value = value.strip()
        if not re.fullmatch(r"^\+?[0-9]+$", value):
            raise ValueError("Phone number must contain only digits and an optional '+' sign")
        return value


class MemberUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    role: Optional[str] = None
    status: Optional[str] = None

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value: Optional[str]):
        if value is None:
            return value
        value = value.strip()
        if not re.fullmatch(r"^\+?[0-9]+$", value):
            raise ValueError("Phone number must contain only digits and an optional '+' sign")
        return value


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