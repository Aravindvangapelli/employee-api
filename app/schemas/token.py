from pydantic import BaseModel


class LoginRequest(BaseModel):
    emailid: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str