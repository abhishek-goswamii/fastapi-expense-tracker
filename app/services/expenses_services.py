from fastapi import FastAPI, HTTPException,status
from config.database import expenses_collection
from models.expense import ExpenseCreateRequest

from datetime import datetime


app = FastAPI()


def create_new_expense(expense_data: ExpenseCreateRequest):
    try:
        expense_doc = {
            "name": expense_data.name,
            "amount": expense_data.amount,
            "expense_type": expense_data.expense_type,
            "participants": expense_data.participants,
            "paid_by": expense_data.paid_by,
            "timestamp": datetime.now(),
            "is_active": True
        }
        
        expenses_collection.insert_one(expense_doc)
        return {"status":"expense created"}        
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create expense")

def get_all_expense():
    try:
        all_documents = list(expenses_collection.find())
        for doc in all_documents:
            doc["_id"] = str(doc["_id"])
        return all_documents        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to get documents")