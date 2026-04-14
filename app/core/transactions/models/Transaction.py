from sqlalchemy import Column, Integer, String
from app.core.db.DBConnection import Base

class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    cred_amount = Column(Integer, index=True)
    debit_amount = Column(Integer, index=True)
    status = Column(String, index=True)
    created_at = Column(String, index=False)
    updated_at = Column(String, index=False)