from fastapi import APIRouter, HTTPException
from models.user import User
from services.user_service import UserService


user_router = APIRouter()

service = UserService()

@user_router.post("/user", response_model=User)
async def create_user(user_data: dict):
    try:
        user = service.create_user(user_data)
        return user
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")