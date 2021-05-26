from flask import Blueprint

from models.db import db, User

users = Blueprint('users', __name__, template_folder='templates')

@users.route('/users')
def hello_world():
    db.session.add(User())
    db.session.commit()
    return 'Hello Max!'