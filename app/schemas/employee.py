from pydantic import BaseModel, EmailStr
from datetime import datetime


class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    emailid: EmailStr
    department: str
    salary: float
    status_id: int


class EmployeeUpdate(BaseModel):
    first_name: str
    last_name: str
    emailid: EmailStr
    department: str
    salary: float
    status_id: int


class EmployeeResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    emailid: EmailStr
    department: str
    salary: float
    status_id: int
    added_date: datetime

    class Config:
        from_attributes = True