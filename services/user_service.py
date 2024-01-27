from models.user import User
from config.db import connect_to_mongodb

mongodb_client, database = connect_to_mongodb()

class UserService:
    def create_user(self, user_data: dict) -> User:
        

        name = user_data.get("name")
        email = user_data.get("email")
        number = user_data.get("number")
        password = user_data.get("password")
        

        existing_user = database["users"].find_one({"email": email})
        if existing_user:
            raise ValueError("User with this email already exists")
        
        user_document = {
            "name": name,
            "email": email,
            "number": number,
            "password": password
        }
        
        database["users"].insert_one(user_document)
        return User(**user_data)