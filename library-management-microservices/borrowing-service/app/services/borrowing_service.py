from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas


def get_all_borrowings_service(db: Session, skip: int = 0, limit: int = 100):
    return crud.get_all_borrowings(db=db, skip=skip, limit=limit)


def get_borrowing_by_id_service(db: Session, borrowing_id: int):
    borrowing = crud.get_borrowing_by_id(db=db, borrowing_id=borrowing_id)
    if not borrowing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Borrowing record not found"
        )
    return borrowing


def create_borrowing_service(db: Session, borrowing: schemas.BorrowingCreate):
    return crud.create_borrowing(db=db, borrowing=borrowing)


def update_borrowing_service(db: Session, borrowing_id: int, borrowing_update: schemas.BorrowingUpdate):
    existing_borrowing = crud.get_borrowing_by_id(db=db, borrowing_id=borrowing_id)
    if not existing_borrowing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Borrowing record not found"
        )

    return crud.update_borrowing(db=db, borrowing_id=borrowing_id, borrowing_update=borrowing_update)


def delete_borrowing_service(db: Session, borrowing_id: int):
    deleted_borrowing = crud.delete_borrowing(db=db, borrowing_id=borrowing_id)
    if not deleted_borrowing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Borrowing record not found"
        )

    return {"message": "Borrowing record deleted successfully"}