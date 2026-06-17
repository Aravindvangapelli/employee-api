from app.repositories.employee_repository import (
    create_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee,
    delete_employee
)


def create_employee_service(
    db,
    employee_data
):
    return create_employee(
        db,
        employee_data
    )


def list_employees_service(db):
    return get_all_employees(db)


def get_employee_service(
    db,
    employee_id
):
    return get_employee_by_id(
        db,
        employee_id
    )


def update_employee_service(
    db,
    employee_id,
    employee_data
):
    return update_employee(
        db,
        employee_id,
        employee_data
    )


def delete_employee_service(
    db,
    employee_id
):
    return delete_employee(
        db,
        employee_id
    )