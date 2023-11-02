from pydantic import BaseModel
from typing import List

class ItemBase(BaseModel):
    name : str
    description : str
    price : float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id : int

    class Config:
        orm_mode = True
        from_attributes = True


class StoreBase(BaseModel):
    name : str

class StoreCreate(StoreBase):
    pass

class Store(StoreBase):
    id: int
    itens: List[Item] = []

    class Config:
        orm_mode = True
        from_attributes = True


