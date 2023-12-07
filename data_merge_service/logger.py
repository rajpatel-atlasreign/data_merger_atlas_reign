import logging
from enum import Enum


class LogMessages(Enum):
    LOGGER_SETUP_SUCCESS = "Logger setup complete."


class LoggerConfig(Enum):
    FILENAME = './server_logs/DataMerger.log'
    FILEMODE = 'w'
    FORMAT = '%(name)s - %(levelname)s - %(message)s'
    LEVEL = logging.INFO


def _setup_logger() -> None:
    """
    Sets up the logger configuration for the application.

    This function configures the logging module with specified settings such as filename,
    filemode, format, and logging level. It is used to establish how logs are recorded
    and formatted, facilitating easier debugging and monitoring of the application's operation.

    The configuration settings are retrieved from the LoggerConfig enum, ensuring consistency
    and ease of configuration management across the application.
    """
    logging.basicConfig(
        filename=LoggerConfig.FILENAME.value,
        filemode=LoggerConfig.FILEMODE.value,
        format=LoggerConfig.FORMAT.value,
        level=LoggerConfig.LEVEL.value
    )
    logging.info(LogMessages.LOGGER_SETUP_SUCCESS.value)
