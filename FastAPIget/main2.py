# =========================================================
# import fast api module
from fastapi import FastAPI
app = FastAPI()
# =========================================================
students = [
    {"id": 1, "name": "Akhil", "course": "Python", "city": "Hyderabad"},
    {"id": 2, "name": "Sai", "course": "FastAPI", "city": "Vijayawada"},
    {"id": 3, "name": "Ravi", "course": "SQL", "city": "Guntur"},
    {"id": 4, "name": "Kiran", "course": "Python", "city": "Vizag"},
    {"id": 5, "name": "Meena", "course": "FastAPI", "city": "Chennai"},
    {"id": 6, "name": "Hemanth", "course": "Python", "city": "Hyderabad"}
]

# ===========================================================
# Adding multiple query parameter
# ===========================================================
@app.get('/students')
def get_student(course : str | None = None , city : str | None = None):
    filtered_student = students
    if course is not None:
        result = []
        for s in filtered_student:
            if s["course"].lower() == course.lower():
                result.append(s)
        filtered_student = result

    if city is not None:
        result = []
        for s in filtered_student:
            if s["city"].lower() == city.lower():
                result.append(s)
        filtered_student = result
    return filtered_student

                