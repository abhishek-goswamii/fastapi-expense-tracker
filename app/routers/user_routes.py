from fastapi import APIRouter,status
from models.user import CreateUser
from services import user_service 
from fastapi import APIRouter

router = APIRouter()

@router.post("/user")
async def create_user(user_data: CreateUser,status_code=status.HTTP_200_OK):
    return user_service.create_user(user_data)


@router.get("/users")
async def get_users(status_code=status.HTTP_200_OK):
    return user_service.get_all_users()


   

    