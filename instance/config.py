import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

SECRET_KEY = os.environ.get('SECRET_KEY')
db_admin = os.environ.get('MYSQL_USER')
db_password = os.environ.get('MYSQL_PASSWORD')
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://trawlerapp:zGHTpvEjQ5@frontier.cs.lewisu.edu:4306/DataSAIL'