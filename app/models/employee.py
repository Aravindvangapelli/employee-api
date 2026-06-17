from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.core.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    emailid = Column(String, unique=True, nullable=False)

    department = Column(String, nullable=False)

    salary = Column(Float, nullable=False)

    status_id = Column(Integer, nullable=False)

    added_date = Column(DateTime, default=datetime.utcnow)