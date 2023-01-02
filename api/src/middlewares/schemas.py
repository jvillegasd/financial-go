from typing import Callable
from functools import wraps
from marshmallow import Schema
from flask import request, abort


def parameters(schema: Schema) -> Callable:
    """Wraps endpoints to check if request body matches
    with provided schema.
    Args:
        -   schema: Schema = Provided schema used to check
        request body make a match.
        -   endpoint: Callable = Wrapped endpoint.
    Return:
        - endpoint: Callable = Wrapped endpoint in order to continue
        execution.
    Raise:
        -   abort: HTTPException = Raised exception if provided request body
        does not match with schema.
    """
    def decorator(endpoint: Callable) -> Callable:
        @wraps(endpoint)
        def wrapper(*args, **kwargs) -> Callable:
            body = request.get_json()
            errors = schema.validate(body)
            if errors:
                abort(400, str(errors))
            else:
                return endpoint(*args, **kwargs)
        return wrapper
    return decorator
