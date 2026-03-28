from sqlalchemy.orm import Session
from app import models, schemas


def get_all_reservations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Reservation).offset(skip).limit(limit).all()


def get_reservation_by_id(db: Session, reservation_id: int):
    return (
        db.query(models.Reservation)
        .filter(models.Reservation.reservation_id == reservation_id)
        .first()
    )


def create_reservation(db: Session, reservation: schemas.ReservationCreate):
    db_reservation = models.Reservation(
        member_id=reservation.member_id,
        book_id=reservation.book_id,
        reservation_date=reservation.reservation_date,
        status=reservation.status
    )
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation


def update_reservation(
    db: Session,
    reservation_id: int,
    reservation_update: schemas.ReservationUpdate
):
    db_reservation = get_reservation_by_id(db, reservation_id)

    if not db_reservation:
        return None

    update_data = reservation_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_reservation, key, value)

    db.commit()
    db.refresh(db_reservation)
    return db_reservation


def delete_reservation(db: Session, reservation_id: int):
    db_reservation = get_reservation_by_id(db, reservation_id)

    if not db_reservation:
        return None

    db.delete(db_reservation)
    db.commit()
    return db_reservation