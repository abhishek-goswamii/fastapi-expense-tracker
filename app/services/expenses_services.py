from fastapi import FastAPI, HTTPException,status
from config.database import expenses_collection,balances_collection
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
        update_balances(expense_data)
        return {"status":"expense created"}        
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create expense")

def get_all_expense():
    """
    returns list of all expenses
    """
    try:
        all_documents = list(expenses_collection.find())
        for doc in all_documents:
            doc["_id"] = str(doc["_id"])
        return all_documents        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to get documents")

        

def update_balances(expense_data: ExpenseCreateRequest):
    try:
        # Get the existing balances for each participant
        for participant in expense_data.participants:
            participant_id = participant['user_id']

            existing_balance = balances_collection.find_one({'user_id': participant_id})

            # If the user does not have an existing balance
            if existing_balance is None:
                existing_balance = {'user_id': participant_id, 'balances': {}}

            # Update the balance for the paid_by user
            paid_by = expense_data.paid_by
            
            if paid_by != participant_id:
                
                share = participant['share']
                
                if expense_data.expense_type == 'EQUAL':
                    share_amount = expense_data.amount / len(expense_data.participants)
                elif expense_data.expense_type == 'EXACT':
                    share_amount = share
                elif expense_data.expense_type == 'PERCENT':
                    share_amount = (share / 100) * expense_data.amount
                else:
                    raise ValueError("Invalid expense type")

                existing_balance['balances'][paid_by] = existing_balance['balances'].get(paid_by, 0) - share_amount

            # Update the balances collection
            balances_collection.update_one({'user_id': participant_id}, {'$set': existing_balance}, upsert=True)
            
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to update balances")
