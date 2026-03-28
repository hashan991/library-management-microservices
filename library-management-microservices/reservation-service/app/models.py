from sqlalchemy import Column, Integer, Date, Enum, TIMESTAMP, text
from app.database import Base


class Reservation(Base):
    __tablename__ = "reservations"

    reservation_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    member_id = Column(Integer, nullable=False)
    book_id = Column(Integer, nullable=False)
    reservation_date = Column(Date, nullable=False)
    status = Column(
        Enum("active", "cancelled", "completed", name="reservation_status"),
        nullable=False,
        server_default="active"
    )
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))