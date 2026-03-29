from sqlalchemy import Column, Integer, String
from .database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    book_code = Column(String(50), unique=True, index=True, nullable=False)
    title = Column(String(200), nullable=False)
    author = Column(String(150), nullable=False)
    category = Column(String(100), nullable=True)
    publisher = Column(String(150), nullable=True)
    published_year = Column(Integer, nullable=True)
    isbn = Column(String(50), unique=True, nullable=True)
    total_copies = Column(Integer, nullable=False, default=1)
    available_copies = Column(Integer, nullable=False, default=1)
    shelf_location = Column(String(100), nullable=True)
    status = Column(String(50), nullable=False, default="Available")