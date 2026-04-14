from pydantic import BaseModel

class TransactionRequest(BaseModel):
    transaction_id: int
    credit: float
    debit: float
    user_id: int
    bank_account_id: int