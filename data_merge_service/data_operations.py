from enum import Enum
import pandas as pd
import logging
from sqlalchemy.engine.base import Engine
from typing import List, Dict, Any


class LogMessages(Enum):
    READ_TABLE_SUCCESS = "Table '{table_name}' read successfully."
    READ_TABLE_FAILURE = "Failed to read table '{table_name}': {error}"
    MERGE_OPERATION_FAILURE = "Failed to perform merge operation: {error}"
    WRITE_CSV_SUCCESS = "Output written to {file_name}."
    WRITE_CSV_FAILURE = "Failed to write DataFrame to CSV: {error}"
    EXECUTE_OPERATION_FAILURE = "Failed to execute data merge operation: {error}"


class MergeKeys(Enum):
    LEFT_DATA_TABLE = 'left_data_table'
    RIGHT_DATA_TABLE = 'right_data_table'
    TABLE_NAME = 'table_name'
    MERGE_KEYS = 'merge_keys'
    MERGE_TYPE = 'merge_type'
    COLUMN_SUFFIXES = 'column_suffixes'
    OUTPUT_FILE_NAME = 'output_file_name'


def _read_sql_table(table_name: str, database_engine: Engine) -> pd.DataFrame:
    """
    Reads a table from a SQL database into a Pandas DataFrame.

    Args:
    - table_name (str): The name of the SQL table to be read.
    - database_engine (Engine): The SQLAlchemy engine to connect to the database.

    Returns:
    - DataFrame: The read SQL table as a Pandas DataFrame.

    Raises:
    - Exception: If the SQL table cannot be read.
    """
    try:
        table = pd.read_sql_table(table_name, database_engine)
        logging.info(LogMessages.READ_TABLE_SUCCESS.value.format(table_name=table_name))
        return table
    except Exception as error:
        logging.error(LogMessages.READ_TABLE_FAILURE.value.format(table_name=table_name, error=error))
        raise


def _perform_merge(left_table: pd.DataFrame, right_table: pd.DataFrame, operation: Dict[str, Any]) -> pd.DataFrame:
    """
    Performs a merge operation on two Pandas DataFrames based on the provided operation parameters.

    Args:
    - left_table (DataFrame): The left DataFrame for the merge.
    - right_table (DataFrame): The right DataFrame for the merge.
    - operation (Dict[str, Any]): A dictionary containing merge parameters.

    Returns:
    - DataFrame: The resulting DataFrame after the merge operation.

    Raises:
    - Exception: If the merge operation fails.
    """
    try:
        return pd.merge(
            left_table,
            right_table,
            how=operation[MergeKeys.MERGE_TYPE.value],
            left_on=operation[MergeKeys.LEFT_DATA_TABLE.value][MergeKeys.MERGE_KEYS.value],
            right_on=operation[MergeKeys.RIGHT_DATA_TABLE.value][MergeKeys.MERGE_KEYS.value],
            suffixes=operation[MergeKeys.COLUMN_SUFFIXES.value]
        )
    except Exception as error:
        logging.error(LogMessages.MERGE_OPERATION_FAILURE.value.format(error=error))
        raise


def _write_to_csv(data_frame: pd.DataFrame, file_name: str):
    """
    Writes a Pandas DataFrame to a CSV file.

    Args:
    - data_frame (DataFrame): The DataFrame to be written to CSV.
    - file_name (str): The name of the output CSV file.

    Raises:
    - Exception: If there is an error in writing to CSV.
    """
    try:
        data_frame.to_csv(file_name, index=False)
        logging.info(LogMessages.WRITE_CSV_SUCCESS.value.format(file_name=file_name))
    except Exception as error:
        logging.error(LogMessages.WRITE_CSV_FAILURE.value.format(file_name=file_name, error=error))
        raise


def _execute_data_merge_operations(database_engine: Engine, data_merge_operations: List[Dict[str, Any]]):
    """
    Executes a series of data merge operations as defined in the 'data_merge_operations' list.

    Args:
    - database_engine (Engine): The SQLAlchemy engine to connect to the database.
    - data_merge_operations (List[Dict[str, Any]]): A list of dictionaries defining merge operations.

    Raises:
    - Exception: If any part of the data merge operations fails.
    """
    for operation in data_merge_operations:
        try:
            left_table_name = operation[MergeKeys.LEFT_DATA_TABLE.value][MergeKeys.TABLE_NAME.value]
            right_table_name = operation[MergeKeys.RIGHT_DATA_TABLE.value][MergeKeys.TABLE_NAME.value]

            left_table = _read_sql_table(left_table_name, database_engine)
            right_table = _read_sql_table(right_table_name, database_engine)

            result = _perform_merge(left_table, right_table, operation)
            _write_to_csv(result, operation[MergeKeys.OUTPUT_FILE_NAME.value])

        except Exception as error:
            logging.error(LogMessages.EXECUTE_OPERATION_FAILURE.value.format(error=error))
            raise
