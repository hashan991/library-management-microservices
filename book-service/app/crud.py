from sqlalchemy.orm import Session
from . import models, schemas

def normalize_status(total_copies: int, available_copies: int, incoming_status: str | None = None) -> str:
    if incoming_status == "Inactive":
        return "Inactive"
    if available_copies == 0:
        return "Out of Stock"
    return "Available"

def get_all_books(db: Session):
    return db.query(models.Book).order_by(models.Book.id.desc()).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_book_by_code(db: Session, book_code: str):
    return db.query(models.Book).filter(models.Book.book_code == book_code).first()

def get_book_by_isbn(db: Session, isbn: str):
    return db.query(models.Book).filter(models.Book.isbn == isbn).first()

def create_book(db: Session, book: schemas.BookCreate):
    data = book.model_dump()

    if data["available_copies"] > data["total_copies"]:
        raise ValueError("Available copies cannot be greater than total copies")

    data["status"] = normalize_status(
        total_copies=data["total_copies"],
        available_copies=data["available_copies"],
        incoming_status=data.get("status")
    )

    db_book = models.Book(**data)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, book_data: schemas.BookUpdate):
    db_book = get_book_by_id(db, book_id)
    if not db_book:
        return None

    update_data = book_data.model_dump(exclude_unset=True)

    new_total = update_data.get("total_copies", db_book.total_copies)
    new_available = update_data.get("available_copies", db_book.available_copies)

    if new_available > new_total:
        raise ValueError("Available copies cannot be greater than total copies")

    for key, value in update_data.items():
        setattr(db_book, key, value)

    db_book.status = normalize_status(
        total_copies=new_total,
        available_copies=new_available,
        incoming_status=update_data.get("status", db_book.status)
    )

    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = get_book_by_id(db, book_id)
    if not db_book:
        return None

    db.delete(db_book)
    db.commit()
    return db_book