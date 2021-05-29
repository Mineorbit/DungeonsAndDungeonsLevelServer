

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Sequence

from file.models import File
from util import Base


class LevelMetaData(Base):
    __tablename__ = "level"
    uniqueGlobalLevelId = Column(Integer, Sequence('level_level_id_seq'), primary_key=True)
    name = Column(String, unique=True, index=True, primary_key=True)
    upload_date = Column(DateTime)
    file_id = Column(Integer, ForeignKey(File.id), primary_key=True, index=True)
