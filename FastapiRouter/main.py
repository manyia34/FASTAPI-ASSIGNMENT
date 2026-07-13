from fastapi import FastAPI
# ====================================================================
# importing different files 
# syntax : from folder_name.file_name import instance as short_name
# ====================================================================
from routers.users import router as user_router
from routers.product import router as product_router

# ===============================================
# Adding Title and Description 
# ===============================================
app = FastAPI(
    title= "API Router Demo",
    description= "Learning FastAPI"
)

# ============================================
# include the router file in the main file 
# ============================================
app.include_router(user_router)
app.include_router(product_router)

@app.get('/home')
def get_home():
    return {
        "message" : "Welcome to the application"
    }

