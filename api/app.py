import os
from src.main import create_app
from src.connection import get_dal


port = os.getenv('FLASK_PORT', 5001)
app = create_app(config_name=os.getenv('APP_ENV', 'dev'))


if __name__ == '__main__':
    get_dal()
    app.run(host='0.0.0.0', port=port)
