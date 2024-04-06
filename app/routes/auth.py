import re
import logging

from flask import Blueprint, request, jsonify
from passlib.hash import pbkdf2_sha256 as sha256
from app import mysql
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from database import SessionLocal, Base
from app.models.User import User
# from logger_config import setup_logging

bp = Blueprint('auth', __name__, url_prefix='/auth')

# setup_logging()

@bp.route('/signup', methods=['POST'])
def signup():
    db_session = SessionLocal()
    logging.info(f"Request: {str(request)}")
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    # firstname = data.get('firstname')
    # lastname = data.get('lastname')
    # emailId = data.get('emailId')
    # Check username length
    if not username or len(username) > 50:
        logging.error("error\": \"Username must be 50 characters or less, Response Code: 400")
        return jsonify({"error": "Username must be 50 characters or less"}), 400
    
    # Check password requirements
    if (not password or len(password) < 8 or not re.search("[A-Z]", password) or not re.search("[a-z]", password) or not re.search("[0-9]", password)):
        logging.error("error\": \"Password must be at least 8 characters long, include 1 capital letter, 1 lowercase letter, and 1 number, Response Code: 400")
        return jsonify({"error": "Password must be at least 8 characters long, include 1 capital letter, 1 lowercase letter, and 1 number"}), 400
    

    if not username or not password:
        logging.error("error\": \"Username and password are required, Response Code: 400")
        return jsonify({"error": "Username and password are required"}), 400
    
    # Hash the password
    hashed_password = sha256.hash(password)
    cursor = mysql.connection.cursor()
    try:
        new_user = User(username=username, password=hashed_password)
        db_session.add(new_user)
        db_session.commit()
        logging.info("User Created Successfully!")
        # cursor.execute("INSERT INTO users(username, password) VALUES (%s, %s)", (username, hashed_password))
        # mysql.connection.commit()
    except Exception as e:
        # print(e)
        db_session.rollback()
        logging.error(f"error: {str(e)}, Response Code: 500")
        return jsonify({"error": "Username already exists or database error, Check logs for details"}), 500
    finally:
        db_session.rollback()
        # cursor.close()
    logging.info("Request Processed, Response code: 201")
    return jsonify({"msg": "User created successfully"}), 201

@bp.route('/signin', methods=['POST'])
def signin():
    logging.info(f"Request: {str(request)}")
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # cursor = mysql.connection.cursor()
    # cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    # user = cursor.fetchone()
    # cursor.close()
    
    db_session = SessionLocal()
    try:
        user = db_session.query(User).filter(User.username == username).first()
        if user and sha256.verify(password, user.password): # Assuming the password is the second column
            access_token = create_access_token(identity=username)
            logging.info("Request Processed, Response code: 200")
            return jsonify(access_token=access_token), 200
        else:
            logging.error("error\": \"Invalid username or password, Response code: 401")
            return jsonify({"error": "Invalid username or password"}), 401
    finally:
        db_session.close()

@bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    logging.info(f"Request: {str(request)}")
    current_user = get_jwt_identity()
    logging.info("Request Processed, Response code: 200")
    return jsonify(logged_in_as=current_user), 200
