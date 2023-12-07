from sqlalchemy import create_engine
import logging


def establish_database_connection(configuration):
    try:
        db_config = configuration['database_config']
        engine = create_engine(
            f"mysql+pymysql://{db_config['user_name']}:{db_config['user_password']}@{db_config['server_host']}:{db_config['server_port']}/{db_config['database_name']}")
        logging.info("SQLAlchemy engine created successfully.")
        return engine
    except Exception as error:
        logging.error(f"Failed to create SQLAlchemy engine: {error}")
        raise
