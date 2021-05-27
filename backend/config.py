VERSION = "0.0.1" # current version of the api
DEBUG = True # Turns on debugging features in Flask
BCRYPT_LOG_ROUNDS = 12 # Configuration for the Flask-Bcrypt extension
MAIL_FROM_EMAIL = "robert@example.com" # For use in application emails
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
HASH_METHOD = 'pbkdf2:sha1'