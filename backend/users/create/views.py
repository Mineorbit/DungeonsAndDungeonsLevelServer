from flask import Blueprint, current_app
from flask_pydantic import validate
from pydantic import BaseModel

from users.models import User, db

users_create_app = Blueprint('users_create',__name__)

class CreateUser(BaseModel):
    name: str
    password: str

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True



@users_create_app.route('/users', methods=['POST'])
def register(create: CreateUser):
    user = User(
        username=create.name)
    user.set_password(create.password)
    return UserOut.from_orm(user)


@users_create_app.route('/users/', methods=['GET'])
def read():
    c = CreateUser(name = "Max",
                   password = "Test")
    return CreateUser.from_orm(c)