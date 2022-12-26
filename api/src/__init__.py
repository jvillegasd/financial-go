import json
import traceback
from src.controllers import home_api
from werkzeug.exceptions import HTTPException
from src.config.app_config import config_by_name
from flask import Flask, make_response, Response


def _handle_exception(error: Exception) -> Response:
    """
      This method changes default HTML response format
      into JSON format for exceptions.
    """

    if isinstance(error, HTTPException):
        response = error.get_response()
        response.data = json.dumps({
            'code': error.code,
            'name': error.name,
            'description': error.description
        })

        response.content_type = 'application/json'
    else:
        traceback.print_exc()

        response = json.dumps({
            'code': 500,
            'name': 'internal server error',
            'description': 'Something is wrong here, try later'
        })
        response = make_response(response, 500)
        response.headers['Content-Type'] = 'application/json'
    
    return response


def create_app(config_name: str) -> Flask:
    """Creates a Flask application and loads configurations
    depending on the provided environment. After the application
    is created, current application context is pushed for 
    use loaded varibles outside context.
    Args:
        -   config_name: str = Enviroment configuration
    Returns:
        -   Flask = Flask application
    """

    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Push the Application context
    app.app_context().push()

    # Blueprints
    app.register_blueprint(home_api, url_prefix='/api')

    # Error handlers
    app.errorhandler(Exception)(_handle_exception)

    return app
