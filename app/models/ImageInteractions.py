"""
A SQLAlchemy model for storing interactions involving images between users and the system.

This model represents the 'userimageinteractions' table in the database, designed to log interactions that include image inputs from users. It captures comprehensive details about each interaction, including the user's identity, the type of input (e.g., 'image'), any associated text prompt, the image data itself, timestamps for both the input and the generated output, the content of the system's response, and the interaction's final status.

Attributes:
    __tablename__ (str): Defines the name of the table within the database, set to 'userimageinteractions'.
    username (Column): Stores the username of the user involved in the interaction as a String, part of the primary key, ensuring that interactions are user-specific.
    input_type (Column): A String column indicating the nature of the interaction input (e.g., 'image'), limited to 10 characters.
    input_prompt (Column): A Text column for any text prompt accompanying the image input, nullable to allow interactions without textual prompts.
    input_image (Column): A LargeBinary column that holds the image data, with a maximum length sufficient for storing large images.
    input_timestamp (Column): A DateTime column recording the exact time the input was received, part of the primary key to differentiate interactions.
    output_content (Column): A Text column containing textual response or content generated in response to the user's input.
    output_timestamp (Column): A DateTime column noting the time when the response or output content was generated.
    status (Column): A String column reflecting the status of the interaction (e.g., 'Processed', 'Failed'), limited to 10 characters, to quickly assess the outcome.

Usage:
    The UserImageInteractions class is utilized for logging and analyzing user interactions that include images as input. This detailed tracking supports functionalities like user feedback analysis, system performance evaluation, and the improvement of image processing features by providing insights into the nature and outcomes of user interactions.
"""

from database import Base
from sqlalchemy import Column, String, Text, DateTime, LargeBinary

class UserImageInteractions(Base):
    __tablename__ = 'userimageinteractions'
    username = Column(String(50), primary_key=True, nullable=False)
    input_type = Column(String(10), nullable=False)
    input_prompt = Column(Text, nullable=True)  # Suitable for long text
    input_image = Column(LargeBinary(length=16777215), nullable=False)
    input_timestamp = Column(DateTime, primary_key=True, nullable=False)
    output_content = Column(Text, nullable=False)
    output_timestamp = Column(DateTime, nullable=False)
    status = Column(String(10), nullable=False)