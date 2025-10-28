from pydantic import BaseModel, ConfigDict
from typing import List

from app.domain.customer.schemas import ResponseCustomer

class ResponseUser(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )

    id: int
    name: str
    email: str 
    login: str
    password: str
    customers: list[ResponseCustomer]
    status: bool

class CreateUser(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
    )

    name: str
    email: str
    login: str
    password: str

class UpdateUser(CreateUser):

    model_config = ConfigDict(
        from_attributes=True,
    )

    name: str
    email: str
