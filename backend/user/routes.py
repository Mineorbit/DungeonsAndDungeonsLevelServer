from datetime import timedelta
from http.client import HTTPException

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from config import ACCESS_TOKEN_EXPIRE_MINUTES
from user.controllers import get_current_active_user
from user.views import UserCreate, UserOut
from user import controllers as user_controller

router = APIRouter()



@router.get("/", tags=["users"])
async def read_users():
    pass


@router.post("/", tags=["users"])
async def add_users(userCreate: UserCreate):
    return UserOut.from_orm(user_controller.create_user(userCreate))


@router.get("/me/", response_model=UserOut)
async def read_users_me(current_user: UserOut = Depends(get_current_active_user)):
    return current_user


@router.get("/{username}", tags=["users"])
async def read_user(username: str):
    pass


