from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import text

from book_app_fastapi.settings import settings

engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True,
)


async def init_db():
    async with engine.begin() as conn:
        statement = text("select 'Hello World'")

        result = await conn.execute(statement)

        print(result.all())
