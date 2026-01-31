from fastapi import FastAPI ,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

books=[
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "year_published": 1949
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year_published": 1960      
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year_published": 1925
    },
    {
        "id": 4,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "year_published": 1813
    }
]

app=FastAPI()

@app.get("/book")
def get_books(book_id: int = None):
         return books

@app.get("/book/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    # If loop finishes and no book found
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with the id {book_id} not found"
    )
  
        

class Book(BaseModel):
    id: int
    title: str 
    author: str
    year_published: int

@app.post("/book")
def create_book(book: Book):
    new_book = book.model_dump()
    books.append(new_book)
    return book

class Book(BaseModel):
    id: int
    title: str 
    author: str
    year_published: int

@app.put("/book/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for book in books:
        if book["id"] == book_id:
            book["title"] = updated_book.title
            book["author"] = updated_book.author
            book["year_published"] = updated_book.year_published
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with the id {book_id} not found"
    )
