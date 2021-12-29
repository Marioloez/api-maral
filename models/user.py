from typing import Optional
from pydantic import BaseModel



class User(BaseModel):
    id: Optional[str]
    Name : str
    Email  : str
    password : str