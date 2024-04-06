import io
import google.generativeai as genai
import logging
import requests

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import mysql
from PIL import Image
from database import SessionLocal, Base
from datetime import datetime, timezone
from app.models.ImageInteractions import UserImageInteractions
from config import Config
from api_client import initialize_gemini_vision_pro_model
# from logger_config import setup_logging

bp = Blueprint('image_processing', __name__, url_prefix='/image')

model = initialize_gemini_vision_pro_model(Config.API_KEY)

@bp.route('/process', methods=['POST'])
@jwt_required()
def process_image():
    user_id = get_jwt_identity()
    if 'image' not in request.files:
        logging.error("error\": \"No image file provided, Response Code: 400")
        return jsonify({"error": "No image file provided"}), 400
    input_timestamp = datetime.now(timezone.utc)
    
    #Getting the image from request and storing it in an array to further put it in a table as a Medium Blob
    img_byte_arr = io.BytesIO()
    image_file = Image.open(request.files['image'])
    image_file.save(img_byte_arr, format=image_file.format)
    img_byte_data = img_byte_arr.getvalue()
    
    #Getting the prompt from the request - If it does not exist then default prompt is empty
    prompt = request.form.get('prompt','')
    db_session = SessionLocal()
    try:
      response = model.generate_content([prompt, image_file])
      output_timestamp = datetime.now(timezone.utc)

      if response and hasattr(response, 'text'):
        interaction = UserImageInteractions(
                username = user_id,
                input_type = 'image',
                input_prompt = prompt,
                input_image = img_byte_data,
                input_timestamp = input_timestamp,
                output_content =response.text,
                output_timestamp = output_timestamp,
                status = 'Processed'
        )
        db_session.add(interaction)
        db_session.commit()
        logging.info("Request Processed, Response code: 200")
        return jsonify({"prompt_response": response.text}), 200
      else:
        interaction = UserImageInteractions(
                username = user_id,
                input_type = 'image',
                input_prompt = prompt,
                input_image = img_byte_data,
                input_timestamp = input_timestamp,
                output_content = '',
                output_timestamp = None,
                status = 'No Response'
        )
        db_session.add(interaction)
        db_session.commit()
        logging.error("error\": \"Unexpected response format from the model, Response code 500")
        return jsonify({"error": "Unexpected response format from the model"}), 500 
    except Exception as e:
      # print(f"Error processing text: {e}")
      logging.error(f"Error processing text: {str(e)}, Response Code: 500")
      return jsonify({"error": "An error occurred while processing your request"}), 500
    finally:
       db_session.close()