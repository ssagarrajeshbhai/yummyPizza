# app/schemas/pizza.py
from __future__ import annotations

from pydantic import BaseModel


class PizzaBase(BaseModel):
    name: str
    description: str
    price: float
    is_available: bool = True


class PizzaCreate(PizzaBase):
    pass


class PizzaUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    is_available: bool | None = None


class Pizza(PizzaBase):
    id: int

    class Config:
        orm_mode = True
