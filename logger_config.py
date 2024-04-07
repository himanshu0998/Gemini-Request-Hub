"""
Configures logging for the application, including file and console output.

This function sets up a dual logging system for the application: it logs to a file with rotation support and also outputs log messages to the console. The log file 'app.log' is stored in a 'logs' directory. If the 'logs' directory does not exist, it is created. Log rotation is configured to keep the file size under 5 MB with a maximum of two backup files.

Logging to file is set at the INFO level, meaning it captures all messages at the INFO level and above (WARNING, ERROR, CRITICAL). The console logging is set at the DEBUG level, capturing all log messages including DEBUG messages, providing more detailed output when running the application interactively.

The log messages include the timestamp, log level, and the message. This configuration aids in both development, by providing immediate feedback in the console, and in production, by persistently logging important information and errors to files for later analysis.

Usage:
    Call `setup_logging()` at the beginning of the application's entry point to initialize the logging system. This ensures that all subsequent log messages are appropriately routed according to the configured levels and handlers.
"""

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