from fastapi import APIRouter,status
from services import balance_service
from fastapi import APIRouter

router = APIRouter()

@router.get("/balances")
async def get_all_balances(status_code=status.HTTP_200_OK):
    return balance_service.get_all_balances()


@router.get("/balance/{user_id}")
async def balance_with_id(user_id: str, status_code=status.HTTP_200_OK):
    return balance_service.get_balance(user_id)
