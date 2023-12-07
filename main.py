import logging

from data_merge_service import load_configuration, establish_database_connection, execute_data_merge_operations
from data_merge_service.logger import setup_logger


def main():
    setup_logger()
    try:
        configuration = load_configuration('config.json')
        database_engine = establish_database_connection(configuration)
        execute_data_merge_operations(database_engine, configuration['data_merge_operations'])
    except Exception as error:
        logging.error(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
