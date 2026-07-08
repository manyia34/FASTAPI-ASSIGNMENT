from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from typing import Optional  # This is used to create option to change the specific field
app = FastAPI()

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

# ================================================================
# Pydantic structure with to change the specific area or field
# ================================================================
class BookUpdate(BaseModel):
    title : Optional[str] = None
    author : Optional[str] = None
    genre : Optional[str] = None
    language : Optional[str] = None
    
# =============================================
# Patch API code
# =============================================
@app.patch('/books/{book_id}')
def Update_books(book_id : int , book : BookUpdate):
    for existing_book in books:
        if existing_book["id"] == book_id:
            if book.title is not None:
                existing_book["title"] = book.title           # Creating Multiple option
            if book.language is not None:
                existing_book["language"] = book.language
            if book.genre is not None:
                existing_book["genre"] = book.genre
            if book.author is not None:
                existing_book["author"] = book.author
            return {
                "message" : "Book updated successfully",
                "book" : existing_book
            }
    raise HTTPException(status_code=404,detail="Book Not found")