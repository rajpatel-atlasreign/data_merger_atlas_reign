import logging


def setup_logger():
    logging.basicConfig(filename='./server_logs/DataMerger.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logging.info("Logger setup complete.")
