__author__ = 'DaisyS'
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clothingHistoryEntry = db.relationship('ClothingHistoryEntry', backref='user', lazy='dynamic')
    autoCompleteGear = db.relationship('UserGear', backref='usergear', lazy='dynamic')


    def __init__(self):
        pass

    def __repr__(self):
        return '<User %d>' % self.id


usergear = db.Table('usergear',
                    db.Column('gear', db.String(100), primary_key=True),
                    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                    db.Column('frequency', db.Integer))


class ClothingHistoryEntry(db.Model):
    location = db.Column(db.String(80), primary_key=True)
    date = db.Column(db.Date, primary_key=True)
    tempHigh = db.Column(db.Integer)
    tempMin = db.Column(db.Integer)
    precipitation = db.Column(db.Integer)
    comfort = db.Column(db.String(80))
    windSpeed = db.Column(db.Integer)
    windGust = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    cloudPrecip = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    gears = db.Column(db.String(100))

    def __init__(self, tempMax, tempMin, precipitation, comfort, windSpeed, windGust, humidity, cloudPrecip,
                 user_id, gears):
        self.tempMax = tempMax
        self.tempMin = tempMin
        self.precipitation = precipitation
        self.comfort = comfort
        self.windSpeed = windSpeed
        self.windGust = windGust
        self.humidity = humidity
        self.cloudPrecip = cloudPrecip
        self.gears = gears
        self.user_id = user_id

    def __repr__(self):
        return '<ClothingHistoryEntry, user=%d, date=%s>' % (self.user_id, str(self.date))


class DefaultGears(db.Model):
    item = db.Column(db.String, primary_key=True)

    def __init(self):
        pass

    def __repr__(self):
        return '<DefaultGears %d>' % self.item

