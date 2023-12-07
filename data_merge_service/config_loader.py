import json
import logging


def load_configuration(configuration_file_path):
    try:
        with open(configuration_file_path, 'r') as file:
            configuration = json.load(file)
        logging.info("Configuration file loaded successfully.")
        return configuration
    except Exception as error:
        logging.error(f"Failed to load configuration file: {error}")
        raise
