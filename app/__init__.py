from flask import Flask
from .views import bp_index
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(bp_index)

    return app
