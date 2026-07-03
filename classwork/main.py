# Steps to intialize the fastapi
# python -m venv .venv
# .venv\Scripts\Activate.ps1
# pip install "fastapi[standard]"
# fastapi dev main.py
from fastapi import FastAPI
app = FastAPI()

# Home API :
@app.get('/')
def home():
    return {
        "message" : "welcome to my first fastapi assignment"
    }

# About API 
@app.get('/about')
def about():
    return {
        "Student_name" : "Manyia Mahajan",
        "Course" : "FastAPI",
        "Topic" : "First API Assignment",
        "Status" : "Learning"
    }
    
# Trainer API
@app.get('/trainer')
def trainer():
    return {
        "Name" : "Hemanth",
        "Role" : "Trainer",
        "Subject" : "FastAPI"
    }

# Course API
@app.get('/courses')
def courses():
    return [ 
            { 
                "id": 1,
                "name": "Python Basics",
                "duration": "1 week" 
            }, 
            { 
                "id": 2, 
                "name": "FastAPI", 
                "duration": "2 weeks" 
            }, 
            {
                "id": 3, 
                "name": "SQL Basics", 
                "duration": "1 week" 
            }
            ]
    
# Student API
@app.get('/student')
def Student():
    return [
        {
            "id": 1, 
            "name": "Akhil", 
            "course": "Python",
            "city": "Hyderabad"
        },
        {
            "id": 2, 
            "name": "Sai", 
            "course": "FastAPI", 
            "city": "Jammu"
        }
    ]
    
# College API
@app.get('/college')
def college():
    return {
        "College Name" : "Model Institute of Engineering and Technology",
        "Location" : "Kot Bhalwal Jammu",
        "Dept" : "Computer Science",
        "Current module" : "FastAPI Basics"
    }
    
# Technologies API
@app.get('/technologies')
def technology():
    return [
        "Python",
        "Fast API",
        "JSON",
        "HTTP",
        "REST API"
    ]
# ========================================================
# Dynamic urls
# ========================================================
@app.get('/student/{student_id}')
def get_student_by_id(student_id : int):
    return {
        "student_id" : student_id,
        "message" : "This is dynamic URL"
    }
    
@app.get('/courses/{course_id}')
def get_course_by_id(course_id : str):
    return {
        "course id" : course_id
    }

@app.get('/books/{book_id}/author/{author_id}')
def get_author_info(book_id : int , author_id : int):
    return {
        "Book id" : book_id,
        "author_id" : author_id
    }

@app.get('/books/{book_id}/courses/{course_name}')
def get_course_info(book_id : int , course_name : str):
    return {
        "Book Id" : book_id,
        "course_name" : course_name
    }
