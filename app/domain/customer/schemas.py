from pydantic import BaseModel, ConfigDict
from typing import Optional

class BaseCustomer(BaseModel):
    name: str
    email: str
    login: str
    user_id: int
    status: bool

class ReadCustomer(BaseCustomer):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )

class CreateCustomer(BaseCustomer):
    password: str

class UpdateCustomer(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    login: Optional[str] = None
    status: Optional[bool] = None

class SimpleCustomer(BaseModel):
    id: int
    name: str
    login: str
    status: bool