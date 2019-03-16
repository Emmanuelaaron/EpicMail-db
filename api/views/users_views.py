from flask import Blueprint


users_blueprint = Blueprint("Users", __name__, url_prefix="/api/v1")

@users_blueprint.route('/')
def index():
    return "You're welcome to EpicMail"