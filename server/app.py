import os
import db
import logging
import traceback

from flask_cors import CORS
from flask import Flask, json, make_response
from werkzeug.exceptions import HTTPException

from modules.users.controller import user_blueprint
from modules.auth.controller import auth_blueprint
from modules.cards.controller import cards_blueprint
from modules.transactions.controller import transaction_blueprint

app = Flask(__name__)
db.connect_to_db()

logging.basicConfig(level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

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
app.register_blueprint(transaction_blueprint, url_prefix='/transaction')

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
        app.logger.error(traceback.format_exc())
        
        response = json.dumps({
            'code': 500,
            'name': 'internal server error',
            'description': 'Internal server error'
        })
        response = make_response(response, 500)
        response.headers['Content-Type'] = 'application/json'
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('FLASK_PORT'), debug=True)
