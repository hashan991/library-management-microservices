from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, text
from app.database import Base


class Member(Base):
    __tablename__ = "members"

    member_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15), nullable=False)
    address = Column(String(255), nullable=True)
    role = Column(Enum("admin", "staff", "member", name="member_roles"), nullable=False, server_default="member")
    status = Column(Enum("active", "inactive", name="member_status"), nullable=False, server_default="active")
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))