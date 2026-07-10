from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional
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


# =====================================
# Pydantic Model for update the book
# ====================================
class BookUpdate(BaseModel):
    title: str
    author: str
    language: str
    genre: str


# ====================================================================
# Pydantic Model for PATCH - all fields optional for partial update
# ====================================================================
class BookPatch(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    language: Optional[str] = None
    genre: Optional[str] = None


# ===================================================================
# Response Model is used when we to show some specific information
# ===================================================================
class BookResponse(BaseModel):
    id: int
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
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book Not Found!")

# HTTP_404_NOT_FOUND is used to show the error message when the book is not found in the name constraints


# =========================================================
#  POST creation of the new books using the response mddel
# =========================================================
@app.post('/books', response_model=BookActionResponse, status_code=status.HTTP_201_CREATED)
def add_new_book(book: BookCreate):
    # Duplication concept
    for existing_book in books:
        if existing_book["title"].lower() == book.title.lower():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="Title with this book already exist")

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


# ==============================================
# PUT : is used to update the whole Data
# ==============================================
@app.put('/books/{book_id}', response_model=BookActionResponse, status_code=status.HTTP_200_OK)
def Update_book(book_id: int, book: BookUpdate):
    for existing_book in books:
        # existing_book.update(book.model_dump())
        if existing_book["id"] == book_id:
            existing_book["title"] = book.title
            existing_book["language"] = book.language
            existing_book["author"] = book.author
            existing_book["genre"] = book.genre
            return {
                "message": "Book Update Successfully !",
                "book": existing_book
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book Not found")


# ==============================================================
# PATCH : is used to update only the given (partial) fields
# ==============================================================
@app.patch('/books/{book_id}', response_model=BookActionResponse, status_code=status.HTTP_200_OK)
def patch_book(book_id: int, book: BookPatch):
    for existing_book in books:
        if existing_book["id"] == book_id:
            # jo field bheji gayi hai (None nahi hai) sirf wahi update hogi
            if book.title is not None:
                existing_book["title"] = book.title
            if book.author is not None:
                existing_book["author"] = book.author
            if book.language is not None:
                existing_book["language"] = book.language
            if book.genre is not None:
                existing_book["genre"] = book.genre
            return {
                "message": "Book Updated Successfully !",
                "book": existing_book
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book Not found")


# ================================
# Delete : To delete the data
# ================================
@app.delete('/books/{book_id}', response_model=BookActionResponse, status_code=status.HTTP_200_OK)
def delete_book(book_id: int):
    for i in books:
        if i["id"] == book_id:
            books.remove(i)
            return {
                "message": "Book Deleted Successfully !",
                "book": i
            }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book Not found")
