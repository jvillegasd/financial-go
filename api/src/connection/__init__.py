

from flask import g
from src.connection.database import DataAccessLayer


def get_dal() -> DataAccessLayer:
    """Store a Data Access Layer instance in Flask
    Application context for use this across requests.
    Returns:
        -   DataAccessLayer
    """

    if 'dal' not in g:
        g.dal = DataAccessLayer()

    return g.dal
