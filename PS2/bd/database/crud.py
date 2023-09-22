from database import SessionLocal
from database.models import Item, User


def create_user(first_name, last_name, email):
    db = SessionLocal()
    try:
        user = User()
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        db.add(user)
        db.commit()
    finally:
        db.close()

    return user

def get_user(user_id):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == user_id).first()
        return user
    finally:
        db.close()


def get_users():
    db = SessionLocal()
    try:
        users = db.query(User)
        for user in users:
            yield user
    finally:
        db.close()


def delete_user(user_id):
    db = SessionLocal()
    try:
        db.query(User).filter(User.id == user_id).delete()
        db.commit()
    finally:
        db.close()

def create_item(title, description, owner):
    db = SessionLocal()
    try:
        item = Item()
        item.title = title
        item.description = description
        item.owner = owner
        db.add(item)
        db.commit()
    finally:
        db.close()

    return item

def get_items():
    db = SessionLocal()
    try:
        items = db.query(Item)
        for item in items:
            yield item
    finally:
        db.close()