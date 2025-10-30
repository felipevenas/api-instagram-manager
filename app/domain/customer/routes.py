from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.domain.customer.model import Customer
from app.domain.customer.service import CustomerService
from app.domain.customer.repository import CustomerRepository
from app.domain.customer.schemas import ReadCustomer, SimpleCustomer, CreateCustomer, UpdateCustomer

customer_router = APIRouter()

def get_customer_service(db: Session = Depends(get_db)):
    repository = CustomerRepository(db)
    return CustomerService(repository)

@customer_router.post("/register", response_model=CreateCustomer, summary=["Criar um novo cliente"])
def create(data: CreateCustomer, service: CustomerService = Depends(get_customer_service)):
    return service.create(data)

@customer_router.get("/", response_model=list[SimpleCustomer], summary=["Buscar todos os clientes do sistema"])
def get_all(service: CustomerService = Depends(get_customer_service)):
    return service.get_all()

@customer_router.get("/{customer_id}", response_model=SimpleCustomer, summary=["Buscar um cliente pelo ID"])
def get_by_id(customer_id: int, service: CustomerService = Depends(get_customer_service)):
    return service.get_by_id(customer_id)

@customer_router.put("/{customer_id}", response_model=ReadCustomer, summary=["Editar um cliente pelo ID"])
def update(customer_id: int, data: UpdateCustomer, service: CustomerService = Depends(get_customer_service)):
    return service.update(customer_id, data)

@customer_router.delete("/{customer_id}", summary=["Deletar um cliente pelo ID"])
def delete(customer_id: int, service: CustomerService = Depends(get_customer_service)):
    return service.delete(customer_id)