from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
app = FastAPI()

# =========================================
# Device List
# =========================================
devices= [
    {
        "id": 101,
        "name": "Wireless Mouse",
        "price": 500,
        "quantity": 10
    },
    {
        "id": 102,
        "name": "Mechanical Keyboard",
        "price": 1800,
        "quantity": 7
    },
    {
        "id": 103,
        "name": "USB-C Charger",
        "price": 900,
        "quantity": 15
    },
    {
        "id": 104,
        "name": "Bluetooth Speaker",
        "price": 2200,
        "quantity": 5
    },
    {
        "id": 105,
        "name": "Laptop Stand",
        "price": 1200,
        "quantity": 12
    }
]

# =============================
# API for get All devices
# =============================
@app.get('/device')
def get_device():
    return devices

# ================================
# Pydantic validation
# ===============================
class DeviceUpdate(BaseModel):
    name : str
    price : int
    quantity : int
    
# =======================================
# Update the device information 
# =======================================
@app.put('/device/{device_id}')
def update_device(device_id : int , device : DeviceUpdate):
    for i in devices:
        if i["id"] == device_id:
            i["name"] = device.name
            i["price"] = device.price
            i["quantity"] = device.quantity
            return {
            "message" : "Device details update successfully!",
            "devices" : i
        }
    raise HTTPException(status_code=404 , detail="Not found")
