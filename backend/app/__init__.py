from flask import Flask
from flask_cors import CORS
from .models import init_db

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['MONGO_URI'] = 'mongodb://localhost:27017/flightdb'
    init_db(app)

    from .api import api
    app.register_blueprint(api, url_prefix='/api')

    return app
