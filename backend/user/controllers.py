from user.models import User
from user.views import UserCreate
from util import SessionMaker


def create_user(userCreate: UserCreate):
    session = SessionMaker()
    user = User(
        name=userCreate.name
    )
    session.add(user)
    session.commit()

