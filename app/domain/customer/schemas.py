from pydantic import BaseModel, ConfigDict

class ResponseCustomer(BaseModel):

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )

    name: str
    email: str
    login: str