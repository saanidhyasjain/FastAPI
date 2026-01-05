from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Book():
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int] = None 
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    rating: int = Field(gt=0, lt=6)

BOOKS = [Book(1, 'title1', 'saanidhya', 'description1', 5),
         Book(2, 'title2', 'saanidhya', 'description2', 5),
         Book(3, 'title3', 'saanidhya', 'description3', 5),
         Book(4, 'title4', 'author 1', 'description', 2),
         Book(5, 'title5', 'author 2', 'description', 3),
         Book(6, 'title6', 'author 3', 'description', 1),
         ]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(book_id(new_book))

def book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book