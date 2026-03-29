from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, crud

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=list[schemas.BookResponse])
def list_books(db: Session = Depends(get_db)):
    return crud.get_all_books(db)

@router.get("/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    existing_code = crud.get_book_by_code(db, book.book_code)
    if existing_code:
        raise HTTPException(status_code=400, detail="Book code already exists")

    if book.isbn:
        existing_isbn = crud.get_book_by_isbn(db, book.isbn)
        if existing_isbn:
            raise HTTPException(status_code=400, detail="ISBN already exists")

    try:
        return crud.create_book(db, book)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_id(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book.book_code and book.book_code != db_book.book_code:
        if crud.get_book_by_code(db, book.book_code):
            raise HTTPException(status_code=400, detail="Book code already exists")

    if book.isbn and book.isbn != db_book.isbn:
        if crud.get_book_by_isbn(db, book.isbn):
            raise HTTPException(status_code=400, detail="ISBN already exists")

    try:
        updated = crud.update_book(db, book_id, book)
        return updated
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_book(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}