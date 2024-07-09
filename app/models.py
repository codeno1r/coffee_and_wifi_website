from .extensions import db


class Cafe(db.Model):
    __tablename__ = 'cafes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    location = db.Column(db.String, nullable=False)
    opening_time = db.Column(db.String, nullable=False)
    closing_time = db.Column(db.String, nullable=False)
    coffee = db.Column(db.String, nullable=False)
    wifi = db.Column(db.String, nullable=False)
    power = db.Column(db.String, nullable=False)

    def __init__(self, name, location, opening_time, closing_time, coffee, wifi, power):
        self.name = name
        self.location = location
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.coffee = coffee
        self.wifi = wifi
        self.power = power
