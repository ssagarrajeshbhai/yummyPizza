# app/crud/cart.py
from typing import List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.cart import CartItem
from app.schemas.cart import CartItemCreate, CartItemUpdate

class CRUDCart(CRUDBase[CartItem, CartItemCreate, CartItemUpdate]):
    def get_user_cart(self, db: Session, *, user_id: int) -> List[CartItem]:
        return db.query(CartItem).filter(CartItem.user_id == user_id).all()

    def add_to_cart(self, db: Session, *, user_id: int, pizza_id: int, quantity: int = 1) -> CartItem:
        cart_item = db.query(CartItem).filter(
            CartItem.user_id == user_id,
            CartItem.pizza_id == pizza_id
        ).first()

        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = CartItem(user_id=user_id, pizza_id=pizza_id, quantity=quantity)
            db.add(cart_item)

        db.commit()
        db.refresh(cart_item)
        return cart_item

    def remove_from_cart(self, db: Session, *, user_id: int, pizza_id: int) -> None:
        db.query(CartItem).filter(
            CartItem.user_id == user_id,
            CartItem.pizza_id == pizza_id
        ).delete()
        db.commit()

    def clear_cart(self, db: Session, *, user_id: int) -> None:
        db.query(CartItem).filter(CartItem.user_id == user_id).delete()
        db.commit()

cart = CRUDCart(CartItem)