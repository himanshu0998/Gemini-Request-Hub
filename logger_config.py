import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logging():
    if not os.path.exists('logs'):
        os.mkdir('logs')
    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    log_file = 'logs/app.log'

    my_handler = RotatingFileHandler(log_file, mode='a', maxBytes=5*1024*1024, backupCount=2, encoding=None, delay=0)
    my_handler.setFormatter(log_formatter)
    my_handler.setLevel(logging.INFO)

    app_logger = logging.getLogger('root')
    app_logger.setLevel(logging.INFO)
    app_logger.addHandler(my_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    console_handler.setLevel(logging.DEBUG)
    app_logger.addHandler(console_handler)

# setup_logging()