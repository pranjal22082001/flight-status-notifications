from flask_pymongo import PyMongo

mongo = PyMongo()

def init_db(app):
    mongo.init_app(app)

def get_flights():
    flights = mongo.db.flights.find()
    return list(flights)

def add_flight(flight):
    mongo.db.flights.insert_one(flight)