from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.token import LoginRequest
from app.services.auth_service import login_user

router = APIRouter()


@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    token = login_user(
        db,
        request.emailid,
        request.password
    )

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }