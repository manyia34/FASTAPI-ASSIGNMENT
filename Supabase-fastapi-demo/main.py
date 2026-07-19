from fastapi import FastAPI, HTTPException, status
from database import supabase

app = FastAPI(
    title="SupaBase Demo",
    description="SupaBase Demo with FastApi",
)

@app.get('/')
def home():
    return {
        "message": "Supabase Api is running"
    }


@app.get('/books', status_code=status.HTTP_200_OK)
def books():
    try:
        response = (
            supabase.table("books").select("*").execute()
        )
        return response.data

    except Exception as error:
        print("database error: ", error)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail="Unable to retrieve books data from database !")
