from contextlib import asynccontextmanager

from fastapi import FastAPI

from book_app_fastapi.database import init_db
from book_app_fastapi.routes import books


@asynccontextmanager
async def life_span(app: FastAPI):
    print('Server is starting up 🛸')
    await init_db()
    yield
    print('Server has been stopped 🛑')


version = 'v1'

app = FastAPI(
    title='Book App',
    description='Book App API',
    version=version,
    lifespan=life_span,
)

app.include_router(
    books.router, prefix=f'/api/{version}/books', tags=['Books']
)
