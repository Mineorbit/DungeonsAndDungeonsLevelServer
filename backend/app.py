from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config
from config import version
from routes.users import users
from models.db import db

app = Flask(__name__)


app.config.from_object(Config)


migrate = Migrate(app, db)

db.app = app
db.init_app(app)
db.create_all()

app.register_blueprint(users)

@app.route("/")
def welcome():
    return "Welcome to the Dungeons And Dungeons Level Server API v"+version


if __name__ == '__main__':
    app.run()
    db.create_all()



