from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse


import schemas
from database import crud

app = FastAPI()

@app.get("/stores", response_model=list[schemas.Store])
def get_store():
    stores = crud.get_stores()
    return stores

@app.post("/stores", status_code=201, response_model=schemas.Store)
def create_store(store: schemas.StoreCreate):
    db_store = crud.create_store(store)
    return db_store

@app.get("/stores/{store_id}", response_model=schemas.Store)
def get_store_by_id(store_id: int):
    store = crud.get_store_by_id(store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store


@app.put("/stores/{store_id}", response_model=schemas.Store)
def update_store(store_id: int, store: schemas.StoreCreate):
    db_store = crud.update_store(store_id, store)
    if not db_store:
        raise HTTPException(status_code=404, detail="Store not found")

    return db_store

@app.post("/stores/{store_id}/items/", status_code=201, response_model=schemas.Item)
def create_item(store_id: int, item: schemas.ItemCreate):
    store = crud.get_store_by_id(store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")

    db_item = crud.create_item(store_id, item)
    return db_item

@app.get("/items/{item_id}", response_model=schemas.Item)
def get_item(item_id: int):
    item = crud.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.delete("/items/{item_id}", response_model=schemas.Item)
def delete_item_by_id(item_id: int):
    item = crud.get_item(item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
        
    crud.delete_item_by_id(item_id)
    
    message = {"message": "item deleted"}
    return JSONResponse(content=message)

@app.get("/stores/{store_id}/items/", response_model=list[schemas.Item])
def get_Item_from_store(store_id: int):
    store = crud.get_store_by_id(store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    items = crud.get_items_from_store(store_id)
    return items

@app.get("/items", response_model=list[schemas.Item])
def get_item():
    items = crud.get_items()
    return items





