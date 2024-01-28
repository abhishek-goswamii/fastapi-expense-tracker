from models.user import User
from config.db import db

def root():
    return "hey"

def create_user(user_data: User):
    try:
        name = user_data.get("name")
        email = user_data.get("email")
        number = user_data.get("number")
        password = user_data.get("password")

        print(name,email,number,password)

        user_collection_ref = db["users"]
        
        existing_user = user_collection_ref.find_one({"email": email})

        if existing_user:
            raise ValueError("User with this email already exists")
        
        user_document = {
            "name": name,
            "email": email,
            "number": number,
            "password": password
        }
        
        user_collection_ref.insert_one(user_document)
        
        return User(**user_data)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    