from datetime import datetime

from fastapi import UploadFile
from pydantic import BaseModel


class LevelOut(BaseModel):
    ulid: int
    name: str
    upload_date: datetime
    description: str

    class Config:
        orm_mode = True


class LevelCreate(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True