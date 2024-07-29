from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
import pika
import json

# Initialize MongoDB or SQLAlchemy
mongo = PyMongo()
db = SQLAlchemy()

# Define a function to fetch flights from MongoDB
def get_flights_mongo():
    flights = mongo.db.flights.find()
    return list(flights)

# Define a function to add a flight to MongoDB
def add_flight_mongo(flight):
    mongo.db.flights.insert_one(flight)

# Define a function to fetch flights from PostgreSQL
def get_flights_postgres():
    return db.session.query(Flight).all()

# Define a function to add a flight to PostgreSQL
def add_flight_postgres(status, gate):
    flight = Flight(status=status, gate=gate)
    db.session.add(flight)
    db.session.commit()

# Define a function to send notifications via RabbitMQ
def send_notification(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='notifications')
    channel.basic_publish(exchange='', routing_key='notifications', body=json.dumps(message))
    connection.close()
