"""
Entry point for the Flask web application.

This script initializes the Flask application by calling the `create_app` function, which is expected to configure and return a Flask app instance. The application is then run with debug mode disabled, indicating it is ready for production use.

To start the application, execute this script directly. It will host the Flask application on the default port (5000) accessible via the local machine.

Usage:
    Run this script directly from the command line to start the Flask application:
    $ python run.py
    OR
    $ flask run.py
    OR
    $ python -m flask run
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=False)