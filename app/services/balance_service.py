from fastapi import HTTPException,status
from config.database import balances_collection



def get_balance(user_id:str):
    """
    fetch balance with user id
    """
    try:
        document = balances_collection.find_one({"user_id":user_id},  {'_id': 0})
        net_balance = 0
        if document:

            for balance in document.get("balances", {}).values():
                net_balance += balance

            document["my_net_balance"] = net_balance
            return document
        else:
            return None

    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to get documents")


def get_all_balances():
    """
    returns list of all balances
    """
    try:
        all_documents = list(balances_collection.find())
        for doc in all_documents:
            doc["_id"] = str(doc["_id"])
        return all_documents        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to get documents")
