import logging

from sqlalchemy.engine.base import Engine
from typing import Any, Dict
from enum import Enum

from .config_loader import _load_configuration
from .database_connector import _establish_database_connection
from .data_operations import _execute_data_merge_operations
from .logger import _setup_logger


class LogMessages(Enum):
    ERROR_OCCURRED = "An error occurred during the execution of the data merge service: {}"


class ConfigKeys(Enum):
    DATA_MERGE_OPERATIONS = 'data_merge_operations'


def perform_merge_from_config(config_path: str) -> None:
    """
    Performs data merging operations as defined in a configuration file.

    This function serves as an orchestrator for the data merging process. It loads the
    configuration from a specified path, establishes a database connection based on this
    configuration, and then executes a series of data merge operations also defined in
    the configuration.

    Args:
        config_path (str): The file path to the configuration file that contains all necessary
                           settings and parameters for the data merging operations.

    The configuration file is expected to contain database connection settings and a list
    of data merge operations to be performed. This function leverages other modules for
    specific tasks like configuration loading, database connection, and executing merge operations.
    """
    _setup_logger()
    try:
        configuration: Dict[str, Any] = _load_configuration(config_path)
        database_engine: Engine = _establish_database_connection(configuration)
        _execute_data_merge_operations(database_engine, configuration[ConfigKeys.DATA_MERGE_OPERATIONS.value])
    except Exception as error:
        logging.error(LogMessages.ERROR_OCCURRED.value.format(error))
