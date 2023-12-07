from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
import logging
from typing import Dict, Any
from enum import Enum


class LogMessages(Enum):
    ENGINE_CREATE_SUCCESS = "SQLAlchemy engine created successfully."
    ENGINE_CREATE_FAILURE = "Failed to create SQLAlchemy engine: {}"


class ConfigKeys(Enum):
    DATABASE_CONFIG = 'database_config'
    USER_NAME = 'user_name'
    USER_PASSWORD = 'user_password'
    SERVER_HOST = 'server_host'
    SERVER_PORT = 'server_port'
    DATABASE_NAME = 'database_name'


def _establish_database_connection(configuration: Dict[str, Any]) -> Engine:
    """
    Establishes a database connection using SQLAlchemy.

    This function reads the database configuration from the provided dictionary
    and uses SQLAlchemy to create an engine for connecting to the database.

    Args:
        configuration (Dict[str, Any]): Configuration dictionary containing the database connection details.

    Returns:
        Engine: A SQLAlchemy Engine object that represents the database connection.

    Raises:
        Exception: If the creation of the database engine fails.
    """
    try:
        db_config = configuration[ConfigKeys.DATABASE_CONFIG.value]
        engine = create_engine(
            f"mysql+pymysql://{db_config[ConfigKeys.USER_NAME.value]}:{db_config[ConfigKeys.USER_PASSWORD.value]}@"
            f"{db_config[ConfigKeys.SERVER_HOST.value]}:{db_config[ConfigKeys.SERVER_PORT.value]}/"
            f"{db_config[ConfigKeys.DATABASE_NAME.value]}")
        logging.info(LogMessages.ENGINE_CREATE_SUCCESS.value)
        return engine
    except Exception as error:
        logging.error(LogMessages.ENGINE_CREATE_FAILURE.value.format(error))
        raise
