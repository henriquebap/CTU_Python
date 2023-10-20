import schemas
from database import SessionLocal, models


def create_artist(artist: schemas.ArtistCreate):
    db  = SessionLocal()

    try:
        db_artist = models.Artist()
        db_artist.name = artist.name
        db_artist.category = artist.category
        db.add(db_artist)
        db.commit()
    finally:
        db.close()
    
    return db_artist

def update_artist(artist_id: int, artist: schemas.ArtistCreate):
    db_artist = get_artist(artist_id)
    if not db_artist:
        return
    
    db_artist.name = artist.name
    db_artist.category = artist.category

    db = SessionLocal()
    try:
        db.add(db_artist)
        db.commit()
    finally:
        db.close()

    return db_artist

def get_artists():
    db = SessionLocal()
    try:
        artists = db.query(models.Artist).all()
    finally:
        db.close()
    return artists

def get_artist(artist_id: int):
    db = SessionLocal()
    try:
        artist = db.query(models.Artist).filter(models.Artist.id == artist_id).first()
    finally:
        db.close()
    return artist

def create_album(artist_id: int, album: schemas.AlbumCreate):
    db = SessionLocal()
    try:
        db_album = models.Album()
        db_album.name = album.name
        db_album.slug = album.slug
        db_album.links = album.links
        db_album.release = album.release
        db_album.description = album.description
        db_album.artist_id = artist_id
        db.add(db_album)
        db.commit()
    finally:
        db.close()
    
    return db_album


def get_album(album_id: int):
    db = SessionLocal()
    try:
        album = db.query(models.Album).filter(models.Album.id == album_id).first()
    finally:
        db.close()
    return album
