from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app import schemas
from app.services.borrowing_service import (
    get_all_borrowings_service,
    get_borrowing_by_id_service,
    create_borrowing_service,
    update_borrowing_service,
    delete_borrowing_service
)

router = APIRouter()


@router.get("/", response_model=List[schemas.BorrowingResponse])
def get_borrowings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_borrowings_service(db=db, skip=skip, limit=limit)


@router.get("/{borrowing_id}", response_model=schemas.BorrowingResponse)
def get_borrowing(borrowing_id: int, db: Session = Depends(get_db)):
    return get_borrowing_by_id_service(db=db, borrowing_id=borrowing_id)


@router.post("/", response_model=schemas.BorrowingResponse, status_code=status.HTTP_201_CREATED)
def create_borrowing(borrowing: schemas.BorrowingCreate, db: Session = Depends(get_db)):
    return create_borrowing_service(db=db, borrowing=borrowing)


@router.put("/{borrowing_id}", response_model=schemas.BorrowingResponse)
def update_borrowing(borrowing_id: int, borrowing_update: schemas.BorrowingUpdate, db: Session = Depends(get_db)):
    return update_borrowing_service(db=db, borrowing_id=borrowing_id, borrowing_update=borrowing_update)


@router.delete("/{borrowing_id}")
def delete_borrowing(borrowing_id: int, db: Session = Depends(get_db)):
    return delete_borrowing_service(db=db, borrowing_id=borrowing_id)