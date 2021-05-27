from fastapi import FastAPI
from base.routes import router as baseRouter
from user.routes import router as userRouter
from util import engine, Base

app = FastAPI()



Base.metadata.create_all(engine)


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
