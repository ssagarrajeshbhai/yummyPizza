# app/routers/delivery.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import get_db
from app.core.dependencies import get_current_active_delivery_partner

router = APIRouter(prefix="/delivery", tags=["delivery"])

@router.put("/orders/{order_id}/status", response_model=schemas.Order)
def update_order_status(
    order_id: int,
    status: schemas.OrderUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_delivery_partner)
):
    db_order = crud.order.get(db=db, id=order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return crud.order.update(db=db, db_obj=db_order, obj_in=status)

@router.post("/orders/{order_id}/comment", response_model=schemas.Order)
def add_order_comment(
    order_id: int,
    comment: str,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_delivery_partner)
):
    db_order = crud.order.get(db=db, id=order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    # Assuming you have a 'comment' field in your Order model
    return crud.order.update(db=db, db_obj=db_order, obj_in={"comment": comment})