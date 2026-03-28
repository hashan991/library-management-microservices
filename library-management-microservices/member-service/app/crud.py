from sqlalchemy.orm import Session
from app import models, schemas


def get_all_members(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Member).offset(skip).limit(limit).all()


def get_member_by_id(db: Session, member_id: int):
    return db.query(models.Member).filter(models.Member.member_id == member_id).first()


def get_member_by_email(db: Session, email: str):
    return db.query(models.Member).filter(models.Member.email == email).first()


def create_member(db: Session, member: schemas.MemberCreate):
    db_member = models.Member(
        name=member.name,
        email=member.email,
        phone=member.phone,
        address=member.address,
        role=member.role
    )
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


def update_member(db: Session, member_id: int, member_update: schemas.MemberUpdate):
    db_member = get_member_by_id(db, member_id)

    if not db_member:
        return None

    update_data = member_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_member, key, value)

    db.commit()
    db.refresh(db_member)
    return db_member


def delete_member(db: Session, member_id: int):
    db_member = get_member_by_id(db, member_id)

    if not db_member:
        return None

    db.delete(db_member)
    db.commit()
    return db_member