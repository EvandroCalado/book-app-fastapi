from fastapi import FastAPI

from book_app_fastapi.routes import books

version = 'v1'

app = FastAPI(
    title='Book App',
    description='Book App API',
    version=version,
)

app.include_router(
    books.router, prefix=f'/api/{version}/books', tags=['Books']
)
