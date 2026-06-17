from sqlalchemy.orm import Session
from app.models.employee import Employee


def create_employee(db: Session, employee_data: dict):
    employee = Employee(**employee_data)

    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee


def get_all_employees(db: Session):
    return db.query(Employee).all()


def get_employee_by_id(db: Session, employee_id: int):
    return (
        db.query(Employee)
        .filter(Employee.id == employee_id)
        .first()
    )


def update_employee(
    db: Session,
    employee_id: int,
    employee_data: dict
):

    employee = get_employee_by_id(
        db,
        employee_id
    )

    if not employee:
        return None

    for key, value in employee_data.items():
        setattr(employee, key, value)

    db.commit()
    db.refresh(employee)

    return employee


def delete_employee(
    db: Session,
    employee_id: int
):

    employee = get_employee_by_id(
        db,
        employee_id
    )

    if not employee:
        return False

    db.delete(employee)
    db.commit()

    return True