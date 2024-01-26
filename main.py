from fastapi import FastAPI
from config.db import connect_to_mongodb
from routers.user_routes import user_router

app = FastAPI()

# including user router 
app.include_router(user_router)

#db connection
mongodb_client, database = connect_to_mongodb()
