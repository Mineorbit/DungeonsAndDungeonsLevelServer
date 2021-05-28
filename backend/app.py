
from fastapi import FastAPI

from base.routes import router as baseRouter
from user.routes import router as userRouter
from auth.routes import router as authRouter
from util import engine, Base

app = FastAPI()


Base.metadata.create_all(engine)









app.include_router(
    baseRouter,
    prefix='',
    tags=['base']
)

app.include_router(
    userRouter,
    prefix='/user',
    tags=['user']
)


app.include_router(
    authRouter,
    prefix='/auth',
    tags=['auth']
)