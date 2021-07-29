from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Trawler(db.Model):
    __tablename__ = 'Trawler'

    ID = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    open = db.Column(db.Numeric(19, 4))
    high = db.Column(db.Numeric(19, 4))
    low = db.Column(db.Numeric(19, 4))
    close = db.Column(db.Numeric(19, 4))
    volume = db.Column(db.Integer)
    stock = db.Column(db.String(30), nullable=False, index=True)
    mentions = db.Column(db.Integer, server_default=db.FetchedValue())


class Predictions(db.Model):
    __tablename__ = 'Predictions'

    stock = db.Column(db.Text(), primary_key=True)
    volume = db.Column(db.BigInteger)
    volume_confidence = db.Column(db.Numeric)
    date = db.Column(db.DateTime, primary_key=True)
