from fastapi import APIRouter,status
from models.user import User
from services import user_service 
from fastapi import APIRouter

router = APIRouter()

@router.post("/user")
async def create_user(user_data: User,status_code=status.HTTP_200_OK):
    return user_service.create_user(user_data)

   

    