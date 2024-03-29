from http.client import HTTPException

from fastapi import Depends
from jose import jwt, JWTError

from auth.views import TokenData
from config import SECRET, ALGO
from user.models import User
from user.views import UserCreate
from util import SessionMaker, oauth2_scheme, pwd_context


def create_user(create: UserCreate):
    session = SessionMaker()
    user = User(
        name=create.name,
        email=create.email,
        hashed_password=pwd_context.hash(create.password)
    )
    session.add(user)
    session.commit()
    _id = user.id
    session.close()
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGO])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException()
        token_data = TokenData(username=username)
    except JWTError:
        raise HTTPException()
    user = get_user(username=token_data.username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    return current_user


def get_user(username: str):
    session = SessionMaker()
    user = session.query(User).filter(User.name == username).first()
    session.close()
    return user


def get_users():
    session = SessionMaker()
    users = session.query(User).all()
    session.close()
    return users


def create_access_token(data, expires_delta):
    pass


