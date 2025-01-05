import logging
import os
from datetime import datetime

class Logger:
    def __init__(self, district: str, sensor_id: str):
        """
        Initializes the Logger class with district and sensor_id for specific logging.

        Args:
            district (str): Name of the district where the sensor is located.
            sensor_id (str): Unique identifier for the sensor.
        """
        self.district = district
        self.sensor_id = sensor_id
        self.base_log_dir = 'logs'
        
        # Create the district directory if it doesn't exist
        self.district_dir = os.path.join(self.base_log_dir, self.district)
        os.makedirs(self.district_dir, exist_ok=True)

    def setup_logger(self):
        """
        Sets up logging to both console and file for a specific sensor in a district.
        Creates a separate log file for each sensor and a directory for each district.
        """
        # Create a log file name based on the sensor_id and today's date
        log_file = os.path.join(self.district_dir, f'{self.sensor_id}_{datetime.now().strftime("%Y-%m-%d")}.log')

        # Create a logger
        logger = logging.getLogger(self.sensor_id)
        logger.setLevel(logging.INFO)
        
        # Create file and console handlers
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        
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

    def log_api_start(self):
        """
        Logs that the API has started running.
        """
        # Create a log file name for the API start
        log_file = os.path.join(self.district_dir, f'{self.sensor_id}_{datetime.now().strftime("%Y-%m-%d")}_api_start.log')

        # Create a logger for API start
        api_logger = logging.getLogger('API')
        api_logger.setLevel(logging.INFO)
        
        # Create file and console handlers for API start
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Formatter for API start log
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to API logger
        api_logger.addHandler(file_handler)
        api_logger.addHandler(console_handler)

        # Log the API start
        api_logger.info('API has started.')

    def log_api_shutdown(self):
        """
        Logs that the API is shutting down.
        """
        # Create a log file name for the API shutdown
        log_file = os.path.join(self.district_dir, f'{self.sensor_id}_{datetime.now().strftime("%Y-%m-%d")}_api_shutdown.log')

        # Create a logger for API shutdown
        api_logger = logging.getLogger('API')
        api_logger.setLevel(logging.INFO)
        
        # Create file and console handlers for API shutdown
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Formatter for API shutdown log
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to API logger
        api_logger.addHandler(file_handler)
        api_logger.addHandler(console_handler)

        # Log the API shutdown
        api_logger.info('API is shutting down.')

    def log_incoming_request(self, data: dict):
        """
        Logs the incoming data for a specific sensor and district when a request is received.

        Args:
            data (dict): The incoming data sent to the API.
        """
        # Use the sensor-specific logger
        logger = self.setup_logger()
        logger.info(f"Received data: {data}")
