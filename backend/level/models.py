

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Sequence, Enum, UnicodeText, Text
import enum
from sqlalchemy.orm import relationship

from backend.util import Base
from backend.file.models import File
from backend.user.models import User


class Utility(enum.Enum):
    LEVELDATA = 1
    IMAGE = 2
    THUMBNAIL = 3


class Level(Base):
    __tablename__ = "level"
    ulid = Column(Integer, primary_key=True)
    name = Column(String)
    upload_date = Column(DateTime)
    description = Column(Text)


class LevelDownload(Base):
    __tablename__ = "level_download"
    level_id = Column(Integer, ForeignKey(Level.ulid, ondelete="CASCADE"), primary_key=True, index=True)
    downloads = Column(Integer)


class UserLevel(Base):
    __tablename__ = "user_level"
    level_id = Column(Integer, ForeignKey(Level.ulid, ondelete="CASCADE"), primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"), primary_key=True, index=True)




class LevelFile(Base):
    __tablename__ = "level_file"
    level_id = Column(Integer, ForeignKey(Level.ulid, ondelete="CASCADE"), primary_key=True, index=True)
    file_id = Column(Integer, ForeignKey(File.id, ondelete="CASCADE"), primary_key=True, index=True)
    type = Column(Enum(Utility), default=Utility.LEVELDATA)
