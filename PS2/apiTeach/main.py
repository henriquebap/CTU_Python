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

@app.put("/artists/{artist_id}", response_model=schemas.Artist)
def update_artist(artist_id: int, artist: schemas.ArtistCreate):
    db_artist = crud.update_artist(artist_id, artist)
    if not db_artist:
        raise HTTPException(404, "Artist não encontrado")
    
    return db_artist

@app.post("/artist/{artist_id}/albums/", status_code=201, response_model=schemas.AlbumBase)
def create_album(artist_id:int, albums: schemas.AlbumCreate):
    db_album = crud.create_album(artist_id, albums)
    if not artist_id:
        raise HTTPException(404, "Artista ou album não encontrados")
    return db_album


@app.get("/albums/{album_id}", response_model=schemas.Album)
def get_album(album_id: int):
    album = crud.get_album(album_id)
    if not album:
        raise HTTPException(404, "Album não encontrado")
    return album