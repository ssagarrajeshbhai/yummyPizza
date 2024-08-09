# app/crud/order.py
from typing import List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.order import Order, OrderItem
from app.schemas.order import OrderCreate, OrderUpdate

class CRUDOrder(CRUDBase[Order, OrderCreate, OrderUpdate]):
    def create_with_items(self, db: Session, *, obj_in: OrderCreate, user_id: int) -> Order:
        db_obj = Order(user_id=user_id, total_amount=0)
        for item in obj_in.items:
            order_item = OrderItem(**item.dict(), order=db_obj)
            db.add(order_item)
            db_obj.total_amount += order_item.unit_price * order_item.quantity
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_user_orders(self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100) -> List[Order]:
        return db.query(Order).filter(Order.user_id == user_id).offset(skip).limit(limit).all()

order = CRUDOrder(Order)
