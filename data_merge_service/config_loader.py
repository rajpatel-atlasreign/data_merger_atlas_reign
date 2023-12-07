import json
import logging
from typing import Any, Dict
from enum import Enum


class LogMessages(Enum):
    CONFIG_LOAD_SUCCESS = "Configuration file loaded successfully."
    CONFIG_LOAD_FAILURE = "Failed to load configuration file: {}"
    FILE_READ_FAILURE = "Failed to read file: {}"
    JSON_PARSE_FAILURE = "Failed to parse JSON: {}"


def _log_info(message: str) -> None:
    """
    Logs an informational message to the logging system.

    Args:
    - message (str): The message to be logged.
    """
    logging.info(message)


def _log_error(message: str) -> None:
    """
    Logs an error message to the logging system.

    Args:
    - message (str): The message to be logged.
    """
    logging.error(message)


def _read_file(file_path: str) -> str:
    """
    Reads the content of a file and returns it as a string.

    Args:
    - file_path (str): The path to the file to be read.

    Returns:
    - str: The content of the file.

    Raises:
    - IOError: If the file cannot be read.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except IOError as error:
        _log_error(LogMessages.FILE_READ_FAILURE.value.format(error))
        raise


def _parse_json(json_string: str) -> Dict[str, Any]:
    """
    Parses a JSON string and returns a dictionary.

    Args:
    - json_string (str): The JSON string to be parsed.

    Returns:
    - Dict[str, Any]: The parsed JSON data.

    Raises:
    - json.JSONDecodeError: If the string cannot be parsed as JSON.
    """
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as error:
        _log_error(LogMessages.JSON_PARSE_FAILURE.value.format(error))
        raise


def _load_configuration(configuration_file_path: str) -> Dict[str, Any]:
    """
    Loads a configuration from a JSON file.

    Args:
    - configuration_file_path (str): The path to the configuration file.

    Returns:
    - Dict[str, Any]: The loaded configuration.

    Raises:
    - Exception: If the configuration file cannot be loaded.
    """
    try:
        file_content = _read_file(configuration_file_path)
        configuration = _parse_json(file_content)
        _log_info(LogMessages.CONFIG_LOAD_SUCCESS.value)
        return configuration
    except Exception as error:
        _log_error(LogMessages.CONFIG_LOAD_FAILURE.value.format(error))
        raise
