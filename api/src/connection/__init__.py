

from src.connection.database import DataAccessLayer

_dal: DataAccessLayer = None


def get_dal() -> DataAccessLayer:
    """Store a Data Access Layer instance in Flask
    Application context for use this across requests.
    Returns:
        -   DataAccessLayer
    """

    global _dal
    if _dal is None:
        _dal = DataAccessLayer()

    return _dal
