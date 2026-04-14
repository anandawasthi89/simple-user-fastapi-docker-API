from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

Base = declarative_base()
engine = create_engine(os.getenv("DB_PATH_USER"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()