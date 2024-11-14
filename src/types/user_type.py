from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, EmailStr, PositiveInt

__all__ = [
    "UserBaseDTO", "UserCreateDTO", "UserUpdateDTO"
]


class UserBaseDTO(BaseModel):
    id: PositiveInt = Field(
        default=...,
        title="UserID",
        description="Positive integer representing user ID",
        examples=[1]
    )
    username: str = Field(
        default=...,
        title="User username",
        description="User's username",
        examples=["Roflianochka"]
    )
    first_name: str = Field(
        default=...,
        title="User name",
        description="User's name",
        examples=["Maxim"]
    )
    last_name: str = Field(
        default=...,
        title="User last name",
        description="User's last name",
        examples=["Belyaev"]
    )
    email: EmailStr = Field(
        default=...,
        title="UserEmail",
        description="Email address of the user",
        examples=["user@example.com"]
    )
    mobile_phone: str = Field(
        default=...,
        title="UserPhone",
        description="",
        examples=["+375545254125"]
    )
    hashed_password: str = Field(
        default=...,
        title="UserPassword",
        description="Hashed password of the user",
        examples=["hashed_password"]
    )
    is_active: bool = Field(
        default=True,
        title="IsActive",
        description="Indicates whether the user is active",
        examples=[True, False]
    )
    created_at: datetime = Field(
        default_factory=datetime.now,
        title="CreatedAt",
        description="Timestamp when the user was created"
    )

class UserCreateDTO(BaseModel):
    id: PositiveInt = Field(
        default=...,
        title="UserID",
        description="Positive integer representing user ID",
        examples=[1]
    )
    username: str = Field(
        default=...,
        title="User username",
        description="User's username",
        examples=["Roflianochka"]
    )
    first_name: str = Field(
        default=...,
        title="User name",
        description="User's name",
        examples=["Maxim"]
    )
    last_name: str = Field(
        default=...,
        title="User last name",
        description="User's last name",
        examples=["Belyaev"]
    )
    email: EmailStr = Field(
        default=...,
        title="UserEmail",
        description="Email address of the user",
        examples=["user@example.com"]
    )
    mobile_phone: str = Field(
        default=...,
        title="UserPhone",
        description="",
        examples=["+375545254125"]
    )
    hashed_password: str = Field(
        default=...,
        title="UserPassword",
        description="Hashed password of the user",
        examples=["hashed_password"]
    )
    is_active: bool = Field(
        default=True,
        title="IsActive",
        description="Indicates whether the user is active",
        examples=[True, False]
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        title="CreatedAt",
        description="Timestamp when the user was created"
    )

class UserUpdateDTO(BaseModel):
    id: PositiveInt = Field(
        default=...,
        title="UserID",
        description="Positive integer representing user ID",
        examples=[1]
    )
    username: str = Field(
        default=...,
        title="User username",
        description="User's username",
        examples=["Roflianochka"]
    )
    first_name: str = Field(
        default=...,
        title="User name",
        description="User's name",
        examples=["Maxim"]
    )
    last_name: str = Field(
        default=...,
        title="User last name",
        description="User's last name",
        examples=["Belyaev"]
    )
    email: EmailStr = Field(
        default=...,
        title="UserEmail",
        description="Email address of the user",
        examples=["user@example.com"]
    )
    mobile_phone: str = Field(
        default=...,
        title="UserPhone",
        description="",
        examples=["+375545254125"]
    )
    hashed_password: str = Field(
        default=...,
        title="UserPassword",
        description="Hashed password of the user",
        examples=["hashed_password"]
    )
    is_active: bool = Field(
        default=True,
        title="IsActive",
        description="Indicates whether the user is active",
        examples=[True, False]
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        title="CreatedAt",
        description="Timestamp when the user was created"
    )
