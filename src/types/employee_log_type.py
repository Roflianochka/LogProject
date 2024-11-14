from typing import Optional
from pydantic import PositiveInt, Field, BaseModel
from datetime import date, time, datetime
from datetime import  date as _date

def current_time() -> time:
    return datetime.now().time()
def current_date() -> date:
    return datetime.now().date()

__all__ = [ "UserLogCreateDTO", "UserLogUpdateDTO", "UserLogBaseDTO"]

class UserLogBaseDTO(BaseModel):
    id: PositiveInt = Field(
        default=...,
        title="ID of entry in employeeLog Table ",
        examples=[1]
    )
    date: _date = Field(
        default=...,
        title="Date when employee came to workplace",
        examples=["2024-09-18"]
    )
    log_in_time: Optional[time] = Field(
        default=None,
        title="Time when employee came to workplace",
        examples=["14:30:00"]
    )
    log_out_time: Optional[time] = Field(
        default=None,
        title="Time when employee leave the workplace",
        examples=["19:30:00"]
    )

class UserLogCreateDTO(BaseModel):
    id: PositiveInt = Field(
        default=...,
        title="ID of entry in employeeLog Table ",
        examples=[1]
    )
    user_id: PositiveInt = Field(
        default=...,
        title="ID of the Employee",
        examples=[1]
    )
    date: _date = Field(
        default_factory=current_date,
        title="Date when employee came to workplace",
    )
    log_in_time: time = Field(
        default_factory=current_time,
        title="Time when employee came to workplace",
    )
    log_out_time: Optional[time] = Field(
        default=None,
        title="Time when employee leave the workplace",
        examples=["00:00:00"]
    )


class UserLogUpdateDTO(BaseModel):
    log_out_time: time = Field(
        default_factory=current_time,
        title="Time when employee leave the workplace",
        examples=["19:30:00"]
    )
