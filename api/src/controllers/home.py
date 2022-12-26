from flask import Blueprint

home_api = Blueprint('Home', __name__)


@home_api.route('/')
def home():
    return {'message': '🚀 Server is up!'}
