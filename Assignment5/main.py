# ===================
# Importing Files
# ===================
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
# ==================
# Data of events 
# ==================
events = [
    {
        "id": 1,
        "title": "Python Backend Workshop",
        "category": "Workshop",
        "location": "Hyderabad",
        "date": "2026-07-20",
        "organizer": "Code Club",
        "capacity": 100,
        "is_open": True
    },
    {
        "id": 2,
        "title": "Tech Career Fair",
        "category": "Career",
        "location": "Bengaluru",
        "date": "2026-07-25",
        "organizer": "Career Connect",
        "capacity": 300,
        "is_open": True
    },
    {
        "id": 3,
        "title": "Cultural Evening",
        "category": "Cultural",
        "location": "Hyderabad",
        "date": "2026-08-02",
        "organizer": "Arts Forum",
        "capacity": 500,
        "is_open": False
    }
]
# ============================
# GET /  API Route
# ============================
@app.get('/')
def event():
    return {"Welcome You!"}

# =============================
# GET /events  API Route
# =============================
@app.get('/event')
def get_event():
    return events

# ===================================
# GET /events/{events_id} API Route
# ====================================
@app.get('/events/{event_id}')
def get_event_by_id(event_id: int):
    for i in events:
        if i["id"] == event_id:
            return i
    raise HTTPException(status_code=404, detail="Event details Not found")

# =========================================
# GET /events?category=workshop API Route
# =========================================
@app.get('/events', status_code=200)
def get_workshop(category: str | None = None):
    if category is not None:
        filtered_record = []
        for e in events:
            if e["category"] == category:
                filtered_record.append(e)
        return filtered_record
    raise HTTPException(status_code=404, detail="Not found")

# ===================================
# GET /events?location=Hyderabad
# ====================================
@app.get('/events', status_code=200)
def get_location(location : str | None = None):
    if location is not None:
        filtered_record = []
        for l in events:
            if l["location"] == location:
                filtered_record.append(l)
        return filtered_record
    raise HTTPException(status_code=404, detail="Not found")

# ===================================
# GET /events?is_open=true
# ====================================
@app.get('/events', status_code=200)
def get_is_open(is_open: bool | None = None):
    if is_open is not None:
        filtered_record = []
        for o in events:
            if o["is_open"] == is_open:
                filtered_record.append(o)
        return filtered_record
    raise HTTPException(status_code=404, detail="Not found")

# =================================
# Pydantic models of Event create
# ================================
class EventCreate(BaseModel):
    title: str
    category: str
    location: str
    date: str
    organizer: str
    capacity: int
    is_open: bool

# ===================================
# Pydantic model of event update 
# ===================================
class EventUpdate(BaseModel):
    title: str
    category: str
    location: str
    date: str
    organizer: str
    capacity: int
    is_open: bool

# ==================================
# Pydantic model of event patch 
# ==================================
class EventPatch(BaseModel):
    title: Optional[str] = None
    category: Optional[str] = None
    location: Optional[str] = None
    date: Optional[str] = None
    organizer: Optional[str] = None
    capacity: Optional[int] = None
    is_open : Optional[bool] = None

# ===========================
# POST /events
# ===========================
@app.post('/events')
def Add_event(event : EventCreate):
    new_id = 0
    for i in events:
        if i["id"] > new_id:
            new_id = i["id"]
    new_id = new_id + 1
    new_event = {
        "id" : new_id,
        "title" : event.title,
        "category" : event.category,
        "location" : event.location,
        "date" : event.date,
        "organizer" : event.organizer,
        "capacity" : event.capacity,
        "is_open" : event.is_open
    }
    events.append(new_event)
    return {
        "message" : "Event Added Successfully!",
        "Event" : new_event
    }

# ============================
# PUT /events/{event_id}
# ===========================
@app.put('/events/{event_id}')
def Update_event_by_put(event_id : int , event : EventUpdate):
    for i in events:
        if i["id"] == event_id:
            i["title"] = event.title
            i["category"] = event.category
            i["location"] = event.location
            i["date"] = event.date
            i["organizer"] = event.organizer
            i["capacity"] = event.capacity
            i["is_open"] = event.is_open
            return {
                "message" : "Event Updated Successfully",
                "Event" : i
            }
    raise HTTPException(status_code=404,detail="Event Not Found")

# ==================================
# PATCH /events/{event_id}
# ==================================
@app.patch('/events/{event_id}')
def Update_events_by_patch(event_id: int, event: EventPatch):
    for i in events:
        if i["id"] == event_id:
            if event.title is not None:
                i["title"] = event.title
            if event.category is not None:
                i["category"] = event.category
            if event.location is not None:
                i["location"] = event.location
            if event.date is not None:
                i["date"] = event.date
            if event.organizer is not None:
                i["organizer"] = event.organizer
            if event.capacity is not None:
                i["capacity"] = event.capacity
            if event.is_open is not None:
                i["is_open"] = event.is_open
            return {
                "message": "Event update successfully",
                "event": i
            }
    raise HTTPException(status_code=404,detail="Event Not Found")

# ==============================
# DELETE/events/{event_id}
# ==============================
@app.delete('/events/{event_id}')
def delete_event(event_id : int):
    for i in events:
        if i["id"] == event_id:
            events.remove(i)
            return {
                "Message" : "Event Deleted Successfully",
                "Event" : i
                }
    raise HTTPException(status_code=404 , detail="Id not found !")