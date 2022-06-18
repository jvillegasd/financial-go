import os
import traceback
from flask_cors import CORS
from flask import Flask, jsonify, json, make_response
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# CORS for frontend application
CORS(app, resources={r'/*': {'origins': '*'}})
app.config['CORS_HEADERS'] = 'Content-Type'

# Ping to server
@app.get('/')
def ping():
    return {'message': 'server is up!'}, 200

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
