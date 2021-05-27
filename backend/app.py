from flask import Flask
from base.views import base_app
from users.create.views import users_create_app
def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from users.models import db
    db.app = app
    db.init_app(app)
    db.create_all()

    app.register_blueprint(base_app)
    app.register_blueprint(users_create_app)
    return app