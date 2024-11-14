import subprocess
from typing import List
from fastapi import APIRouter, Path, HTTPException
from sqlalchemy import select, update, delete
from sqlalchemy.orm import joinedload
from starlette import status
from src.models import User
from src.types import UserCreateDTO
from src.types.user_type import UserBaseDTO as UserDTO, UserUpdateDTO
from src.dependencies.database_session import DBSession


router = APIRouter(
    prefix="/users",
    tags=["Пользователи"]
)


@router.get(
    path="",
    response_model=List[UserDTO]
)
async def get_all_users(db_session: DBSession):
    statement = select(User)
    users = await db_session.scalars(statement=statement)
    users = users.unique().all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
    return [UserDTO.model_validate(user, from_attributes=True) for user in users]



@router.get(
    path="/{user_id}",
    response_model=UserDTO
)
async def get_user_by_id(
        db_session: DBSession,
        user_id: int = Path()
):
    statement = select(User).filter(User.id == user_id)
    user = await db_session.scalar(statement=statement)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
    return UserDTO.model_validate(user, from_attributes=True)


@router.post(
    path="",
    response_model=UserDTO
)
async def create_new_user(
        db_session: DBSession,
        user: UserCreateDTO,
):
    new_user = User(**user.model_dump())  # Убираем исключение ролей
    db_session.add(new_user)
    try:
        await db_session.commit()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Couldn't add a new entry")

    result = await db_session.execute(
        select(User).where(User.id == new_user.id)
    )
    new_user = result.scalars().first()
    return UserDTO.model_validate(obj=new_user, from_attributes=True)


@router.put(
    path="/{user_id}",
    response_model=UserDTO
)
async def update_user(
        db_session: DBSession,
        user: UserUpdateDTO,
        user_id: int = Path()
):
    statement = select(User).filter(User.id == user_id)
    existing_user = await db_session.scalar(statement)
    if existing_user:
        await db_session.execute(
            update(User).filter(User.id == user_id).values(**user.model_dump())
        )
        await db_session.commit()  # Обновляем пользователя
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return await get_user_by_id(db_session=db_session, user_id=user_id)


@router.delete(
    path="/{user_id}"
)
async def delete_user(
        db_session: DBSession,
        user_id: int = Path()
):
    statement = select(User).filter(User.id == user_id)
    existing_user = await db_session.scalar(statement)
    if existing_user:
        try:
            await db_session.delete(existing_user)
            await db_session.commit()
            return {"status": "success"}
        except Exception as e:
            print(e)
            await db_session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to delete user")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
