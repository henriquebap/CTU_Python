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

def get_stores_with_items():
    db = SessionLocal()
    try:
        stores = db.query(models.Store).options(joinedload(models.Store.itens)).all() 
    finally:
        db.close()

    return stores

def create_item(name, description, price, store_id):
    db = SessionLocal()
    try:
        db_item = models.Item()
        db_item.name = name
        db_item.description = description
        db_item.price = price
        db_item.store_id = store_id  # Make sure store_id is an integer
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    finally:
        db.close()
    return db_item


def get_store_by_id(store_id):
    db = SessionLocal()
    try:
        store = db.query(models.Store).filter(models.Store.id==store_id).first()
        return store
    finally:
        db.close()
    

def delete_store_by_id(store_id):
    db = SessionLocal()
    try:
        store = db.query(models.Store).filter(models.Store.id == store_id).first()
        if store:
            db.delete(store)
            db.commit()
            return True  # Store deleted successfully
        else:
            return False  # Store with the specified ID not found
    finally:
        db.close()

def delete_item_by_id(item_id):
    db = SessionLocal()
    try:
        item = db.query(models.Item).filter(models.Item.id == item_id).first()
        if item:
            db.delete(item)
            db.commit()
            return True
        else:
            return False
    finally:
        db.close()

def get_items_from_store(store_id):
    db = SessionLocal()
    try:
        items = db.query(models.Item).filter(models.Item.store_id == store_id).all()
        return items
    finally:
        db.close()

        