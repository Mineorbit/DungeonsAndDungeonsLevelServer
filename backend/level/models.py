

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Sequence

from file.models import File
from user.models import User
from util import Base


class Level(Base):
    __tablename__ = "level"
    ulid = Column(Integer, primary_key=True)
    name = Column(String)
    upload_date = Column(DateTime)




class UserLevel(Base):
    __tablename__ = "user_level"
    level_id = Column(Integer, ForeignKey(Level.ulid), primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True, index=True)




class LevelFile(Base):
    __tablename__ = "level_file"
    level_id = Column(Integer, ForeignKey(Level.ulid), primary_key=True, index=True)
    file_id = Column(Integer, ForeignKey(File.id), primary_key=True, index=True)


