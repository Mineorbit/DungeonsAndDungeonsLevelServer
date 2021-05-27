from user.models import User
from user.views import UserCreate
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from util import SessionMaker


def create_user(userCreate: UserCreate):
    session = SessionMaker()

    user = User(
        name=userCreate.name,
        email=userCreate.email,
        hashed_password=generate_password_hash(userCreate.password)
    )
    session.add(user)
    session.commit()
    _id = user.id
    return user


def authenticate(id: int, password: str):
    pass