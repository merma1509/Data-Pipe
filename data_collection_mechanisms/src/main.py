import time
import sys
import os
from dotenv import load_dotenv
import requests

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import custom modules
from src.config import DATA_COLLECTION_INTERVAL
from src.services.sensor_collector import initialize_sensors
from src.utils.logger import Logger
from src.utils.file_handler import save_to_csv

# Load environment variables
load_dotenv()

# API URL for data submission
API_URL = "http://localhost:8000/collect_sensor_data"

def send_data_to_api(sensor_data):
    """
    Send collected sensor data to the FastAPI server.
    
    Args:
        sensor_data (dict): The sensor data to be sent.
    """
    try:
        response = requests.post(API_URL, json=sensor_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to API: {e}")
        return None

def main():
    try:
        # Initialize sensors
        sensors = initialize_sensors()

        # Collect data in real-time
        while True:
            for sensor in sensors:
                # Access sensor attributes using dot notation
                sensor_id = sensor.sensor_id
                district = sensor.district

                # Setup logger for each sensor using the Logger class
                logger = Logger(district, sensor_id).setup_logger()

                try:
                    # Collect sensor data
                    data = sensor.get_sensor_data()
                    logger.info(f"Data collected: {data}")

                    # Save data to CSV
                    save_to_csv(sensor_id, data)
                    logger.info(f"Data successfully saved to CSV for sensor {sensor_id}")

                    # Send data to the FastAPI server
                    api_response = send_data_to_api(data)
                    if api_response:
                        logger.info(f"Data successfully sent to API: {api_response}")
                    else:
                        logger.error(f"Failed to send data to API for sensor {sensor_id}")

                except Exception as e:
                    # Log any errors encountered during the process
                    logger.error(f"Error collecting or saving data for sensor {sensor_id}: {e}")

            # Sleep to control the collection interval
            time.sleep(DATA_COLLECTION_INTERVAL * 60)  # Convert minutes to seconds
    finally:
        print("Data collection completed.")

if __name__ == "__main__":
    main()
