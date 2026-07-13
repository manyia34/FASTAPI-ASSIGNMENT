# =====================================================================================================
# Rouetrs is used to group all the routes in a single file and then we can import that file in main.py
# =====================================================================================================
from fastapi import APIRouter

# ===================================================================
# Adding prefix in the to reduction the /users again and again
# ===================================================================
router = APIRouter(
    prefix = '/users',
    tags= ['users']
)

@router.get('')
def get_users():
    return ["Manyia","vivek"]

@router.get('/{user_id}')
def  get_user(user_id : str):
    return {
        "name" : "Unknown",
        "user_id" : user_id
    }