from datetime import datetime

from util import Base


class FileOut(Base):
    id: int
    name: str
    type: str
    creation_date: datetime


class LevelCreate(Base):
    name: str
    type:  str
