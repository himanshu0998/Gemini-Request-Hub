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
