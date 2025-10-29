from app.db.base_class import Base

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    login = Column(String(40), nullable=False)
    password = Column(String(40), nullable=False)
    email = Column(String(100), nullable=False)
    status = Column(Boolean, default=True)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="customers")
    posts = relationship("Post", back_populates="customer")