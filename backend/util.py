from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

SQLALCHEMY_DATABASE_URL = "postgresql://db:db@46.232.248.108/api"

SQLALCHEMY_DATABASE_SQLITE_URL = "sqlite:///"+config.PERMANENT_DATA+"/database.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Base = declarative_base()
SessionMaker = sessionmaker(bind=engine)