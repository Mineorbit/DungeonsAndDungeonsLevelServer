from datetime import datetime, timedelta
from typing import Optional

from jose import jwt

from config import SECRET, ALGO
from user.models import User
from util import SessionMaker, pwd_context
from werkzeug.security import check_password_hash


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET, algorithm=ALGO)
    return encoded_jwt


def authenticate_user(name: str, password: str):
    session = SessionMaker()
    print("Checking for "+name)
    user = session.query(User).filter(User.name == name).first()
    if user is None:
        return None
    else:
        print(user.hashed_password)
        if pwd_context.verify(password, user.hashed_password):
            return user
        else:
            print("Passwort falsch")
            return None