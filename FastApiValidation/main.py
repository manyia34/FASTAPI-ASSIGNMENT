from fastapi import FastAPI, HTTPException , status  
from pydantic import BaseModel
app = FastAPI()

books = [
    {
        "id": 1,
        "title": "The Guide",
        "author": "R K Narayan",
        "genre": "Fiction",
        "language": "English",
        "internal_note": "Added by admin",
        "created_by": "trainer"
    }
]

# ====================================
# Pydanctic model for creating books 
# ====================================
class BookCreate(BaseModel):
    title: str
    author: str
    language: str
    genre: str


# ===================================================================
# Response Model is used when we to show some specific information
# ===================================================================
class BookResponse(BaseModel):
    id : int
    title: str
    author: str
    genre: str
    language: str

# ======================================
# Message Response Model
# ======================================
class BookActionResponse(BaseModel):
    message: str
    book: BookResponse

# ===================================================================
# list[BookResponse] is used because we return all the books record
# ==================================================================
@app.get('/books', response_model=list[BookResponse])
def get_books():
    return books

# ============================================================
# Response model is always written in the decorator
# ============================================================
@app.get('/books/{book_id}', response_model=BookResponse)
def get_books_by_id(book_id: int):
    for i in books:
        if i["id"] == book_id:
            return i
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found!")

# HTTP_404_NOT_FOUND is used to show the error message when the book is not found in the name constraints

# ======================================================
# creation of the new books using the response mddel
# ======================================================
@app.post('/books', response_model=BookActionResponse,status_code=status.HTTP_201_CREATED)
def add_new_book(book: BookCreate):
    new_id = max((book["id"] for book in books), default=0)+1
    new_book = {
        "id": new_id,
        "title": book.title,
        "genre": book.genre,
        "language": book.language,
        "author": book.author,
        "internal_note": "Added by admin",
        "created_by": "trainer"
    }
    books.append(new_book)
    return {
        "message": "Book Added Successfully!",
        "book": new_book
    }
