# app/routers/customer.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import get_db
from app.core.dependencies import get_current_active_user

router = APIRouter(prefix="/customer", tags=["customer"])

@router.get("/pizzas", response_model=list[schemas.Pizza])
def get_pizzas(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user),
    skip: int = 0,
    limit: int = 100
):
    return crud.pizza.get_multi(db, skip=skip, limit=limit)

@router.post("/cart/add", response_model=schemas.CartItem)
def add_to_cart(
    item: schemas.CartItemCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    return crud.cart.add_to_cart(db, user_id=current_user.id, pizza_id=item.pizza_id, quantity=item.quantity)

@router.delete("/cart/remove/{pizza_id}")
def remove_from_cart(
    pizza_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    crud.cart.remove_from_cart(db, user_id=current_user.id, pizza_id=pizza_id)
    return {"message": "Item removed from cart"}

@router.get("/cart", response_model=list[schemas.CartItem])
def get_cart(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    return crud.cart.get_user_cart(db, user_id=current_user.id)

@router.post("/orders", response_model=schemas.Order)
def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user)
):
    return crud.order.create_with_items(db, obj_in=order, user_id=current_user.id)

@router.get("/orders", response_model=list[schemas.Order])
def get_orders(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user),
    skip: int = 0,
    limit: int = 100
):
    return crud.order.get_user_orders(db, user_id=current_user.id, skip=skip, limit=limit)
