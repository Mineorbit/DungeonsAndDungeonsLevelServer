from sqlalchemy import Column, Integer, String, Boolean

from util import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String,unique=True,index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)