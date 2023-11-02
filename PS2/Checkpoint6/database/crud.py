from database import SessionLocal, models
from sqlalchemy.orm import joinedload
import schemas
import sqlalchemy


def create_store(store: schemas.StoreCreate):
    db = SessionLocal()

    try:
        db_store = models.Store()
        db_store.name = store.name
        db.add(db_store)
        db.commit()
        db.refresh(db_store)
    finally:
        db.close()
    return db_store


def create_item( store_id: int, item: schemas.ItemCreate):
    db = SessionLocal()
    try:
        db_item = models.Item()
        db_item.name = item.name
        db_item.description = item.description
        db_item.price = item.price
        db_item.store_id = store_id
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    finally:
        db.close()
    return db_item

def get_stores():
    db = SessionLocal()
    try:
        artists = db.query(models.Store).all()
    finally:
        db.close()
    return artists



def get_store_by_id(store_id):
    db = SessionLocal()
    try:
        store = db.query(models.Store).filter(models.Store.id==store_id).first()
        
    finally:
        db.close()
    return store

# def delete_store_by_id(store_id):
#     db = SessionLocal()
#     try:
#         store = db.query(models.Store).filter(models.Store.id == store_id).first()
#         if store:
#             db.delete(store)
#             db.commit()
#             return True  # Store deleted successfully
#         else:
#             return False  # Store with the specified ID not found
#     finally:
#         db.close()

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

def update_store(store_id: int, store: schemas.StoreCreate):
    db_store = get_store_by_id(store_id)
    if not db_store:
        return
    
    db_store.name = store.name

    db = SessionLocal()
    try:
        db.add(db_store)
        db.commit()
    finally:
        db.close()

    return db_store

def get_item(item_id: int):
    db = SessionLocal()
    try:
        item = db.query(models.Item).filter(models.Item.id == item_id).first()
    finally:
        db.close()
    return item


# def get_store_and_items():
#     db = SessionLocal()
#     try:
#         stores = db.query(models.Store).options(joinedload(models.Store.itens)).order_by(models.Store.name).all()
#         return [store.__dict__ for store in stores]
#     except Exception as e:
#         print("Error: ", str(e))
#     finally:
#         db.close()

def get_items():
    db = SessionLocal()
    try:
        artists = db.query(models.Item).all()
    finally:
        db.close()
    return artists