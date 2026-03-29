from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.crud import (
    get_all_reservations,
    get_reservation_by_id,
    create_reservation,
    update_reservation,
    delete_reservation
)
from app import schemas


def get_all_reservations_service(db: Session, skip: int = 0, limit: int = 100):
    return get_all_reservations(db=db, skip=skip, limit=limit)


def get_reservation_by_id_service(db: Session, reservation_id: int):
    reservation = get_reservation_by_id(db=db, reservation_id=reservation_id)
    if not reservation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reservation not found"
        )
    return reservation


def create_reservation_service(db: Session, reservation: schemas.ReservationCreate):
    return create_reservation(db=db, reservation=reservation)


def update_reservation_service(
    db: Session,
    reservation_id: int,
    reservation_update: schemas.ReservationUpdate
):
    reservation = update_reservation(
        db=db,
        reservation_id=reservation_id,
        reservation_update=reservation_update
    )

    if not reservation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reservation not found"
        )
    return reservation


def delete_reservation_service(db: Session, reservation_id: int):
    reservation = delete_reservation(db=db, reservation_id=reservation_id)

    if not reservation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reservation not found"
        )
    return {"message": "Reservation deleted successfully"}