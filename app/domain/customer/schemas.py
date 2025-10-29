from pydantic import BaseModel, ConfigDict
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.domain.user.schemas import ResponseUser

class ResponseCustomer(BaseModel):
    id: int
    name: str
    email: str
    login: str
    password: str
    owner: "ResponseUser"
    status: bool

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )

class ResponseCustomerSimple(BaseModel):
    id: int
    name: str
    email: str
    login: str
    status: bool

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )

class CreateCustomer(BaseModel):
    name: str
    email: str
    login: str
    password: str
    user_id: Optional[int] = None
    status: bool = True

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )

class UpdateCustomer(BaseModel):
    name: str
    email: str
    login: str
    status: bool

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )