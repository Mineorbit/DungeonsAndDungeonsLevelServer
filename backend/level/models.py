from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime

from user.models import User
from util import Base


class LevelMetaData(Base):
    __tablename__ = "levels"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    upload_date = Column(DateTime)


class UserLevel(Base):
    __tablename__ = "users"
    level_id = Column(Integer, ForeignKey(LevelMetaData.id), primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True, index=True)


