"""
Initializes and returns a Google Generative AI model with specified configurations.

This function configures the Google Generative AI library with an API key and initializes a generative model based on the provided model name and pre-defined generation settings. The generation settings control aspects of the model's output, such as creativity (temperature), token selection strategies (top_p, top_k), and the maximum length of generated content (max_output_tokens). Additionally, safety settings are defined to automatically block content related to harassment, hate speech, sexually explicit material, and dangerous content at medium thresholds and above.

Parameters:
- model_name (str): The name of the generative model to be initialized (e.g., "Gemini Pro").
- api_key (str): The API key required to authenticate and authorize usage of the Google Generative AI services.

Returns:
- genai.GenerativeModel: An instance of the GenerativeModel class, configured and ready for generating content based on the specified settings.

Usage:
- This function is intended to be used for setting up a generative AI model instance with specific output generation and safety configurations. It simplifies the process of model initialization, making it straightforward to integrate generative AI capabilities into applications.
"""


import google.generativeai as genai

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
    
def initialize_model(model_name,api_key):
    # Initialize and return the Gemini Pro model with the provided API key
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name=model_name, generation_config=generation_config)
    return model
