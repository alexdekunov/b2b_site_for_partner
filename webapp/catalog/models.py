from webapp.model import db

class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)