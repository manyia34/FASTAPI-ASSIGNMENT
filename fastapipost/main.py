from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

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
# ==========================================================
# We can send data from client to server in three forms:
# 1) Path parameter  --> /path/id
# 2) Query parameter --> ?name  => filter
# 3) Request body
# ==========================================================
# Flow of a POST request API
#   Client Sends JSON Body
#           ▼
#   FastAPI Receives POST Request  
#           ▼
#   Pydantic Validates Data ──Invalid──> 422 Error Response       
#        Valid
#           ▼
#   Backend Generates ID
#           ▼
#   Backend Stores Book
#           ▼
#   Response Status Code (201 Created)
# ============================================================
# Pydantic validation of data / Structure of the response body 
# ============================================================
class BookCreate(BaseModel):
    tittle : str
    genre : str
    author: str
    language: str
    
# =====================================================
# Creatig a new book sending data from client to server
# =====================================================
@app.post('/books',status_code=201)         # status code is declared in path parameter
def create_book(book : BookCreate):   # This calls the pydantic class
    # Logic to create the new_id
    new_id = max((book["id"] for book in books),default=0) + 1
    #  # dictonary for entering the new class
    new_book = {            
        "id" : new_id,                          
        "tittle" : book.tittle,
        "genre" : book.genre,
        "author" : book.author,
        "language" : book.language
    }
    books.append(new_book)                                         # Adding in the books list
    return {                                                       # server response in JSON bodyF
        "message" : "Book added successfully!",
        "book" : new_book
    }

