from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
app = FastAPI()

# ==================================
# Movies Data 
# ===================================
movies = [
    {
        "id" : 1,
        "title" : "3 Idiots",
        "director" : "Rajkumar Hirani",
        "genre" : "Comedy Drama",
        "language" : "Hindi",
        "release_year": 2009
    },
    {
        "id" : 2,
        "title" : "Baahubali",
        "director": "S S Rajamouli",
        "genre": "Action Drama",
        "language": "Telugu",
        "release_year": 2015
    }
]


# =================================
# Create a Pydantic model Named 
# =================================
class MovieUpdate(BaseModel):
    title : str
    director : str
    genre : str
    language : str
    release_year : int

# =======================
# GET/
# =======================
@app.get('/')
def movie():
    return movies


# =======================
# GET /movies
# =======================
@app.get('/movies')
def get_movies():
    return movies

# =========================
# GET/movies/{movies_id}
# =========================
@app.get('/movies/{movies_id}')
def get_movies_by_id(movies_id : int | None = None):
    if movies_id is not None:
        filter_movie = []
        for movie in movies:
            if movie["id"] == movies_id:
                filter_movie.append(movie)
        return filter_movie
    return movies

# ================================
# PUT Request API
# ================================
@app.put('/movies/{movies_id}',status_code=201)
def update_movie(movies_id : int , movie : MovieUpdate):
    for existing_movie in movies:
        if existing_movie["id"] == movies_id:
            existing_movie["title"] = movie.title
            existing_movie["director"] = movie.director
            existing_movie["genre"] = movie.genre
            existing_movie["language"] = movie.language
            existing_movie["release_year"] = movie.release_year
            return {
                "message" : "Movie Update Successfully",
                "Movies" : existing_movie
            }
            
    raise HTTPException(status_code=404 , detail="Movie Not found")
            