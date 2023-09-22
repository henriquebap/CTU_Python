from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    name = Column(String(128))

    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    isbn = Column(String(128))
    name = Column(String(512))

    author_id = Column(Integer, ForeignKey("author.id"))
    author = relationship("Author", back_populates="books")