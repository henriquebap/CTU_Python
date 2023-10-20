from pydantic import BaseModel


class ArtistBase(BaseModel):
    name: str
    category: str

class ArtistCreate(ArtistBase):
    pass

class Artist(ArtistBase):
    id: int

    class Config:
        from_attributes = True

class AlbumBase(BaseModel):
    name: str
    slug: str
    links: str
    release: int
    description: str

class AlbumCreate(AlbumBase):
    pass

class Album(AlbumBase):
    id: int

    class Config:
        from_attributes = True
        


