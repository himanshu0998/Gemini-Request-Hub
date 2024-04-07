"""
Initializes and configures the Flask application with MySQL, JWT authentication, and logging.

This module sets up a Flask application integrating several components crucial for a web application: database connection via SQLAlchemy and MySQL, JWT-based authentication for secure endpoints, and a logging system for application-wide logging. It also creates all database tables based on SQLAlchemy models if they don't already exist.

The Flask application is configured with settings from the `Config` class, and the MySQL and JWT extensions are initialized with the Flask app instance. Additionally, the application's routes are imported and registered using Flask Blueprints, organizing the application into distinct authentication, image processing, and text processing components.

Functions:
    create_app(): Configures and returns the Flask application instance.

Usage:
    This function is intended to be called to initialize the Flask application, typically from an entry point in the project. After the application is returned by `create_app()`, it can be run to serve the web application.
"""


from flask import Flask
from config import Config
from database import engine, Base
from flask_mysqldb import MySQL
from flask_jwt_extended import JWTManager
from logger_config import setup_logging
from .models.User import User
from .models.TextInteractions import UserTextInteractions
from .models.ImageInteractions import UserImageInteractions

mysql = MySQL()
jwt = JWTManager()

setup_logging()

Base.metadata.create_all(bind=engine)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mysql.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from .routes import auth, image_processing, text_processing
        app.register_blueprint(auth.bp)
        app.register_blueprint(text_processing.bp)
        app.register_blueprint(image_processing.bp)
        
    return app
