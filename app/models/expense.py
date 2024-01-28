from pydantic import BaseModel
from typing import List, Dict


class ExpenseType(str):
    EQUAL = "EQUAL"
    EXACT = "EXACT"
    PERCENT = "PERCENT"


class ExpenseParticipant(BaseModel):
    user_id: str
    share: float


class Expense(BaseModel):
    name: str
    amount: float
    expense_type: ExpenseType
    participants: List[ExpenseParticipant]
    paid_by: str


class Balance(BaseModel):
    user_id: str
    balances: Dict[str, float]


class Transaction(BaseModel):
    transaction_id: str
    payer: str
    payee: str
    amount: float
    timestamp: str