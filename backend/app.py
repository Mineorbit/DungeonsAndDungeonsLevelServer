from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from user import User

app = Flask(__name__)


app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)



@app.route('/')
def hello_world():
    user = User("Test")
    return 'Hello '+user.username+'!'


if __name__ == '__main__':
    app.run()
