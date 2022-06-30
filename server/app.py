import os
import db
import traceback
from flask_cors import CORS
from flask import Flask, json, make_response
from werkzeug.exceptions import HTTPException

from modules.users.controller import user_blueprint
from modules.auth.controller import auth_blueprint
from modules.cards.controller import cards_blueprint

app = Flask(__name__)
db.connect_to_db()

# CORS for frontend application
CORS(app, resources={r'/*': {'origins': '*'}})
app.config['CORS_HEADERS'] = 'Content-Type'

# Ping to server
@app.get('/')
def ping():
    return {'message': 'server is up!'}, 200
  
# Attach blueprints to app
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(cards_blueprint, url_prefix='/card')

# Error handling to JSON
@app.errorhandler(Exception)
def handle_exception(error: Exception):
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
        response = json.dumps({
            'code': 500,
            'name': 'internal server error',
            'description': traceback.format_exc()
        })
        response = make_response(response, 500)
        response.headers['Content-Type'] = 'application/json'
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('FLASK_PORT'), debug=True)
