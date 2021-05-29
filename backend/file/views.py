from datetime import datetime

from pydantic import BaseModel


class FileOut(BaseModel):
    id: int
    name: str
    type: str
    upload_date: datetime

    class Config:
        orm_mode = True