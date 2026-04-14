from pydantic import BaseModel

class TransactionResponse(BaseModel):
    transaction_id: int
    balance: float
    status: str
    user_id: int
    bank_account_id: int