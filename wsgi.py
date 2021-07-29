import os
from app import create_app


config_name = os.environ.get('FLASK_CONFIG')
app = create_app('development')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == "__main__":
    app.run()