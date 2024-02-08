from typing import Optional
from pydantic import BaseModel


class Blog(BaseModel):
  title: str
  body: str
  published: bool = True
  isAuthor: Optional[bool] = False