from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from base.routes import router as baseRouter
from user.routes import router as userRouter

SQLALCHEMY_DATABASE_URL = "sqlite:///database.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


app = FastAPI()
Base = declarative_base()

app.include_router(
    baseRouter,
    prefix='/base',
    tags=['base']
)

app.include_router(
    userRouter,
    prefix='/user',
    tags=['base']
)
