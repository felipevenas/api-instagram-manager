from sqlalchemy.orm import Session

from app.domain.customer.model import Customer
from app.domain.customer.schemas import CreateCustomer, UpdateCustomer, ReadCustomer, SimpleCustomer

class CustomerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: CreateCustomer) -> Customer:
        customer = Customer(**data.model_dump())
        self.db.add(customer)
        self.db.commit()
        return customer
    
    def get_all(self) -> list[SimpleCustomer]:
        return self.db.query(Customer).all()
    
    def get_by_id(self, customer_id: int) -> SimpleCustomer | None:
        db_customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
        if db_customer:
            return db_customer
        return None
    
    def update(self, user_id: int, data: UpdateCustomer) -> SimpleCustomer | None:
        db_customer = self.get_by_id(user_id)
        if db_customer:
            for key, value in data.model_dump().items():
                setattr(db_customer, key, value)
        self.db.commit()
        self.db.refresh(db_customer)
        return db_customer

    def delete(self, customer_id: int):
        db_customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
        if db_customer:
            self.db.delete(db_customer)
            self.db.commit()
            return
        return None