from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas


def get_all_members_service(db: Session, skip: int = 0, limit: int = 100):
    return crud.get_all_members(db=db, skip=skip, limit=limit)


def get_member_by_id_service(db: Session, member_id: int):
    member = crud.get_member_by_id(db=db, member_id=member_id)
    if not member:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Member not found"
        )
    return member


def create_member_service(db: Session, member: schemas.MemberCreate):
    existing_member = crud.get_member_by_email(db=db, email=member.email)
    if existing_member:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    return crud.create_member(db=db, member=member)


def update_member_service(db: Session, member_id: int, member_update: schemas.MemberUpdate):
    existing_member = crud.get_member_by_id(db=db, member_id=member_id)
    if not existing_member:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Member not found"
        )

    if member_update.email:
        member_with_email = crud.get_member_by_email(db=db, email=member_update.email)
        if member_with_email and member_with_email.member_id != member_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

    return crud.update_member(db=db, member_id=member_id, member_update=member_update)


def delete_member_service(db: Session, member_id: int):
    deleted_member = crud.delete_member(db=db, member_id=member_id)
    if not deleted_member:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Member not found"
        )

    return {"message": "Member deleted successfully"}