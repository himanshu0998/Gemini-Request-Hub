# text_processing.py
import logging
import google.generativeai as genai
import requests

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import mysql
from database import SessionLocal, Base
from datetime import datetime, timezone
from app.models.TextInteractions import UserTextInteractions
from config import Config
from api_client import initialize_model
# from logger_config import setup_logging

bp = Blueprint('text_processing', __name__, url_prefix='/text')

model = initialize_model('gemini-pro',Config.API_KEY)

userHistory = {}


@bp.route('/chat', methods=['POST'])
@jwt_required()
def chat():
    """
    Handle a chat interaction with a user by processing a text prompt and generating a response.

    This endpoint ('/chat') is designed to accept POST requests with a JSON payload containing a 'prompt' key. It requires a valid JWT for user authentication. Upon receiving a valid request, the function retrieves the user's ID from the JWT, checks for the presence of a prompt in the request data, and interacts with a chat model to generate a response based on the prompt and any existing chat history associated with the user.

    If the user does not have an existing chat history, a new history record is initialized. The function logs the request and its outcome, including any errors. It records the interaction details, including the input prompt and the model's response, in the database with timestamps.

    Parameters:
    - None directly; relies on application/json content type for the 'prompt' data.

    Returns:
    - A JSON response containing the chat model's response to the prompt, with a 200 OK status if the process is successful.
    - A JSON response with an error message and a 400 Bad Request status if no prompt is provided in the request.
    - A JSON response with an error message and a 500 Internal Server Error status if an error occurs during the processing or if the model's response format is unexpected.

    Note: This function demonstrates secure handling of user input in a chat context, including authentication, validation of input, interaction with a chat model, and error handling. It ensures that the user's chat history is maintained and utilized for context in generating responses.
    """

    logging.info(f"Request: {str(request)}")
    input_timestamp = datetime.now(timezone.utc)
    user_id = get_jwt_identity()
    if(user_id not in userHistory):
        userHistory[user_id] = []
    data = request.get_json()  # Proper way to get JSON data
    if not data or 'prompt' not in data:
        logging.error("error\": \"No prompt provided, Response Code: 400")
        return jsonify({"error": "No prompt provided"}), 400

    text_data = data['prompt']
    db_session = SessionLocal()
    try:
        # Ensure model and its methods are correctly defined and accessible
        convo = model.start_chat(history=userHistory[user_id])
        response = convo.send_message(text_data)
        output_timestamp = datetime.now(timezone.utc)
        userHistory[user_id] += convo.history
        
        # Ensure that response.text is the correct way to access the desired information
        if response and hasattr(response, 'text'):
            interaction = UserTextInteractions(
                username=user_id,
                input_type='chat',
                input_content=text_data,
                input_timestamp=input_timestamp,
                output_content = response.text,
                output_timestamp=output_timestamp,  # Adjust as necessary
                status='Processed'
            )
            db_session.add(interaction)
            db_session.commit()
            logging.info("Request Processed, Response code: 200")
            return jsonify({"prompt_response": response.text}), 200
        else:
            interaction = UserTextInteractions(
                username=user_id,
                input_type='chat',
                input_content=text_data,
                input_timestamp=input_timestamp,
                output_content = '',
                output_timestamp=None,  # Adjust as necessary
                status='No Response'
            )
            db_session.add(interaction)
            db_session.commit()
            logging.error("error\": \"Unexpected response format from the model, Response code 500")
            return jsonify({"error": "Unexpected response format from the model"}), 500
    except Exception as e:
        # Log the exception or handle it as needed
        # print(f"Error processing text: {e}")
        db_session.rollback()
        logging.error(f"Error processing text: {str(e)}, Response Code: 500")
        return jsonify({"error": "An error occurred while processing your request"}), 500
    finally:
        db_session.close()

@bp.route('/prompt', methods=['POST'])
@jwt_required()
def prompt():
    """
    Processes a text prompt to generate and return content based on the input.

    This endpoint ('/prompt') is secured with JWT authentication and accepts POST requests containing a JSON payload with a 'prompt' key. The function validates the presence of the prompt in the request, generates content based on this prompt using a predefined model, and records the interaction, including timestamps and the generated content, in the database.

    The user's identity is determined via the JWT, and the interaction is logged for maintaining the history. If the model successfully generates content, this content is returned to the user. If no content is generated or if an error occurs during processing, appropriate error messages are returned.

    Parameters:
    - None directly; relies on application/json content type for the 'prompt' data.

    Returns:
    - A JSON response containing the generated content for the prompt, with a 200 OK status, if the process is successful.
    - A JSON response with an error message and a 400 Bad Request status if no prompt is provided.
    - A JSON response with an error message and a 500 Internal Server Error status if an error occurs during processing or if the model's response format is unexpected.

    Note: The function demonstrates handling of dynamic content generation based on user input in a secure and authenticated context. It includes detailed error handling and transaction logging for comprehensive tracking and troubleshooting.
    """

    logging.info(f"Request: {str(request)}")
    input_timestamp = datetime.now(timezone.utc)
    user_id = get_jwt_identity()
    data = request.get_json()  # Proper way to get JSON data
    if not data or 'prompt' not in data:
        logging.error("error\": \"No prompt provided, Response Code: 400")
        return jsonify({"error": "No prompt provided"}), 400

    text_data = data['prompt']
    db_session = SessionLocal()
    try:
        # Ensure model and its methods are correctly defined and accessible
        response = model.generate_content(text_data)
        output_timestamp = datetime.now(timezone.utc)

        # Ensure that response.text is the correct way to access the desired information
        if response and hasattr(response, 'text'):
            interaction = UserTextInteractions(
                username=user_id,
                input_type='prompt',
                input_content=text_data,
                input_timestamp=input_timestamp,
                output_content = response.text,
                output_timestamp=output_timestamp,  # Adjust as necessary
                status='Processed'
            )
            db_session.add(interaction)
            db_session.commit()
            logging.info("Request Processed, Response code: 200")
            return jsonify({"prompt_response": response.text}), 200
        else:
            interaction = UserTextInteractions(
                username=user_id,
                input_type='prompt',
                input_content=text_data,
                input_timestamp=input_timestamp,
                output_content = '',
                output_timestamp=None,  # Adjust as necessary
                status='No Response'
            )
            db_session.add(interaction)
            db_session.commit()
            logging.error("error\": \"Unexpected response format from the model, Response code 500")
            return jsonify({"error": "Unexpected response format from the model"}), 500
    except Exception as e:
        # Log the exception or handle it as needed
        db_session.rollback()
        print(f"Error processing text: {e}")
        return jsonify({"error": "An error occurred while processing your request"}), 500
    finally:
        db_session.close()
