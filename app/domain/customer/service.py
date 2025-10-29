from fastapi import HTTPException, status

from app.domain.customer.repository import CustomerRepository
from app.domain.customer.schemas import ResponseCustomer, CreateCustomer, UpdateCustomer

class CustomerService:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def create(self, data: CreateCustomer):
        customer = self.repository.create(data)
        if customer:
            return customer
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não foi possível criar um novo cliente!")
    
    def get_all(self):
        customers = self.repository.get_all()
        if customers:
            return customers
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum cliente foi encontrado!")

    def get_by_id(self, customer_id: int):
        db_customer = self.repository.get_by_id(customer_id)
        if db_customer:
            return db_customer
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum cliente foi encontrado!")
    
    def update(self, customer_id: int, data: UpdateCustomer):
        db_customer = self.repository.get_by_id(customer_id)
        if db_customer:
            return self.repository.update(customer_id, data)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum cliente foi encontrado para atualização!")

    def delete(self, customer_id: int):
        db_customer = self.repository.get_by_id(customer_id)
        if db_customer:
            return self.repository.delete(customer_id)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum cliente foi encontrado!")