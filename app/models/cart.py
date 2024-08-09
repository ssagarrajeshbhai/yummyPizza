# app/models/cart.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class CartItem(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    pizza_id = Column(Integer, ForeignKey("pizzas.id"))
    quantity = Column(Integer, default=1)

    user = relationship("User", back_populates="cart")
    pizza = relationship("Pizza")