# app/routers/admin.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import get_db
from app.core.dependencies import get_current_active_admin

router = APIRouter(prefix="/admin", tags=["admin"])

@router.post("/pizzas", response_model=schemas.Pizza)
def create_pizza(
    pizza: schemas.PizzaCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_admin)
):
    return crud.pizza.create(db=db, obj_in=pizza)

@router.put("/pizzas/{pizza_id}", response_model=schemas.Pizza)
def update_pizza(
    pizza_id: int,
    pizza: schemas.PizzaUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_admin)
):
    db_pizza = crud.pizza.get(db=db, id=pizza_id)
    if not db_pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")
    return crud.pizza.update(db=db, db_obj=db_pizza, obj_in=pizza)

@router.delete("/pizzas/{pizza_id}", response_model=schemas.Pizza)
def delete_pizza(
    pizza_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_admin)
):
    db_pizza = crud.pizza.get(db=db, id=pizza_id)
    if not db_pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")
    return crud.pizza.remove(db=db, id=pizza_id)

@router.put("/orders/{order_id}/status", response_model=schemas.Order)
def update_order_status(
    order_id: int,
    status: schemas.OrderUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_admin)
):
    db_order = crud.order.get(db=db, id=order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return crud.order.update(db=db, db_obj=db_order, obj_in=status)