from fastapi import APIRouter

user_router = APIRouter()

@user_router.get("/user")
async def root():
    return {"hellllooo"}

@user_router.post("/user")
async def root():
    
    return {"hellllooo"}
