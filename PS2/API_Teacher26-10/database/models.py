from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Artist(Base):
    __tablename__ = 'artist'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    category = Column(String(64))

    albums = relationship("Album", back_populates="artist")

class Album(Base):
    __tablename__ = 'album'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    slug = Column(String(256))
    links = Column(String(128))
    release = Column(Integer)
    description = Column(String(512))
    artist_id = Column(Integer, ForeignKey("artist.id"))

    artist = relationship("Artist", back_populates="albums")
    songs = relationship("Song", back_populates="album")

class Song(Base):
    __tablename__ = 'song'

    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    track_number = Column(Integer)
    album_id = Column(Integer, ForeignKey("album.id"))

    album = relationship("Album", back_populates="songs")
