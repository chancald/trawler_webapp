
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql.cursors
import json
import os
from dotenv import load_dotenv

# Local imports
from config import app_config


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

db = SQLAlchemy()

def create_app(config_name):
    
    # Connecting to the database and starting app
    connection = pymysql.connect(host='frontier.cs.lewisu.edu',
                             port= 4306,
                             user='trawlerapp',
                             password='zGHTpvEjQ5',
                             db='DataSAIL',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def home():

        # Reading table and graph data
        with open('app/files/table-data.json') as f:
            table_data = json.load(f)
        with open('app/files/graph-data.json') as f:
            graph_data = json.load(f)
        with open('app/files/prediction-data.json') as f:
            pred_data = json.load(f)

        return render_template('home.html', table_data=table_data, graph_data=graph_data, pred_data=pred_data)
    
    from app import models, scheduler

    return app
