import pytest
from data_merge_service.database_connector import _establish_database_connection


def test_create_engine_from_config():
    # Test with a valid database configuration
    config = {
        "database_config": {
            "server_host": "localhost",
            "server_port": "3306",
            "user_name": "root",
            "user_password": "password",
            "database_name": "valid_db"
        }
    }
    engine = _establish_database_connection(config)
    assert engine is not None

    # Test with an invalid database configuration
    config = {
        "database_config": {
            "server_host": "invalid_host",
            "server_port": "invalid_port",
            "user_name": "invalid_user",
            "user_password": "invalid_password",
            "database_name": "invalid_db"
        }
    }
    with pytest.raises(Exception):
        engine = _establish_database_connection(config)
