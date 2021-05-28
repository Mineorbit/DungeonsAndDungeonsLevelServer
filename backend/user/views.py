from typing import Optional, List

from pydantic import BaseModel


class UserOut(BaseModel):
    id: int
    name: str
    email: Optional[str]

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    name: str
    email: Optional[str]
    password: str

    class Config:
        orm_mode = True
