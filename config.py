"""
A configuration class for centralizing application settings, including database and authentication parameters.

This class stores configuration parameters as class attributes, making them easily accessible throughout the application. It includes settings for connecting to a MySQL database and for security features such as JWT authentication.

Attributes:
- `MYSQL_USER` (str): The username for the MySQL database connection.
- `MYSQL_PASSWORD` (str): The password for the MySQL database connection.
- `MYSQL_DB` (str): The name of the MySQL database to use.
- `MYSQL_HOST` (str): The hostname where the MySQL database server is running, typically 'localhost' for local development environments.
- `JWT_SECRET_KEY` (str): A randomly generated secret key for JWT authentication, ensuring security for token generation and verification.
- `API_KEY` (str): A static API key that could be used for accessing certain APIs or for simple API key-based authentication.

The `secrets` module is used to generate a secure, random `JWT_SECRET_KEY` for each instance of the application, enhancing security by preventing hard-coded or predictable keys.

Usage:
This class is intended to be instantiated or directly accessed to retrieve configuration settings. The attributes can be modified to match the deployment environment's specific configuration needs.
"""


import secrets
class Config:
    MYSQL_USER = '<user_name>'
    MYSQL_PASSWORD = '<password>'
    MYSQL_DB = '<mysql db name>'
    MYSQL_HOST = '<hostname>'
    JWT_SECRET_KEY = secrets.token_hex(24)
    API_KEY = '<Gemini API key>'
