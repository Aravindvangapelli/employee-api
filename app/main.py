from fastapi import FastAPI

from app.core.database import engine, Base

from app.models.user import User
from app.models.employee import Employee

from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.employee import router as employee_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee API"
)

app.include_router(
    auth_router,
    prefix="/api/v1",
    tags=["Authentication"]
)
app.include_router(
    employee_router,
    prefix="/api/v1",
    tags=["Employees"]
)

@app.get("/")
def home():
    return {
        "message": "Employee API Running"
    }

