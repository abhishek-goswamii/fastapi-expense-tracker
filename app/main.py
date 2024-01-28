from fastapi import FastAPI
from routers import user_routes,expense_routes
app = FastAPI()

app.include_router(user_routes.router)
app.include_router(expense_routes.router)


