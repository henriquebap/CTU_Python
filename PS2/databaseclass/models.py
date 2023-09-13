from database import Base
from sqlalchemy import Column, String, Integer

class User(Base):
    __tablename__ = 'PRODUTO'

    CD_USUARIO = Column(Integer)
    NM_USUARIO = Column(String)


