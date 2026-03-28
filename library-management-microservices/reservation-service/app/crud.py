from sqlalchemy.orm import Session
from app import models, schemas


def create_reservation(db: Session, reservation: schemas.ReservationCreate):
    db_reservation = models.Reservation(
        member_id=reservation.member_id,
        book_id=reservation.book_id,
        reservation_date=reservation.reservation_date,
        expiry_date=reservation.expiry_date,
        status="PENDING"
    )
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation


def get_all_reservations(db: Session):
    return db.query(models.Reservation).all()


def get_reservation_by_id(db: Session, reservation_id: int):
    return (
        db.query(models.Reservation)
        .filter(models.Reservation.reservation_id == reservation_id)
        .first()
    )


def update_reservation(db: Session, reservation_id: int, reservation_data: schemas.ReservationUpdate):
    db_reservation = get_reservation_by_id(db, reservation_id)

    if not db_reservation:
        return None

    if reservation_data.member_id is not None:
        db_reservation.member_id = reservation_data.member_id
    if reservation_data.book_id is not None:
        db_reservation.book_id = reservation_data.book_id
    if reservation_data.reservation_date is not None:
        db_reservation.reservation_date = reservation_data.reservation_date
    if reservation_data.expiry_date is not None:
        db_reservation.expiry_date = reservation_data.expiry_date
    if reservation_data.status is not None:
        db_reservation.status = reservation_data.status

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