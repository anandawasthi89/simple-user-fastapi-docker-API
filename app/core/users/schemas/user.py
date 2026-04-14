from sqlalchemy import Column, Integer, String
from app.core.db.DBConnection import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=False)
    email = Column(String, unique=True, index=True)
    bank_id = Column(String, index=True)
    bank_account = Column(String, unique=True, index=True)
    status = Column(String, index=True)
    created_at = Column(String, index=False)
    updated_at = Column(String, index=False)
