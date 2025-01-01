import logging
import os
from datetime import datetime

# Base directory to store log files
BASE_LOG_DIR = 'logs'

# Ensure the base log directory exists
os.makedirs(BASE_LOG_DIR, exist_ok=True)

def setup_logger(sensor_id, district):
    """
    Sets up logging to both console and file for a specific sensor in a district.
    Creates a directory for each district and a separate log file for each sensor.
    
    Args:
        sensor_id (str): Unique sensor identifier.
        district (str): Name of the district where the sensor is located.
    """
    # Create the district directory if it doesn't exist
    district_dir = os.path.join(BASE_LOG_DIR, district)
    os.makedirs(district_dir, exist_ok=True)
    
    # Create a log file name based on the sensor_id and today's date
    log_file = os.path.join(district_dir, f'{sensor_id}_{datetime.now().strftime("%Y-%m-%d")}.log')

    # Create a logger
    logger = logging.getLogger(sensor_id)
    logger.setLevel(logging.INFO)
    
    # Create a file handler that logs to the sensor's log file
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    
    # Create a console handler that logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Create a formatter and set it for both handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
