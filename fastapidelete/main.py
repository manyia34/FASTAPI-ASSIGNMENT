from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from typing import Optional  # This is used to create option to change the specific field
app = FastAPI()

# ==============================================
# Books List
# ==============================================
books = [
    {
        "id": 1,
        "title": "The Guide",
        "author": "R K Narayan",
        "genre": "Fiction",
        "language": "English"
    },
    {
        "id": 2,
        "title": "Wings of Fire",
        "author": "A P J Abdul Kalam",
        "genre": "Biography",
        "language": "English"
    }
]

# ==================================
# API Codes
# ==================================
@app.get('/')
def read_books():
    return books

@app.get('/book')
def get_books():
    return books 

# ====================================
# Delete API 
# ====================================
@app.delete('/books/{book_id}')
def delete_book(book_id : int):
    for existing_book in books:
        if existing_book["id"] == book_id:
            books.remove(existing_book)
            return {
                "message" : "Book deleted Successfully",
                "book" : existing_book
            }
    raise HTTPException(status_code=404 , detail="Book Not found") 