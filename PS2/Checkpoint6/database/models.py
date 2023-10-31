from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Store(Base):
    __tablename__ = 'STORE_CP6'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    # Defina o relacionamento com a classe "Item"
    itens = relationship("Item", back_populates="store", lazy = "joined")

class Item(Base):
    __tablename__ = 'ITEM_CP6'

    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    description = Column(String(100))
    price = Column(Float, default=0)
    store_id = Column(Integer, ForeignKey('STORE_CP6.id'))

    # Defina o relacionamento com a classe "Store"
    store = relationship("Store", back_populates="itens")
