import google.generativeai as genai
class APIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        # Initialize the Gemini API client or AI model here
        # For example:
        self.model = self.initialize_gemini_model(api_key)
    
    def initialize_gemini_model(self, api_key):
        # Initialize and return the Gemini model with the provided API key
        # safety_settings = [
        #   {
        #     "category": "HARM_CATEGORY_HARASSMENT",
        #     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        #   },
        #   {
        #     "category": "HARM_CATEGORY_HATE_SPEECH",
        #     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        #   },
        #   {
        #     "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        #     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        #   },
        #   {
        #     "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        #     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        #   },
        # ]
        generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
        }
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config)
        return model

# Instantiate the API client with the API key
# Ideally, the API key should be stored in a secure place, like environment variables
api_key = "AIzaSyBUx2njqnTUtvTmW-Uomv71nntTKE1eHDo"
gemini_api_client = APIClient(api_key)
