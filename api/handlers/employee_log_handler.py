from typing import List

from fastapi import APIRouter, HTTPException, Path
from sqlalchemy import select, update
from starlette import status
from src.models import User
from src.models.users_logs import UserLog as EmployeeLog
from src.dependencies import DBSession
from src.types import  UserLogCreateDTO,  UserLogUpdateDTO, UserLogBaseDTO

from sqlalchemy.orm import joinedload

router = APIRouter(
    prefix="/logs",
    tags=["Логи"]
)


@router.get(
    path="/",
    response_model=List[UserLogBaseDTO]
)
async def get_all_logs(db_session: DBSession):
    statement = select(EmployeeLog).options(
        joinedload(EmployeeLog.user)
    )

    logs = await db_session.scalars(statement=statement)
    logs = logs.unique().all()
    if not logs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Logs not found")
    return [UserLogBaseDTO.model_validate(obj=log, from_attributes=True) for log in logs]


@router.post(
    path="/",
    response_model=UserLogCreateDTO
)
async def create_new_log(db_session: DBSession, log: UserLogCreateDTO):
    new_log = EmployeeLog(**log.model_dump())
    try:
        db_session.add(new_log)
        await db_session.commit()
    except Exception as e:
        print(e)
        await db_session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to create new log")
    return UserLogCreateDTO.model_validate(obj=new_log, from_attributes=True)


@router.put(
    path="/{user_id}",
    response_model=UserLogBaseDTO
)
async def update_by_user_id(db_session: DBSession, data: UserLogUpdateDTO, user_id: int = Path()):
    await db_session.execute(
        update(EmployeeLog).filter(EmployeeLog.user_id == user_id).values(**data.model_dump())
    )
    try:
        await db_session.commit()
    except Exception as e:
        print(e)
        await db_session.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to update log")

    statement = select(EmployeeLog).filter(EmployeeLog.user_id == user_id)
    obj = await db_session.scalar(statement=statement)

    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Log not found")

    return UserLogBaseDTO.model_validate(obj=obj, from_attributes=True)
