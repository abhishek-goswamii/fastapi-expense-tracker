from pydantic import BaseModel
from typing import List, Dict

class ExpenseCreateRequest(BaseModel):
    name: str
    amount: float
    expense_type: str
    participants: list
    paid_by: str

class ExpenseType(str):
    EQUAL = "EQUAL"
    EXACT = "EXACT"
    PERCENT = "PERCENT"

class ExpenseParticipant(BaseModel):
    user_id: str
    share: float

class Balance(BaseModel):
    user_id: str
    balances: Dict[str, float]

class Transaction(BaseModel):
    transaction_id: str
    payer: str
    payee: str
    amount: float
    timestamp: str