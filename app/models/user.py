# app/models/user.py
from sqlalchemy import Column, Integer, String, Enum, Boolean
from app.database import Base
import enum

class UserRole(str, enum.Enum):
    CUSTOMER = "customer"
    DELIVERY_PARTNER = "delivery_partner"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(UserRole), default=UserRole.CUSTOMER)
    is_active = Column(Boolean, default=True)