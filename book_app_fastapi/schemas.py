from pydantic import BaseModel


class BookUpdateSchema(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


class MessageSchema(BaseModel):
    message: str
