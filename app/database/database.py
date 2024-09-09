from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:123@db:5432/eventlink')

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    """Cria todas as tabelas no banco de dados"""
    import app.models.models
    Base.metadata.create_all(bind=engine)

def get_db():
    """Retorna uma sessão de banco de dados"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
