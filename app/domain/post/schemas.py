from pydantic import BaseModel, ConfigDict
from typing import Optional, TYPE_CHECKING
import datetime

if TYPE_CHECKING:
	from app.domain.customer.schemas import ResponseCustomer

class ResponsePost(BaseModel):
	id: int
	description: str
	content: Optional[str]
	date: datetime.date
	schedule: bool
	customer: "ResponseCustomer"

	model_config = ConfigDict(
		from_attributes=True,
		arbitrary_types_allowed=True
	)

class CreatePost(BaseModel):
	description: str
	content: Optional[str] = None
	date: Optional[datetime.date] = None
	schedule: Optional[bool] = False
	customer_id: int

	model_config = ConfigDict(
		from_attributes=True,
	)

class UpdatePost(BaseModel):
	description: Optional[str]
	content: Optional[str]
	date: Optional[datetime.date]
	schedule: Optional[bool]

	model_config = ConfigDict(
		from_attributes=True,
	)
