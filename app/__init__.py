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
