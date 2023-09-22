from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(128), unique=True)
    first_name = Column(String(32))
    last_name = Column(String(128))

    items = relationship("Item", back_populates="owner")

    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'.strip()


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    title = Column(String(128))
    description = Column(String(512))
    owner_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="items")
