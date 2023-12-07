
# Data Merger Service

Data Merger Service is a Python package that provides a simple and flexible way to merge data from two tables in a MySQL database. The service reads a configuration file that specifies the details of the merge operation, such as the names of the tables, the keys to join on, the type of join, and the output file name.

## Installation

You can install DataMerger from PyPI:

```bash
pip install atreign-datamanager
```

## Usage

To use Data Merger Service, you need to create a configuration file in JSON format. Here’s an example:

```json
{
    "database_config": {
        "server_host": "localhost",
        "server_port": "3306",
        "user_name": "root",
        "user_password": "password",
        "database_name": "database_name"
    },
    "data_merge_operations": [
        {
            "left_data_table": {
                "table_name": "table1",
                "merge_keys": ["key1", "key3"]
            },
            "right_data_table": {
                "table_name": "table2",
                "merge_keys": ["key2", "key4"]
            },
            "merge_type": "inner",
            "column_suffixes": ["_from_left_table", "_from_right_table"],
            "output_file_name": "merged_data_output.csv"
        }
    ]
}
```

Once you have your configuration file, you can perform the merge operation with a single function call:

```python
from data_merger import perform_merge_from_config

perform_merge_from_config('config.json')
```

Replace 'config.json' with the path to your actual configuration file.

## Root Directory Structure
```
data_merger_atlas_reign/
│
├── data_merger/
│   ├── __init__.py
│   ├── config_loader.py
│   ├── database_connector.py
│   ├── data_operations.py
│   └── logger.py
│
├── tests/
│   ├── __init__.py
│   ├── test_config_loader.py
│   ├── test_database_connector.py
│   └── test_data_operations.py
│
├── server_logs/
│   └── DataMerger.log
│
├── config.json
├── test_config.json
├── requirements.txt
├── setup.py
└── main.py

```
## Contributing

If you want to contribute to this project, please submit a pull request.

## License

This project is licensed under the MIT License.
