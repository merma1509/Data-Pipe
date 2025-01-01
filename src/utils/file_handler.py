import csv
from datetime import datetime
import logging
import os

# Directory to store data files (this is the root directory for all districts)
DATA_DIR = 'data_files'

# Ensure the base directory exists
os.makedirs(DATA_DIR, exist_ok=True)

def save_to_csv(sensor_id, data):
    """
    Save the collected sensor data to a CSV file for the specific sensor.
    Creates a new folder for each district, and inside each district,
    a folder for each sensor, where daily data will be saved.
    
    Args:
        sensor_id (str): Unique sensor identifier.
        data (dict): Sensor data to save.
    """
    # Create the district directory (assuming the 'district' key exists in the data)
    district = data.get('district', 'Unknown_District')
    district_dir = os.path.join(DATA_DIR, district)
    os.makedirs(district_dir, exist_ok=True)
    
    # Create the sensor directory inside the district folder
    sensor_dir = os.path.join(district_dir, sensor_id)
    os.makedirs(sensor_dir, exist_ok=True)
    
    # Create the filename based on today's date
    today = datetime.now().strftime('%Y-%m-%d')
    filename = os.path.join(sensor_dir, f'sensor_data_{sensor_id}_{today}.csv')
    
    # Prepare header from data keys
    header = data.keys()

    try:
        # Open the CSV file in append mode
        with open(filename, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            
            # Write header only if the file is empty (i.e., first time on this day)
            if file.tell() == 0:
                writer.writeheader()
                
            writer.writerow(data)
    except Exception as e:
        logging.error(f"Error saving data to CSV for {sensor_id} in {district}: {e}")
