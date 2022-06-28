import jwt
from functools import wraps
from typing import Callable
from flask import request, abort
import modules.auth.service as auth_service


def jwt_required(endpoint: Callable) -> Callable:
    """
      Wraps endpoints to check if request headers hav a valid
      authorization token.
      
      Args:
        - endpoint: Callable = Wrapped endpoint.
        
      Return:
        - endpoint: Callable = Wrapped endpoint in order to continue execution.
      
      Raise:
        - jwt.ExpiredSignatureError = Raised exception if JWT token is expired.
        - jwt.DecodeError = Raised exception if JWT token is invalid.
    """

    @wraps(endpoint)
    def wrapper(*args, **kwargs):
        if not 'Authorization' in request.headers:
            abort(401, 'Authorization token required.')
        else:
            try:
                auth_token = request.headers.get('Authorization')
                auth_service.decode_auth_token(auth_token)

                return endpoint(*args, **kwargs)
            except jwt.ExpiredSignatureError:
                abort(403, 'Authorization token expired.')
            except jwt.DecodeError:
                abort(400, 'Invalid authorization token.')

    return wrapper
