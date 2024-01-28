from fastapi import APIRouter,status
from models.expense import ExpenseCreateRequest
from services import expenses_services 
from fastapi import APIRouter

router = APIRouter()

@router.post("/expense")
async def new_expense(expense_data: ExpenseCreateRequest, status_code=status.HTTP_200_OK):
    return expenses_services.create_new_expense(expense_data)

   
@router.get("/expenses")
async def new_expense(status_code=status.HTTP_200_OK):
    return expenses_services.get_all_expense()

   

    