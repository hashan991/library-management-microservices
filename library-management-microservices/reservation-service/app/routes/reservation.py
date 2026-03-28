from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas
from app.services import reservation_service

router = APIRouter(prefix="/reservations", tags=["Reservations"])


@router.post("/", response_model=schemas.ReservationResponse)
def create_reservation(reservation: schemas.ReservationCreate, db: Session = Depends(get_db)):
    return reservation_service.create_new_reservation(db, reservation)


@router.get("/", response_model=list[schemas.ReservationResponse])
def get_all_reservations(db: Session = Depends(get_db)):
    return reservation_service.fetch_all_reservations(db)


@router.get("/{reservation_id}", response_model=schemas.ReservationResponse)
def get_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation = reservation_service.fetch_reservation_by_id(db, reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation


@router.put("/{reservation_id}", response_model=schemas.ReservationResponse)
def update_reservation(reservation_id: int, reservation_data: schemas.ReservationUpdate, db: Session = Depends(get_db)):
    updated_reservation = reservation_service.modify_reservation(db, reservation_id, reservation_data)
    if not updated_reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return updated_reservation


@router.delete("/{reservation_id}")
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    deleted_reservation = reservation_service.remove_reservation(db, reservation_id)
    if not deleted_reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return {"message": "Reservation deleted successfully"}