# =====================================================================================================
# Rouetrs is used to group all the routes in a single file and then we can import that file in main.py
# =====================================================================================================
from fastapi import APIRouter

# ===================================================================
# Adding prefix in the to reduction the /products again and again
# ===================================================================
router = APIRouter(
    prefix = '/products',          
    tags= ['product']        # Used to seperration in different different domain 
)

@router.get('')
def get_products():
    return ["Mobile","laptop","watch"]

@router.get('/{product_id}')
def get_product(product_id : str):
    return {
        "Message" : "Product found !",
        "product" : product_id
    }
