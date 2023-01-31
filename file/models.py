from sqlalchemy import Column, Integer, String, DateTime

from util import Base


class File(Base):
    __tablename__ = "file"
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    type = Column(String(64))
    upload_date = Column(DateTime)
