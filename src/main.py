import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add the parent directory to the sys.path
from src.services.sensor_collector import initialize_sensors
from src.utils.logger import setup_logger
from src.utils.file_handler import save_to_csv

def main():
    # Initialize sensors
    sensors = initialize_sensors()

    # Collect data in real-time
    while True:
        for sensor in sensors:
            # Access sensor attributes using dot notation
            sensor_id = sensor.sensor_id
            district = sensor.district

            # Setup logger for each sensor
            logger = setup_logger(sensor_id, district)

            try:
                # Collect sensor data
                data = sensor.get_sensor_data()
                logger.info(f"Data collected: {data}")

                # Save data to CSV
                save_to_csv(data['sensor_id'], data)

                # Log successful data collection
                logger.info(f"Data successfully saved to CSV for sensor {data['sensor_id']}")

            except Exception as e:
                # Log any errors encountered during the process
                logger.error(f"Error collecting or saving data for sensor {sensor_id}: {e}")

        # Sleep to control the collection interval (e.g., every 7 minutes)
        time.sleep(420)

if __name__ == "__main__":
    main()
