from pydantic import BaseModel


class UserOut(BaseModel):
    id: int
    name: str


class UserCreate(BaseModel):
    name: str
    password: str