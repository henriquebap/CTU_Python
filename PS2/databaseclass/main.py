from database import SessionLocal
from models import User


db = SessionLocal()
usuarios = db.query(User)

for usuario in usuarios:
    print(f'id:{usuario.CD_USUARIO}')
    print(f'Nome:{usuario.NM_USUARIO}')

    