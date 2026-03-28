import os
from typing import Optional

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import Response
from pydantic import BaseModel, EmailStr

load_dotenv()

BOOK_SERVICE_URL = os.getenv("BOOK_SERVICE_URL")
MEMBER_SERVICE_URL = os.getenv("MEMBER_SERVICE_URL")
BORROWING_SERVICE_URL = os.getenv("BORROWING_SERVICE_URL")
RESERVATION_SERVICE_URL = os.getenv("RESERVATION_SERVICE_URL")

app = FastAPI(
    title="Library Management System - API Gateway",
    description="Single entry point for Book, Member, Borrowing, and Reservation microservices",
    version="1.0.0"
)


# -----------------------------
# Pydantic Models for Swagger
# -----------------------------

class BookCreate(BaseModel):
    title: str
    author: str
    category: str
    isbn: str
    published_year: Optional[int] = None
    available_copies: int = 1
    status: str = "available"


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    category: Optional[str] = None
    isbn: Optional[str] = None
    published_year: Optional[int] = None
    available_copies: Optional[int] = None
    status: Optional[str] = None


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


class BorrowingCreate(BaseModel):
    member_id: int
    book_id: int
    borrow_date: Optional[str] = None
    due_date: Optional[str] = None
    status: str = "borrowed"


class BorrowingUpdate(BaseModel):
    return_date: Optional[str] = None
    status: Optional[str] = None


class ReservationCreate(BaseModel):
    member_id: int
    book_id: int
    reservation_date: Optional[str] = None
    status: str = "active"


class ReservationUpdate(BaseModel):
    status: Optional[str] = None


# -----------------------------
# Common Forward Function
# -----------------------------

async def forward_request(
    service_url: str,
    path: str,
    method: str,
    params: Optional[dict] = None,
    body: Optional[dict] = None
):
    url = f"{service_url}{path}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(
                method=method,
                url=url,
                params=params,
                json=body
            )

            return Response(
                content=response.content,
                status_code=response.status_code,
                media_type=response.headers.get("content-type")
            )

        except httpx.RequestError:
            raise HTTPException(
                status_code=503,
                detail=f"Target service unavailable: {service_url}"
            )


@app.get("/")
async def root():
    return {
        "message": "Library API Gateway is running",
        "docs": "http://127.0.0.1:8000/docs"
    }


# =====================================================
# BOOK SERVICE ROUTES
# =====================================================

@app.get("/books/", tags=["Books"])
async def get_books(
    skip: int = Query(0),
    limit: int = Query(100)
):
    return await forward_request(
        BOOK_SERVICE_URL,
        "/books/",
        "GET",
        params={"skip": skip, "limit": limit}
    )


@app.get("/books/{book_id}", tags=["Books"])
async def get_book(book_id: int):
    return await forward_request(
        BOOK_SERVICE_URL,
        f"/books/{book_id}",
        "GET"
    )


@app.post("/books/", tags=["Books"])
async def create_book(book: BookCreate):
    return await forward_request(
        BOOK_SERVICE_URL,
        "/books/",
        "POST",
        body=book.model_dump()
    )


@app.put("/books/{book_id}", tags=["Books"])
async def update_book(book_id: int, book: BookUpdate):
    return await forward_request(
        BOOK_SERVICE_URL,
        f"/books/{book_id}",
        "PUT",
        body=book.model_dump(exclude_unset=True)
    )


@app.delete("/books/{book_id}", tags=["Books"])
async def delete_book(book_id: int):
    return await forward_request(
        BOOK_SERVICE_URL,
        f"/books/{book_id}",
        "DELETE"
    )


# =====================================================
# MEMBER SERVICE ROUTES
# =====================================================

@app.get("/members/", tags=["Members"])
async def get_members(
    skip: int = Query(0),
    limit: int = Query(100)
):
    return await forward_request(
        MEMBER_SERVICE_URL,
        "/members/",
        "GET",
        params={"skip": skip, "limit": limit}
    )


@app.get("/members/{member_id}", tags=["Members"])
async def get_member(member_id: int):
    return await forward_request(
        MEMBER_SERVICE_URL,
        f"/members/{member_id}",
        "GET"
    )


@app.post("/members/", tags=["Members"])
async def create_member(member: MemberCreate):
    return await forward_request(
        MEMBER_SERVICE_URL,
        "/members/",
        "POST",
        body=member.model_dump()
    )


@app.put("/members/{member_id}", tags=["Members"])
async def update_member(member_id: int, member: MemberUpdate):
    return await forward_request(
        MEMBER_SERVICE_URL,
        f"/members/{member_id}",
        "PUT",
        body=member.model_dump(exclude_unset=True)
    )


@app.delete("/members/{member_id}", tags=["Members"])
async def delete_member(member_id: int):
    return await forward_request(
        MEMBER_SERVICE_URL,
        f"/members/{member_id}",
        "DELETE"
    )


# =====================================================
# BORROWING SERVICE ROUTES
# =====================================================

@app.get("/borrowings/", tags=["Borrowings"])
async def get_borrowings(
    skip: int = Query(0),
    limit: int = Query(100)
):
    return await forward_request(
        BORROWING_SERVICE_URL,
        "/borrowings/",
        "GET",
        params={"skip": skip, "limit": limit}
    )


@app.get("/borrowings/{borrowing_id}", tags=["Borrowings"])
async def get_borrowing(borrowing_id: int):
    return await forward_request(
        BORROWING_SERVICE_URL,
        f"/borrowings/{borrowing_id}",
        "GET"
    )


@app.post("/borrowings/", tags=["Borrowings"])
async def create_borrowing(borrowing: BorrowingCreate):
    return await forward_request(
        BORROWING_SERVICE_URL,
        "/borrowings/",
        "POST",
        body=borrowing.model_dump()
    )


@app.put("/borrowings/{borrowing_id}", tags=["Borrowings"])
async def update_borrowing(borrowing_id: int, borrowing: BorrowingUpdate):
    return await forward_request(
        BORROWING_SERVICE_URL,
        f"/borrowings/{borrowing_id}",
        "PUT",
        body=borrowing.model_dump(exclude_unset=True)
    )


@app.delete("/borrowings/{borrowing_id}", tags=["Borrowings"])
async def delete_borrowing(borrowing_id: int):
    return await forward_request(
        BORROWING_SERVICE_URL,
        f"/borrowings/{borrowing_id}",
        "DELETE"
    )


# =====================================================
# RESERVATION SERVICE ROUTES
# =====================================================

@app.get("/reservations/", tags=["Reservations"])
async def get_reservations(
    skip: int = Query(0),
    limit: int = Query(100)
):
    return await forward_request(
        RESERVATION_SERVICE_URL,
        "/reservations/",
        "GET",
        params={"skip": skip, "limit": limit}
    )


@app.get("/reservations/{reservation_id}", tags=["Reservations"])
async def get_reservation(reservation_id: int):
    return await forward_request(
        RESERVATION_SERVICE_URL,
        f"/reservations/{reservation_id}",
        "GET"
    )


@app.post("/reservations/", tags=["Reservations"])
async def create_reservation(reservation: ReservationCreate):
    return await forward_request(
        RESERVATION_SERVICE_URL,
        "/reservations/",
        "POST",
        body=reservation.model_dump()
    )


@app.put("/reservations/{reservation_id}", tags=["Reservations"])
async def update_reservation(reservation_id: int, reservation: ReservationUpdate):
    return await forward_request(
        RESERVATION_SERVICE_URL,
        f"/reservations/{reservation_id}",
        "PUT",
        body=reservation.model_dump(exclude_unset=True)
    )


@app.delete("/reservations/{reservation_id}", tags=["Reservations"])
async def delete_reservation(reservation_id: int):
    return await forward_request(
        RESERVATION_SERVICE_URL,
        f"/reservations/{reservation_id}",
        "DELETE"
    )