from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from api import api_bp


def create_app():
    app = Flask(__name__)
    CORS(app)
    # Setup the Flask-JWT-Extended extension
    app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this "super secret" to something else!
    jwt = JWTManager(app)
    app.register_blueprint(api_bp, url_prefix='')
    return app