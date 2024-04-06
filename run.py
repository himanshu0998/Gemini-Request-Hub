from app import create_app
# import logging
# from logger_config import setup_logging

# setup_logging()

# # logging.basicConfig(level=logging.INFO)
# logging.info("Starting Flask application...")

app = create_app()

if __name__ == '__main__':
    app.run(debug=False)