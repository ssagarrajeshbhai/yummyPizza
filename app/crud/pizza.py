# app/crud/pizza.py
from app.crud.base import CRUDBase
from app.models.pizza import Pizza
from app.schemas.pizza import PizzaCreate, PizzaUpdate

class CRUDPizza(CRUDBase[Pizza, PizzaCreate, PizzaUpdate]):
    pass

pizza = CRUDPizza(Pizza)
