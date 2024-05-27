# utils/logging.py
# Define a logging utility to configure and manage application logging.
import logging

def configure_logging():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger
