from flask import Blueprint, request, jsonify
import pika
import json

api = Blueprint('api', __name__)

@api.route('/flights', methods=['GET'])
def get_flights():
    flights = [
        {"id": 1, "status": "On Time", "gate": "A1"},
        {"id": 2, "status": "Delayed", "gate": "B2"},
        {"id": 3, "status": "Cancelled", "gate": "C3"},
    ]
    return jsonify(flights)

@api.route('/notify', modify=['Post'])
def send_notification():
    data = request.json
    message = json.dumps(data)
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='notifications')
    channel.basic_publish(exchange='', routing_key='notifications', body=message)
    connection.close()
    return jsonify({"message" : "Notification sent"}), 200