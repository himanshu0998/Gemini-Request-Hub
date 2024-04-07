"""
    Initializes and returns a Flask application instance configured with necessary extensions, blueprints, and database models.

    This function performs the following key tasks to set up the Flask application:

    1. Creates a Flask application instance.
    2. Configures the application using settings from the 'Config' class.
    3. Initializes the MySQL extension with the application for database operations.
    4. Initializes the JWTManager extension with the application to handle JWT operations, including setting up a callback 
       for checking if a token is in the blocklist.
    5. Registers various application blueprints for handling authentication, text processing, and image processing routes.
    6. Creates all database tables defined in SQLAlchemy models, if they do not already exist, by binding the models to the 
       specified database engine.

    Additionally, it configures logging for the application based on a predefined logging configuration.

    Returns:
        Flask: The configured Flask application instance ready for use.

    Note:
        - The JWTManager configuration includes a 'token_in_blocklist_loader' callback that defines how to check if a JWT token is 
          in the blocklist, effectively enabling token revocation.
        - Database models must be imported before calling 'Base.metadata.create_all' to ensure SQLAlchemy is aware of them and can 
          create the necessary tables.
    """


from flask import Flask
from config import Config
from database import engine, Base, SessionLocal
from flask_mysqldb import MySQL
from flask_jwt_extended import JWTManager
from logger_config import setup_logging
from .models.User import User
from .models.TextInteractions import UserTextInteractions
from .models.ImageInteractions import UserImageInteractions
from .models.BlockListedToken import BlocklistedToken

mysql = MySQL()
jwt = JWTManager()

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    db_session = SessionLocal()
    token = db_session.query(BlocklistedToken).filter_by(jti=jti).first()
    db_session.close()
    return token is not None

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
