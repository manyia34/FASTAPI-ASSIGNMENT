from fastapi import FastAPI, HTTPException
app = FastAPI()

# Creating a Book function 
books = [
    {
        "id": 1, 
        "title": "The Guide",
        "author": "R K Narayan", 
        "genre": "Fiction", 
        "language": "English", 
        "available": True
    },
    {
        "id": 2,
        "title": "Wings of Fire",
        "author": "A P J Abdu l Kalam",
        "genre": "Biography", 
        "language": "English", 
        "available": True
    },
    {
        "id": 3, 
        "title": "Python Basics", 
        "author": "Code Tea m", 
        "genre": "Technology", 
        "language": "English", 
        "available": False
    },
    {
        "id": 4, 
        "title": "Telugu Stories", 
        "author": "Local Aut hor", 
        "genre": "Fiction", 
        "language": "Telugu", 
        "available": True
    },
    {
        "id": 5, 
        "title": "Indian History", 
        "author": "History Team", 
        "genre": "History",
        "language": "English", 
        "available": True
    },
    {
        "id": 6, 
        "title": "Science Facts",
        "author": "Science Team", 
        "genre": "Science", 
        "language": "Hindi",
        "available": True
    }
]

# Home API 
@app.get('/')
def home():
    return {
        "Message" : "Library API is Running !"
    }

# Get All Books
@app.get('/books')
def get_books():
    return books

# Get Books by id using path parameter
@app.get('/books/{book_id}')
def get_book_by_id(book_id : int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error" : "Book Not Found !"}

# Filter Books by Genre Using Query Parameter
@app.get('/books')
def get_book_by_genre(genre : str | None = None):
    if genre is not None:
        filtered_books = []
        for book in books:
            if book["genre"] == genre:
                filtered_books.append(book)
        return filtered_books
    return books

# Filter Books by language Using Query Parameter
@app.get('/books-by-language')
def get_book_by_language(language : str | None = None):     
    if language is not None:
        filtered_books = []
        for book in books:
            if book["language"] == language:
                filtered_books.append(book)
        return filtered_books
    return books
