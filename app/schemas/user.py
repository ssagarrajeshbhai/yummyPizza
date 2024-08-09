# app/schemas/user.py
from __future__ import annotations

from pydantic import BaseModel, EmailStr
from models.user import UserRole


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserLogin(BaseModel):
    username: str
    password: str


class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.CUSTOMER


class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None


class User(UserBase):
    id: int
    role: UserRole
    is_active: bool

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    role: UserRole | None = None
