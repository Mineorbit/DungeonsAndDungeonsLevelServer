
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from base.routes import router as baseRouter
from user.routes import router as userRouter
from auth.routes import router as authRouter
from file.routes import router as fileRouter
from level.routes import router as levelRouter
from util import engine, Base

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
try:
    Base.metadata.create_all(engine)
except Exception as e:
    print(e)







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


app.include_router(
    fileRouter,
    prefix='/file',
    tags=['file']
)


app.include_router(
    levelRouter,
    prefix='/level',
    tags=['level']
)