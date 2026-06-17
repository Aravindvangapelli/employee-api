from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeUpdate
)

from app.services.employee_service import (
    create_employee_service,
    list_employees_service,
    get_employee_service,
    update_employee_service,
    delete_employee_service
)

router = APIRouter()


@router.post("/employees")
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    return create_employee_service(
        db,
        employee.model_dump()
    )


@router.get("/employees")
def get_all_employees(
    db: Session = Depends(get_db)
):
    return list_employees_service(db)


@router.get("/employees/{employee_id}")
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = get_employee_service(
        db,
        employee_id
    )

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee


@router.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    updated_employee = update_employee_service(
        db,
        employee_id,
        employee.model_dump()
    )

    if not updated_employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return updated_employee


@router.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_employee_service(
        db,
        employee_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully"
    }