from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel
app = FastAPI()

# ================================================
# PUT request means update the whole data
# ================================================
books = [
    {
        "id": 1,
        "title": "The Guide",
        "author": "R K Narayan",
        "genre": "Fiction",
        "language": "English",
    },
    {
        "id": 2,
        "title": "Wings of Fire",
        "author": "A P J Abdul Kalam",
        "genre": "Biography",
        "language": "English",
    },
]

@app.get('/books')
def get_books():
    return books

# =========================================
# creating a pydantic class for put
# =========================================
class BookUpdate(BaseModel):
    tittle : str
    author : str
    genre : str
    language : str
    
# ===========================================
# updating the books
# ===========================================
@app.put('/books/{book_id}')
def update_book(book_id : int , book : BookUpdate):
    for existing_book in books:
        if existing_book["id"] == book_id:
            # existing_book["tittle"] = book.tittle
            # existing_book["author"] = book.author
            # existing_book["genre"] = book.genre
            # existing_book["language"] = book.language
            existing_book.update(book.model_dump())
            return {
                "message" : "Book update Successfully !",
                "book" : existing_book 
            }
    raise HTTPException(status_code=404,detail="Book Not Found")