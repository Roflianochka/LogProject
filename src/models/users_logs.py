from sqlalchemy import Column, INTEGER, ForeignKey, Time, func, Date
from sqlalchemy.orm import relationship

from .base import Base

__all__ = [
    'UserLog'
]

class UserLog(Base):
    __tablename__ = 'employee_logs'
    id = Column(INTEGER, primary_key=True)
    user_id = Column(
        INTEGER,
        ForeignKey('users.id'),
        nullable=False,
        index=True,
        unique=True
    )
    date = Column(Date, default=func.now())
    log_in_time = Column(Time, nullable=True, unique=True)
    log_out_time = Column(Time, nullable=True, unique=True)

    user = relationship(argument='User', back_populates='log')
