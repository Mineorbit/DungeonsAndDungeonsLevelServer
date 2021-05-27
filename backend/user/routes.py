from fastapi import APIRouter

from user.views import UserCreate, UserOut
from user import controllers as user_controller

router = APIRouter()



@router.get("/users/", tags=["users"])
async def read_users():
    pass


@router.post("/users/", tags=["users"])
async def add_users(userCreate: UserCreate):
    return UserOut.from_orm(user_controller.create_user(userCreate))


@router.get("/users/me", tags=["users"])
async def read_user_me():
    pass


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    pass