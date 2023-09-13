from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)

#database_url = 'oracl+oracledb://rm97796:240019@server/database'
database_url = '''
oracle+oracledb://rm97796:153462@oracle.fiap.com.br?service_name=orcl'''

engine = create_engine(database_url)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()