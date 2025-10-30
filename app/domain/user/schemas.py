from pydantic import BaseModel, ConfigDict
from typing import Optional

from app.domain.customer.schemas import SimpleCustomer

class BaseUser(BaseModel):
    name: str
    email: str 
    login: str
    customers: list[SimpleCustomer]
    status: bool

class ReadUser(BaseUser):
    id: int

    model_config = ConfigDict(from_attributes=True)

class CreateUser(BaseUser):
    password: str

class UpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    status: Optional[bool] = None

class SimpleUser(BaseModel):
    id: int
    name: str
    status: bool