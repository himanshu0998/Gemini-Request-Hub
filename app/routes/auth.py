import re
import logging

from flask import Blueprint, request, jsonify
from passlib.hash import pbkdf2_sha256 as sha256
from app import mysql
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jti, get_jwt
from database import SessionLocal, Base
from app.models.User import User
from app.models.BlockListedToken import BlocklistedToken
from datetime import datetime
# from logger_config import setup_logging

bp = Blueprint('auth', __name__, url_prefix='/auth')

# setup_logging()

@bp.route('/signup', methods=['POST'])
def signup():
    """
    Create a new user account with the provided username and password.

    This endpoint ('/signup') accepts POST requests with JSON content including the username and password for the new account. 
    The function validates the username to ensure it does not exceed 50 characters and validates the password to ensure it meets 
    complexity requirements (at least 8 characters long, includes at least one uppercase letter, one lowercase letter, and one number). 
    If the validations pass, the password is hashed and the new user is saved to the database.

    If any validation fails, an appropriate error message and a 400 Bad Request status are returned. If the user creation process 
    encounters an error, such as a username already existing or a database error, an error message and a 500 Internal Server Error status 
    are returned.

    Parameters:
    - None directly taken; however, the function expects a JSON payload in the request with 'username' and 'password' keys.

    Returns:
    - A JSON response with a success message and a 201 Created status if the user is successfully created.
    - A JSON response with an error message and a 400 Bad Request status if input validation fails.
    - A JSON response with an error message and a 500 Internal Server Error status if there is a problem creating the user in the database.

    Note: The function initializes a database session, logs request and error information, and handles exceptions related to database 
    operations.
    """

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
    """
    Authenticate a user based on username and password.

    This endpoint ('/signin') accepts POST requests with JSON content containing the username and password. It attempts to
    authenticate the user by checking the provided credentials against the stored credentials in the database. If the 
    authentication is successful, the function generates and returns an access token.

    The function logs the request details and the outcome of the authentication attempt. In case of successful authentication,
    an access token is returned with a 200 OK status. If the authentication fails due to invalid credentials, an error message
    and a 401 Unauthorized status are returned.

    Parameters:
    - None directly taken; however, the function expects a JSON payload in the request with 'username' and 'password' keys.

    Returns:
    - A JSON response containing the access token and a 200 OK status if authentication is successful.
    - A JSON response with an error message and a 401 Unauthorized status if the username or password is incorrect.

    Note: The function initializes a database session to query the user details and ensures the session is closed after 
    processing the request. It leverages password hashing and token generation for security.
    """

    logging.info(f"Request: {str(request)}")
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
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
    """
    Retrieve the identity of the current user from a protected endpoint.

    This endpoint ('/protected') requires a valid JWT (JSON Web Token) to access. 
    It is intended to demonstrate a protected route that only authenticated users can access. 
    Upon a successful request, it returns the username of the currently authenticated user, 
    indicating the request was made with a valid token.

    The function logs the details of the incoming request and the identity of the user making the request. 
    It responds with the username of the authenticated user and a 200 OK status to indicate successful access 
    to the protected resource.

    Parameters:
    - None; the function does not take parameters directly but requires a valid JWT in the request's Authorization header.

    Returns:
    - A JSON response containing the username of the authenticated user and a 200 OK status.

    Note: The `jwt_required()` decorator is used to enforce that this endpoint can only be accessed by requests with a valid JWT. 
    The function logs the request and the result of the authorization check.
    """
    
    logging.info(f"Request: {str(request)}")
    current_user = get_jwt_identity()
    logging.info("Request Processed, Response code: 200")
    return jsonify(logged_in_as=current_user), 200

@bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    """
    Logs out a user by blacklisting the current JWT token.

    This endpoint accepts POST requests and requires a valid JWT token in the Authorization header. It extracts the 'jti' (JWT ID) and 'exp' (expiration time) claims from the current token. The token is then added to a blacklist (stored in a database), effectively preventing it from being used for further requests.

    The blacklist mechanism is essential for allowing users to explicitly end their sessions, even though JWT tokens are stateless and cannot be invalidated directly.

    Parameters:
    - None directly taken from the request; however, the JWT token is required in the Authorization header.

    Returns:
    - A JSON response with a message indicating successful logout and a 200 HTTP status code if the token is successfully blacklisted.
    - A JSON response with an error message and a 500 HTTP status code if there is an issue blacklisting the token, such as a database error.

    The function attempts to create a database session, add the token to the blacklist, and commit the transaction. Any exceptions encountered during this process are caught, logged, and reported back to the client.

    The database session is always properly closed, regardless of whether the operation succeeds or fails, to ensure resource cleanup and prevent leaks.

    Note:
    - This endpoint does not actually "log out" the user in the traditional sense, as JWT tokens are stateless and the server does not maintain session states. Instead, it prevents the blacklisted token from being used again, simulating the effect of a logout.
    """

    jwt_claims = get_jwt()
    jti = jwt_claims["jti"]
    expires_at = jwt_claims.get('exp')
    try:
        db_session = SessionLocal()
        blacklisted_token = BlocklistedToken(jti=jti, expires_at=datetime.fromtimestamp(expires_at))
        db_session.add(blacklisted_token)
        db_session.commit()
        logging.info(f"Token {jti} blacklisted. Successfully logged out, Response code: 200")
        return jsonify({"msg": "Successfully logged out"}), 200
    except Exception as e:
        db_session.rollback()
        logging.error(f"Failed to blacklist token {jti}: {str(e)}")
        return jsonify({"error": "Failed to logout, please try again"}), 500
    finally:
        db_session.close()

