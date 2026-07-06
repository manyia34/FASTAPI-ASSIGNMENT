from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# =====================================
# Notes List 
# =====================================
Notes = [
    {
        "id" : 1,
        "tittle" : "FastAPI Intro",
        "content" : "FastAPI is used to build backend APIs in python.",
        "category" : "Backend",
        "priority" : "High",
    },
    {
        "id" : 2,
        "tittle" : "Request Body",
        "content" : "A request body carries data sent by the client.",
        "category" : "API",
        "priority" : "Medium"
    }
]

# =============================================
# Creation of pydantic model named NotesCreate
# =============================================
class NoteCreate(BaseModel):
    tittle : str
    content : str
    category : str
    priority : str
    
# =============================================
# GET/ to check API status
# =============================================
@app.get('/')
def notes():
    return Notes

# =============================================
# GET/notes to return all notes
# =============================================
@app.get('/Notes')
def get_notes():
    return Notes

# ============================================
# POST/notes with status code = 201
# ============================================
@app.post('/Notes',status_code=201)
def add_notes(note : NoteCreate):
    new_id = 0
    for i in Notes:
        if (i["id"] > new_id):
            new_id = i["id"]
    new_id = new_id + 1
    new_notes = {
        "id" : new_id,
        "tittle" : note.tittle,
        "content" : note.content,
        "category" : note.category,
        "priority" : note.priority
    }
    Notes.append(new_notes)
    return {
        "message" : "New Book is added successfully!",
        "notes" : new_notes
    }