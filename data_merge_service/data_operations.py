import pandas as pd
import logging


def execute_data_merge_operations(database_engine, data_merge_operations):
    for operation in data_merge_operations:
        try:
            left_table = pd.read_sql_table(operation['left_data_table']['table_name'], database_engine)
            right_table = pd.read_sql_table(operation['right_data_table']['table_name'], database_engine)
            result = pd.merge(left_table, right_table, how=operation['merge_type'],
                              left_on=operation['left_data_table']['merge_keys'],
                              right_on=operation['right_data_table']['merge_keys'], suffixes=operation['column_suffixes'])
            result.to_csv(operation['output_file_name'], index=False)
            logging.info(
                f"Data merge operation completed successfully. Output written to {operation['output_file_name']}.")
        except Exception as error:
            logging.error(f"Failed to perform data merge operation: {error}")
            raise
