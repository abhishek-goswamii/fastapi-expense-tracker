from fastapi import FastAPI, HTTPException
from config.database import users_collection
from models.user import User

app = FastAPI()


def create_user(user_data: User):
    """
    creates new user in database
    """
    try:
        existing_user = users_collection.find_one({"email": user_data.email})

        if existing_user:
            raise HTTPException(status_code=400, detail="User with the same email already exists")

        user_id = users_collection.insert_one(user_data.model_dump()).inserted_id
        return {"user_id": str(user_id)}

    except HTTPException as http_exception:
        raise http_exception
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    



def get_all_users():
    """
    Retrieve all users from the database
    """
    try:

        all_documents = list(users_collection.find())
        # all_documents = list(users_collection.find( {},{"password": 0}))

        for doc in all_documents:
            doc['_id'] = str(doc['_id'])
        
        return all_documents
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")