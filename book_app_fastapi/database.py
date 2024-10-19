from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel

from book_app_fastapi.settings import settings

engine = create_async_engine(
    url=settings.DATABASE_URL,
    connect_args={'ssl': True},
    echo=True,
)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
