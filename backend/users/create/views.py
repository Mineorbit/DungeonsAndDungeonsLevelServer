from flask import Blueprint, current_app

from users.models import User, db

users_create_app = Blueprint('users_create',__name__)


@users_create_app.route("/users")
def create_user():
    user = User(
        username = "Test"
    )
    user.set_password("Testpasswort")
    db.session.add(user)
    db.session.commit()
    return "New User "+user.id.__str__()