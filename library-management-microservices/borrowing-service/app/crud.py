from sqlalchemy.orm import Session
from app import models, schemas


def get_all_borrowings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Borrowing).offset(skip).limit(limit).all()


def get_borrowing_by_id(db: Session, borrowing_id: int):
    return db.query(models.Borrowing).filter(models.Borrowing.borrowing_id == borrowing_id).first()


def create_borrowing(db: Session, borrowing: schemas.BorrowingCreate):
    db_borrowing = models.Borrowing(
        member_id=borrowing.member_id,
        book_id=borrowing.book_id,
        borrow_date=borrowing.borrow_date,
        due_date=borrowing.due_date,
        return_date=borrowing.return_date,
        status=borrowing.status
    )
    db.add(db_borrowing)
    db.commit()
    db.refresh(db_borrowing)
    return db_borrowing


def update_borrowing(db: Session, borrowing_id: int, borrowing_update: schemas.BorrowingUpdate):
    db_borrowing = get_borrowing_by_id(db, borrowing_id)

    if not db_borrowing:
        return None

    update_data = borrowing_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_borrowing, key, value)

    db.commit()
    db.refresh(db_borrowing)
    return db_borrowing


def delete_borrowing(db: Session, borrowing_id: int):
    db_borrowing = get_borrowing_by_id(db, borrowing_id)

    if not db_borrowing:
        return None

    db.delete(db_borrowing)
    db.commit()
    return db_borrowing