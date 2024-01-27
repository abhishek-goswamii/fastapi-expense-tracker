from typing import Union
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from dotenv import dotenv_values
from config.db import connect_to_mongodb
from routers.user_routes import user_router
config = dotenv_values(".env")

app = FastAPI()

app.include_router(user_router)



mongodb_client, database = connect_to_mongodb()

