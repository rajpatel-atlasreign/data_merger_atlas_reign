import pytest
import pandas as pd

from data_merge_service.database_connector import _establish_database_connection
from data_merge_service.data_operations import _execute_data_merge_operations


def test_perform_data_merge_operations():
    # Test with a valid data merge operation
    config = {
        "database_config": {
            "server_host": "localhost",
            "server_port": "3306",
            "user_name": "root",
            "user_password": "password",
            "database_name": "test_database"
        },
        "data_merge_operations": [
            {
                "left_data_table": {
                    "table_name": "table1",
                    "merge_keys": ["id"]
                },
                "right_data_table": {
                    "table_name": "table2",
                    "merge_keys": ["id"]
                },
                "merge_type": "inner",
                "column_suffixes": ["_from_left_table", "_from_right_table"],
                "output_file_name": "test_output.csv"
            }
        ]
    }
    engine = _establish_database_connection(config)
    _execute_data_merge_operations(engine, config['data_merge_operations'])
    result = pd.read_csv('test_output.csv')
    assert not result.empty

    # Test with an invalid data merge operation
    config = {
        "database_config": {
            "server_host": "localhost",
            "server_port": "3306",
            "user_name": "root",
            "user_password": "password",
            "database_name": "test_db"
        },
        "data_merge_operations": [
            {
                "left_data_table": {
                    "table_name": "invalid_table",
                    "merge_keys": ["invalid_key"]
                },
                "right_data_table": {
                    "table_name": "invalid_table",
                    "merge_keys": ["invalid_key"]
                },
                "merge_type": "inner",
                "column_suffixes": ["_from_left_table", "_from_right_table"],
                "output_file_name": "test_output.csv"
            }
        ]
    }
    engine = _establish_database_connection(config)
    with pytest.raises(Exception):
        _execute_data_merge_operations(engine, config['data_merge_operations'])
