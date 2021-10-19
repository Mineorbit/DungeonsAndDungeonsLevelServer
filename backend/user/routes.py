from fastapi import APIRouter, Depends, HTTPException
from backend.decorators import proto_resp
from backend.user.controllers import get_current_active_user
from backend.user.views import UserCreate, UserOut
from backend.user import controllers as user_controller

router = APIRouter()



@router.get("/", tags=["user"])
@proto_resp
async def read_users():
    users = user_controller.get_users()
    usersOut = []
    for user in users:
        usersOut.append(UserOut.from_orm(user))
    return usersOut


@router.post("/", tags=["user"])
async def add_users(userCreate: UserCreate):
    return UserOut.from_orm(user_controller.create_user(userCreate))


@router.get("/me/", response_model=UserOut)
@proto_resp
async def read_users_me(current_user: UserOut = Depends(get_current_active_user)):
    return current_user


@router.get("/{username}", tags=["user"])
@proto_resp
async def read_user(username: str):
    result = user_controller.get_user(username)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return result


