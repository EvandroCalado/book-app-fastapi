from typing import List

from fastapi import APIRouter, HTTPException, status

from book_app_fastapi.data import books
from book_app_fastapi.models import Book
from book_app_fastapi.schemas import BookUpdateSchema, MessageSchema

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(book: Book):
    new_book = book.model_dump()

    books.append(new_book)

    return new_book


@router.get('/', response_model=List[Book])
async def read_all_books() -> list[dict]:
    return books


@router.get('/{book_id}', response_model=Book)
async def read_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Book with id {book_id} not found',
    )


@router.patch('/{book_id}', response_model=Book)
async def update_book(book_id: int, book_update: BookUpdateSchema):
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update.title
            book['author'] = book_update.author
            book['publisher'] = book_update.publisher
            book['page_count'] = book_update.page_count
            book['language'] = book_update.language

            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Book with id {book_id} not found',
    )


@router.delete('/{book_id}', response_model=MessageSchema)
async def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)

            return {'message': f'Book with id {book_id} deleted successfully'}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Book with id {book_id} not found',
    )
