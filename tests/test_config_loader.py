import pytest
from data_merge_service.config_loader import _load_configuration


def test_load_config():
    # Test with a valid configuration file
    config = _load_configuration('test_config.json')
    assert 'database_config' in config
    assert 'data_merge_operations' in config

    # Test with an invalid configuration file
    with pytest.raises(Exception):
        config = _load_configuration('invalid_config.json')
