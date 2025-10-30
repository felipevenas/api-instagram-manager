from pydantic import BaseModel, ConfigDict
from typing import Optional
import datetime

class BasePost(BaseModel):
	description: str
	content: Optional[str] = None
	date: Optional[datetime.date] = None
	schedule: Optional[bool] = False
	customer_id: int

class ReadPost(BasePost):
	id: int

	model_config = ConfigDict(from_attributes=True)

class CreatePost(BasePost):
	pass

class UpdatePost(BaseModel):
	description: Optional[str] = None
	content: Optional[str] = None
	date: Optional[datetime.date] = None
	schedule: Optional[bool] = False
