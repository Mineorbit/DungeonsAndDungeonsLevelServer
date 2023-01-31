from sqlalchemy import Column, Integer, String, Boolean

from util import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), unique=True, index=True)
    email = Column(String(40), unique=True, index=True)
    hashed_password = Column(String(40))
    is_active = Column(Boolean, default=True)
