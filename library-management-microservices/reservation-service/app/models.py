from sqlalchemy import Column, Integer, String, Date
from app.database import Base


class Reservation(Base):
    __tablename__ = "reservations"

    reservation_id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, nullable=False)
    book_id = Column(Integer, nullable=False)
    reservation_date = Column(Date, nullable=False)
    status = Column(String, default="PENDING", nullable=False)
    expiry_date = Column(Date, nullable=False)