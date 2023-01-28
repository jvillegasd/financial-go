import os
from src.main import create_app
from src.connection import DataAccessLayer


port = os.getenv('FLASK_PORT', 5001)
app = create_app(config_name=os.getenv('APP_ENV', 'dev'))


if __name__ == '__main__':
    DataAccessLayer()
    app.run(host='0.0.0.0', port=port)
