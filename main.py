import logging
from typing import Any, Dict
from enum import Enum
from sqlalchemy.engine.base import Engine
from data_merge_service import _load_configuration, _establish_database_connection, _execute_data_merge_operations
from data_merge_service.logger import _setup_logger


class ConfigKeys(Enum):
    DATA_MERGE_OPERATIONS = 'data_merge_operations'


class LogMessages(Enum):
    ERROR_OCCURRED = "An error occurred during the execution of the data merge service: {}"


def main() -> None:
    """
    Main function to set up logger, load configuration, establish database connection,
    and execute data merge operations.
    """
    _setup_logger()
    try:
        configuration: Dict[str, Any] = _load_configuration('config.json')
        database_engine: Engine = _establish_database_connection(configuration)
        _execute_data_merge_operations(database_engine, configuration[ConfigKeys.DATA_MERGE_OPERATIONS.value])
    except Exception as error:
        logging.error(LogMessages.ERROR_OCCURRED.value.format(error))


if __name__ == "__main__":
    main()
