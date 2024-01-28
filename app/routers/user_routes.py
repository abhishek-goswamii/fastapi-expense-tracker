from fastapi import APIRouter, HTTPException
from models.user import User
from services.user_service import create_user, root


router = APIRouter()

@router.get('/user')
def r():
    return root()


@router.post("/user", response_model=User)
async def create(user_data: User):
    try:
        user = create_user(user_data)
        return user
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error")