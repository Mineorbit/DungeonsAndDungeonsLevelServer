from pydantic import BaseModel


class UserOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True