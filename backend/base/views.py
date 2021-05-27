from flask import Blueprint, current_app

base_app = Blueprint('base_app',__name__)


@base_app.route("/")
def welcome():
    return "Welcome to the Dungeons and Dungeons LevelServer API v"+current_app.config['VERSION']
