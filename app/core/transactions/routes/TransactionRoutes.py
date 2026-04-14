from fastapi import APIRouter

from app.core.transactions.models.TransactionRequest import TransactionRequest

router = APIRouter()

@router.get("/is_alive")
def is_alive():
    return {"status": "alive"}

@router.get("/get_incomplete_transactions")
def get_incomplete_transactions():
    # Placeholder for fetching incomplete transactions from the database
    incomplete_transactions = [
        {"id": 1, "amount": 100, "status": "incomplete"},
        {"id": 2, "amount": 200, "status": "incomplete"}
    ]
    return {"incomplete_transactions": incomplete_transactions}
    
@router.post("/new_transaction")
def new_transaction(Request: TransactionRequest):
    # Placeholder for creating a new transaction in the database
    return {"message": "Transaction created successfully", "transaction_data": Request.dict()}

@router.put("/update_transaction/{transaction_id}")
def update_transaction(transaction_id: int, Transaction: TransactionRequest):
    # Placeholder for updating a transaction in the database
    return {"message": f"Transaction {transaction_id} updated successfully", "transaction_data": Transaction.dict()}

@router.delete("/delete_transaction/{transaction_id}")
def delete_transaction(transaction_id: int):
    # Placeholder for deleting a transaction from the database
    return {"message": f"Transaction {transaction_id} deleted successfully"}