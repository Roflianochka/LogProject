from pydantic import PostgresDsn, SecretStr
from pydantic_settings import BaseSettings

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession


class Settings(BaseSettings):
    POSTGRES_URL: PostgresDsn
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    class Config:
        env_file = '.env'

config = Settings()

async_engine = create_async_engine(
    url=config.POSTGRES_URL.unicode_string(),
    echo=True
)

async_session_maker = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)
