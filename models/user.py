from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
  name: Optional[str]
  email:Optional[str]
  password:Optional[str]