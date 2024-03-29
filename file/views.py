from datetime import datetime

from base.views import Response


class FileOut(Response):
    id: int
    name: str
    type: str
    upload_date: datetime

    class Config:
        orm_mode = True