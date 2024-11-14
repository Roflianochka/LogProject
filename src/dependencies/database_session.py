from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from annotated_types import Annotated
from config import async_session_maker

__all__ = [
    "DBSession"
]


async def create_database_session():
    session: AsyncSession = async_session_maker()
    try:
        yield session
    finally:
        await session.aclose()


DBSession = Annotated[AsyncSession, Depends(dependency=create_database_session)]
