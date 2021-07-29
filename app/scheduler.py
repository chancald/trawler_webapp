from .models import Trawler, Predictions
from apscheduler.schedulers.background import BackgroundScheduler
import json
import os
from datetime import date

# Importing local variables
config_name = os.environ.get('FLASK_CONFIG')

# Creates table and graph data then writes them to json files
def write_json_files():
    # Initializing SQLAlchemy context
    from app import create_app
    app = create_app(config_name)
    app.app_context().push()

    # var used to store stocks to be used in the graph_data
    all_stocks = []

    # Serializes table data to JSON format and stores stock names to all_stocks
    def serialize(obj):
        if obj.stock not in all_stocks:
            all_stocks.append(obj.stock)
        return {
            'stock': obj.stock,
            'open' : str(round(obj.open, 2)),
            'high':str(round(obj.high, 2)),
            'low'  : str(round(obj.low, 2)),
            'close' : str(round(obj.close, 2)),
            'volume' : obj.volume,
            'mentions': obj.mentions,
        }

    # Querying table data
    latest_date = date(2021, 6, 27)
    query = Trawler.query.filter(Trawler.date == date(2021, 6, 22))
    # close, high and low columns are left out since they have the same order as the open column
    table_data = {'open_top_10': [serialize(row) for row in query.order_by(Trawler.open.desc()).limit(10).all()],
                    'volume_top_10': [serialize(row) for row in query.order_by(Trawler.volume.desc()).limit(10).all()],
                    'mentions_top_10': [serialize(row) for row in query.order_by(Trawler.mentions.desc()).limit(10).all()]
                }

    # Querying graph data
    graph_data = {}
    for stock in all_stocks:
        stock_rows = Trawler.query.filter(Trawler.stock == stock).order_by(Trawler.date.desc()).limit(182).all()
        format_rows = [[] for i in range(5)]
        for row in stock_rows:
            format_rows[0].append(row.date.strftime('%Y-%m-%d'))
            format_rows[1].append(str(row.mentions))
            format_rows[2].append(str(row.volume))
            
        graph_data[stock] = format_rows
    
    # Querying prediction data
    pred_data = {} 
    for stock in all_stocks:
        stock_row = Predictions.query.filter(Predictions.stock == stock, Predictions.date == latest_date)[0]
        pred_data[stock] = [
            stock_row.volume,
            stock_row.volume_confidence
        ]

    # Writing table, graph, prediction data to JSON files
    with open('app/files/table-data.json', 'w') as outfile:
        json.dump(table_data, outfile)
    with open('app/files/graph-data.json', 'w') as outfile:
        json.dump(graph_data, outfile)
    with open('app/files/prediction-data.json', 'w') as outfile:
        json.dump(pred_data, outfile)
    return False

# Starting CRON scheduler
sched = BackgroundScheduler(daemon=True)
sched.add_job(write_json_files,'cron', hour='6', minute="0")
sched.start()

# from app import create_app
# app = create_app(config_name)
# app.app_context().push()

# query = Predictions.query.filter(Predictions.date == date(2021, 6, 27)).limit(10).all()
# print("\n", query, "\n")
#write_json_files()