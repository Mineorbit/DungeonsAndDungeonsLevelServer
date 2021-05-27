from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app

db = SQLAlchemy()

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    password_hash = db.Column(db.String(80), unique=True, nullable=False)

    def set_password(self,password):
        self.password_hash = generate_password_hash(password,method=current_app.config['HASH_METHOD'])

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
