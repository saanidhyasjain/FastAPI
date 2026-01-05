from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import  status
app = FastAPI()

class Book():
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is auto generated", default=None) 
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1990, lt=2040)

    # Change the default values using model_config
    class Config:
        schema_extract = {
            "json_schema_extra": {
                "example": {
                    "title": "FastAPI",
                    "author": "geron",
                    "description": "Informative",
                    "rating": 5,
                    "published_date":2025
                }
            }
        }

BOOKS = [Book(1, 'title1', 'saanidhya', 'description1', 5, 2025),
         Book(2, 'title2', 'saanidhya', 'description2', 5, 2025),
         Book(3, 'title3', 'saanidhya', 'description3', 5, 2020),
         Book(4, 'title4', 'author 1', 'description', 2, 2039),
         Book(5, 'title5', 'author 2', 'description', 3, 2037),
         Book(6, 'title6', 'author 3', 'description', 1, 2027),
         ]

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


# Fetch a specific book from a list of books
# Validation for path parameters
@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def fetch_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')


# Filter by rating and get all the books
# Validation for query parameters
@app.get("/books/", status_code=status.HTTP_200_OK)
async def get_book_by_rating(b_rating:int = Query(gt=0, lt=6)):
    return_books = []
    for book in BOOKS:
        if book.rating == b_rating:
            return_books.append(book)
    return return_books


##### assignment ######

@app.get("/books/publish/", status_code=status.HTTP_200_OK)
async def get_book_by_publish_date(publish_date: int = Query(gt=1990, lt=2040)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == publish_date:
            books_to_return.append(book)
    return books_to_return

##### assignment ######

@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(book_id(new_book))

def book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


# PUT request method
@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='book not found')

#DELETE request method
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='book not found')

