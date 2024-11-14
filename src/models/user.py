from datetime import datetime

from sqlalchemy import Column, INTEGER, VARCHAR, Boolean, DateTime
from sqlalchemy.orm import relationship

from .base import Base

__all__ = ["User"]


class User(Base):
    __tablename__ = "users"

    id = Column(INTEGER, primary_key=True, nullable=False)
    username = Column(VARCHAR, unique=True, nullable=False)
    first_name = Column(VARCHAR, unique=False, nullable=False)
    last_name = Column(VARCHAR, unique=False, nullable=False)
    email = Column(VARCHAR, nullable=False, unique=True)
    mobile_phone = Column(VARCHAR, nullable=True, default=" ", unique=False)
    hashed_password = Column(VARCHAR, nullable=False)
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now, nullable=False)

    log = relationship(argument="UserLog", back_populates="user", uselist=False)
