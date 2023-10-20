from fastapi import FastAPI, HTTPException
import typing
import schemas
from database import crud

app = FastAPI()

@app.post("/artists", status_code=201, response_model=schemas.Artist)
def create_artist(artist: schemas.ArtistCreate):
    db_artist = crud.create_artist(artist)
    return db_artist

@app.get("/artists", response_model=typing.List[schemas.Artist])
def get_artists():
    artists = crud.get_artists()
    return artists

@app.get("/artists/{artist_id}",status_code=201, response_model=schemas.Artist)
def get_artist(artist_id: int):
    artist = crud.get_artist(artist_id)
    if not artist:
        raise HTTPException(404, "Artista não encontrado") 
    return artist

@app.post("/artist/{artist_id}/albums/", status_code=201, response_model=schemas.AlbumBase)
def create_album(artist_id:int, albums: schemas.AlbumCreate):
    db_album = crud.create_album(artist_id, albums)
    if not artist_id:
        raise HTTPException(404, "Artista ou album não encontrados")
    return db_album


