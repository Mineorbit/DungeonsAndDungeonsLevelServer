from datetime import datetime

from fastapi import UploadFile
from pydantic import BaseModel


class LevelOut(BaseModel):
    uniqueGlobalLevelId: int
    name: str
    upload_date: datetime

    class Config:
        orm_mode = True


class LevelCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True