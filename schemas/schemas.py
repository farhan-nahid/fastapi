from typing import Optional

from pydantic import BaseModel


class Blog(BaseModel):
    title : str
    description: str
    published: Optional[bool]
    
    
class User(BaseModel):
    name: str
    email: str
    password: str