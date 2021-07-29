import os
from app import create_app

# Importing local variable
config_name = os.environ.get('FLASK_CONFIG')
app = create_app(config_name)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)