from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [

    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},

    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},

    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},

    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},

    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},

    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}

]

# Static path
@app.get("/books")
async def read_all_books():
    return BOOKS

# Dynamic Path (API URL - {book_title})
@app.get("/books/{book_title}")
async def read_book(book_title : str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        
# Query Parameter
@app.get("/books/")
async def read_book_by_category(category : str):
    book_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            book_to_return.append(book)
    return book_to_return

#####################################
###############  SOL  ###############
#####################################

# Query parameter sol
@app.get("/books/byauthor/")
async def get_all_books(author: str):
    all_books = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            all_books.append(book)
    return all_books

#####################################
###############  SOL  ###############
#####################################

# Query and Path Parameter (dynamic - author and query parameter - category)
@app.get("/books/{author}/")
async def read_book_by_author_and_category(author:str, category:str):
    book_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold() and \
            book.get('category').casefold() == category.casefold():
            book_to_return.append(book)
    return book_to_return

# POST request methods
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

# PUT request methods
@app.put("/books/update_book")
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.get('title').casefold():
            BOOKS[i] = update_book

# DELETE request method
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break  


'''Get all books from a specific author using path or query parameters'''

#####################################
###############  SOL  ###############
#####################################

# Path parameter sol
@app.get("/books/byauthor/{author}")
async def get_all_books(author: str):
    all_books = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            all_books.append(book)
    return all_books

#####################################
###############  SOL  ###############
#####################################
