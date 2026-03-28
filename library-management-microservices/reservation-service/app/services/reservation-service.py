from sqlalchemy.orm import Session
from app import crud, schemas


def create_new_reservation(db: Session, reservation: schemas.ReservationCreate):
    return crud.create_reservation(db, reservation)


def fetch_all_reservations(db: Session):
    return crud.get_all_reservations(db)


def fetch_reservation_by_id(db: Session, reservation_id: int):
    return crud.get_reservation_by_id(db, reservation_id)


def modify_reservation(db: Session, reservation_id: int, reservation_data: schemas.ReservationUpdate):
    return crud.update_reservation(db, reservation_id, reservation_data)


def remove_reservation(db: Session, reservation_id: int):
    return crud.delete_reservation(db, reservation_id)