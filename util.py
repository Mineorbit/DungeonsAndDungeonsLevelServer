from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


if config.DB_TYPE == "PSQL":
    SQLALCHEMY_DATABASE_URL = "postgresql://api:api@0.0.0.0/dungeonsanddungeonsapi"
elif config.DB_TYPE == "MSQL":
    SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://api:api@localhost:3306/dungeonsanddungeonsapi"
else:
    SQLALCHEMY_DATABASE_URL = "sqlite:///" + config.PERMANENT_DATA + "/database.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Base = declarative_base()
SessionMaker = sessionmaker(bind=engine)
