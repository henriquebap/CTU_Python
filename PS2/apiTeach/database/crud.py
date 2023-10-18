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


def create_album(album: schemas.Album):
    db = SessionLocal()

    try:
        db_album = models.Album()
        db_album.name = album.name
        db.add(db_album)
        db.commit()
    finally:
        db.close()
    return album


    