from app.db.base_class import Base

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    login = Column(String(40), nullable=False)
    password = Column(String(40), nullable=False)
    email = Column(String(100), nullable=False)
    status = Column(Boolean, default=True)
    
    customers = relationship("Customer", back_populates="owner")