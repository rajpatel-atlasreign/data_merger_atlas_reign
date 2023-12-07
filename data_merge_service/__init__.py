from .config_loader import load_configuration
from .database_connector import establish_database_connection
from .data_operations import execute_data_merge_operations


def perform_merge_from_config(config_path):
    config = load_configuration(config_path)
    engine = establish_database_connection(config)
    execute_data_merge_operations(engine, config['data_merge_operations'])
