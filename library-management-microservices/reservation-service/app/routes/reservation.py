from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app import schemas
from app.services.reservation_service import (
    get_all_reservations_service,
    get_reservation_by_id_service,
    create_reservation_service,
    update_reservation_service,
    delete_reservation_service
)

router = APIRouter()


@router.get("/", response_model=List[schemas.ReservationResponse])
def get_reservations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_reservations_service(db=db, skip=skip, limit=limit)


@router.get("/{reservation_id}", response_model=schemas.ReservationResponse)
def get_reservation(reservation_id: int, db: Session = Depends(get_db)):
    return get_reservation_by_id_service(db=db, reservation_id=reservation_id)


@router.post("/", response_model=schemas.ReservationResponse, status_code=status.HTTP_201_CREATED)
def create_reservation(reservation: schemas.ReservationCreate, db: Session = Depends(get_db)):
    return create_reservation_service(db=db, reservation=reservation)


@router.put("/{reservation_id}", response_model=schemas.ReservationResponse)
def update_reservation(
    reservation_id: int,
    reservation_update: schemas.ReservationUpdate,
    db: Session = Depends(get_db)
):
    return update_reservation_service(
        db=db,
        reservation_id=reservation_id,
        reservation_update=reservation_update
    )


@router.delete("/{reservation_id}")
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    return delete_reservation_service(db=db, reservation_id=reservation_id)