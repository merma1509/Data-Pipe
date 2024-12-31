import csv
import os
import logging


class RawDataBackup:
    """Class to handle saving sensor data to a CSV file as backup."""

    def __init__(self, backup_dir="Backups/raw_backups"):
        self.backup_dir = backup_dir
        # Create the directory if it doesn't exist
        os.makedirs(self.backup_dir, exist_ok=True)

    def save_raw_data_to_csv(self, data, date_str):
        """Save sensor data to a CSV file as backup.
        Arguments:
            data (list): List of dictionaries containing sensor data.
            date_str (str): Date string in the format 'YYYY-MM-DD'.
        Descriptions:
            - The CSV file name will be in the format 'YYYY-MM-DD_sensor_data.csv'
        """
        file_name = os.path.join(
            self.backup_dir, f"Backup_sensor_raw_data_{date_str}.csv")
        fieldnames = [
            'sensor_id', 'time_and_date', 'location', 'barometric_pressure_hpa',
            'temperature_c', 'wind_direction_deg', 'humidity_percent', 'wind_speed_mps',
            'precipitation_mm', 'soil_moisture_percent', 'evapotranspiration_mm_day',
            'rainfall_mm', 'rainfall_duration_hours', 'water_level_m', 'river_flow_rate_m3s',
            'elevation_m', 'solar_radiation_wm2', 'groundwater_level_m', 'air_quality_index'
        ]

        try:
            # Check if the file already exists
            file_exists = os.path.isfile(file_name)
            with open(file_name, mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                if not file_exists:
                    writer.writeheader()
                writer.writerow(data)
            logging.info(f"Raw data entry backed up to: '{file_name}' ...")
            return "Success"  # Indicate success
        except IOError as e:
            logging.error(f"Error saving to CSV: {e}")
            return None  # Indicate failure
