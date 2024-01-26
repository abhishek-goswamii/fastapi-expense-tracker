

class UserService:
    def create_user(self, user_data: dict) -> User:
        user = User(**user_data)
        return user