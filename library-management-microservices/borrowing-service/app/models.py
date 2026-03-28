from sqlalchemy import Column, Integer, String, Date, Enum, TIMESTAMP, text
from app.database import Base


class Borrowing(Base):
    __tablename__ = "borrowings"

    borrowing_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    member_id = Column(Integer, nullable=False)
    book_id = Column(Integer, nullable=False)
    borrow_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)
    status = Column(
        Enum("borrowed", "returned", "overdue", name="borrowing_status"),
        nullable=False,
        server_default="borrowed"
    )
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))