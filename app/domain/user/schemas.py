from pydantic import BaseModel, ConfigDict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.domain.customer.schemas import ResponseCustomer

class ResponseUser(BaseModel):
    id: int
    name: str
    email: str 
    login: str
    password: str
    customers: list["ResponseCustomer"]
    status: bool
    
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )

class ResponseUserSimple(BaseModel):
    id: int
    name: str
    email: str 
    login: str
    status: bool

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )

class CreateUser(BaseModel):
    name: str
    email: str
    login: str
    password: str

    model_config = ConfigDict(
        from_attributes=True,
    )

class UpdateUser(CreateUser):
    name: str
    email: str

    model_config = ConfigDict(
        from_attributes=True,
    )
