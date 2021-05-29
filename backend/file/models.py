from sqlalchemy import Column, Integer, String, DateTime

from util import Base


class File(Base):
    __tablename__ = "file"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    upload_date = Column(DateTime)