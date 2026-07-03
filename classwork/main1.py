from fastapi import FastAPI , HTTPException  
app = FastAPI()

# ===========================================================
students = [
    {"id": 1, "name": "Akhil", "course": "Python", "city": "Hyderabad"},
    {"id": 2, "name": "Sai", "course": "FastAPI", "city": "Vijayawada"},
    {"id": 3, "name": "Ravi", "course": "SQL", "city": "Guntur"},
    {"id": 4, "name": "Kiran", "course": "Python", "city": "Vizag"},
    {"id": 5, "name": "Meena", "course": "FastAPI", "city": "Chennai"}
]

# Get the whole Student record
@app.get('/students')
def get_students():
    return students

# Iterating whole student record by student_id
@app.get('/students/{student_id}')
def get_student_info_by_id(student_id : int):
    for student in students:
        if student["id"] == student_id:
            return student
    return {"error" : "Student does not found"}   # No found case

# ===========================================================
# HTTP exceptions 
# ===========================================================
@app.get('/students/{student_id}')
def get_student_info_by_id(student_id : int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code = 404, detail = "Student Data Not Founded !")

# ============================================================
# Order of execution : fixed to dynamic 
# ============================================================
@app.get('/students/topper')
def get_topper():
    return {
        "Name" : "Chandra bhushan",
        "Rank" : "topper"
    }

@app.get('/students/{student_id}')
def get_student_info_by_id(student_id : int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code = 404, detail = "Student Data Not Founded !")

# =========================================================
# Query parameters 
# =========================================================
@app.get('/students')
def get_students(course : str | None = None):
    if course is not None:
        filtered_students = []
        
        for student in students:
            if student["course"].lower() == course.lower():
                filtered_students.append(student)  
        return filtered_students
    return students
    
products = [
    {"id": 1, "name": "Asus", "category": "Electronics", "price": 50000},
    {"id": 2, "name": "Dell", "category": "Electronics", "price": 60000},
    {"id": 3, "name": "iPhone", "category": "Mobiles", "price": 80000},
    {"id": 4, "name": "Samsung TV", "category": "Electronics", "price": 45000},
    {"id": 5, "name": "Nike Shoes", "category": "Fashion", "price": 5000},
    {"id": 6, "name": "Office Chair", "category": "Furniture", "price": 12000},
    {"id": 7, "name": "Water Bottle", "category": "Kitchen", "price": 500},
    {"id": 8, "name": "Notebook", "category": "Stationery", "price": 100}
]

@app.get('/products')
def home():
    return products

@app.get('/products')
def get_product(category : str | None = None):
    if category is not None:
        filter_product = []
        for product in products:
            if product["category"] == category:
                filter_product.append(product)
        return filter_product
    return products
