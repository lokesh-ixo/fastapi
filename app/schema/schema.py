from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class userCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name: Optional[str]
    password : str

    class Config:
        orm_mode = True

class userOutput(BaseModel):
    email:EmailStr
    first_name:str
    last_name:str
    time_created:datetime

    class Config:
        orm_mode = True