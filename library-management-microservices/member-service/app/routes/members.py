from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app import schemas
from app.services.member_service import (
    get_all_members_service,
    get_member_by_id_service,
    create_member_service,
    update_member_service,
    delete_member_service
)

router = APIRouter()


@router.get("/", response_model=List[schemas.MemberResponse])
def get_members(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_members_service(db=db, skip=skip, limit=limit)


@router.get("/{member_id}", response_model=schemas.MemberResponse)
def get_member(member_id: int, db: Session = Depends(get_db)):
    return get_member_by_id_service(db=db, member_id=member_id)


@router.post("/", response_model=schemas.MemberResponse, status_code=status.HTTP_201_CREATED)
def create_member(member: schemas.MemberCreate, db: Session = Depends(get_db)):
    return create_member_service(db=db, member=member)


@router.put("/{member_id}", response_model=schemas.MemberResponse)
def update_member(member_id: int, member_update: schemas.MemberUpdate, db: Session = Depends(get_db)):
    return update_member_service(db=db, member_id=member_id, member_update=member_update)


@router.delete("/{member_id}")
def delete_member(member_id: int, db: Session = Depends(get_db)):
    return delete_member_service(db=db, member_id=member_id)