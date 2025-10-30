from app.db.base_class import Base

from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
import datetime

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(500), nullable=False)
    content = Column(String(300), nullable=True)
    date = Column(Date, default=datetime.date.today)
    schedule = Column(Boolean, default=False)

    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="posts")