from fastapi import HTTPException
from database import SessionLocal, models
from sqlalchemy.orm import joinedload


def create_store(name):
    db = SessionLocal()

    try:
        db_store = models.Store()
        db_store.name = name
        db.add(db_store)
        db.commit()
        db.refresh(db_store)
    finally:
        db.close()
    
    return db_store

# def get_stores():
#     db = SessionLocal()
#     try:
#         stores = db.query(models.Store).all()
#     finally:
#         db.close()
#     return stores


# def get_store(store_id):
#     db = SessionLocal()
#     try:
#         store = db.query(models.Store).filter(models.Store.id == store_id).first()
#     finally:
#         db.close()
#     return store

# Em crud.py

def get_stores_with_items():
    db = SessionLocal()
    try:
        stores = db.query(models.Store).options(joinedload(models.Store.itens)).all() 
    finally:
        db.close()

    return stores

def create_item(store_id: int, name, description, price):
    db = SessionLocal()
    try:
        db_item = models.Item()
        db_item.name = name
        db_item.description = description
        db_item.price = price
        db_item.store_id = store_id
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    finally:
        db.close()
    return db_item

def get_store_by_id(store_id: int):
    db = SessionLocal()
    try:
        store = db.query(models.Store).filter(models.Store.id==store_id).first()
    except:
        raise HTTPException(status_code=404, detail="Store not found")
    return store