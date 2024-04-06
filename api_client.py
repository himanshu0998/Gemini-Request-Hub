import google.generativeai as genai
# from config import Config

safety_settings = [
          {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
        ]
    
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }
    
def initialize_gemini_pro_model(api_key):
    # Initialize and return the Gemini Pro model with the provided API key
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config)
    return model

def initialize_gemini_vision_pro_model(api_key):
    # Initialize and return the Gemini Vision Pro model with the provided API key
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-pro-vision", generation_config=generation_config)
    return model
