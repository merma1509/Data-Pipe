from datetime import datetime
from random import sample
import asyncio
import logging
import csv
import os
from collect_sensor_raw_data import SensorDataCollector

# Configure and set up logging
'''LOG_FILE = "sensor_raw_data.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

'''
# RawDataCollector class
class RawDataCollector:
    """Main Class that will run the data collection layer"""

    def __init__(self, locations, data_collection_interval=420, csv_file="collected_sensor_data.csv"):
        self.data_collection_interval = data_collection_interval
        self.sensor_collector = SensorDataCollector(locations=locations)
        self.csv_file = csv_file

        # Ensure the CSV file has headers if it doesn't exist
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    "sensor_id", "timestamp", "location", "barometric_pressure", "temperature", 
                    "wind_direction", "humidity", "wind_speed", "precipitation", "soil_moisture", 
                    "evapotranspiration", "rainfall_duration", "water_level", "river_flow_rate", 
                    "elevation", "solar_radiation", "groundwater_level", "air_quality_index"
                ])

    async def save_sensor_data_to_csv(self, sensor_data):
        """Save sensor data to a CSV file."""
        try:
            with open(self.csv_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    sensor_data["sensor_id"], sensor_data["timestamp"], sensor_data["location"],
                    sensor_data["barometric_pressure"], sensor_data["temperature"],
                    sensor_data["wind_direction"], sensor_data["humidity"], sensor_data["wind_speed"],
                    sensor_data["precipitation"], sensor_data["soil_moisture"],
                    sensor_data["evapotranspiration"], sensor_data["rainfall_duration"],
                    sensor_data["water_level"], sensor_data["river_flow_rate"],
                    sensor_data["elevation"], sensor_data["solar_radiation"],
                    sensor_data["groundwater_level"], sensor_data["air_quality_index"]
                ])
            logging.info(f"Sensor data saved to `{self.csv_file}`")
        except Exception as e:
            logging.error(f"Error saving data to CSV: {e}")

    async def collect_and_save_data(self):
        """Main method for collecting sensor data and logging it."""
        try:
            while True:
                # Collect sensor data
                sensor_data = self.sensor_collector.get_sensor_data()

                # Save the collected data to CSV
                await self.save_sensor_data_to_csv(sensor_data)

                # Wait for the specified interval before the next collection
                await asyncio.sleep(self.data_collection_interval)

        except asyncio.CancelledError:
            logging.info("Data collection stopped by user.")
        except Exception as e:
            logging.error(f"An error occurred during data collection: {e}")

    def run(self):
        """Run the data collection asynchronously."""
        try:
            asyncio.run(self.collect_and_save_data())
        except KeyboardInterrupt:
            logging.info("Data collection stopped by user.")


if __name__ == "__main__":
    locations = [
        'Kigali City', 'Nyamirambo', 'Muhima', 'Biryogo', 'Rwezamenyo', 'Gitega',
        'Kiyovu', 'Kimisagara', 'Nyabugogo', 'Kabeza', 'Gisozi', 'Kacyiru', 'Cyahafi',
        'Kiyovu (upper)', 'Rugenge', 'Nyakabanda', 'Agatare', 'Gatenga', 'Rugarama',
        'Kiyovu (lower)', 'Karuruma', 'Gikondo', 'Kabusunzu', 'Kimicanga', 'Nyarugenge Market',
        'Nyabugogo Taxi Park', 'Kanyinya', 'Rebero', 'Nyabugogo (bridge area)', 'Nyarugenge Prison',
        'Kigali Genocide Memorial', 'Kicukiro Bus Park', 'Camp Kigali', 'Gatsata', 'Muhima Hospital',
        'Nyamirambo Stadium', 'Kimironko Road', 'Biryogo Market', 'Cyaruzinge', 'Biryogo Health Center',
        'Rugunga', 'Shyorongi', 'Kamenge', 'Mageragere', 'Kigali Convention Center (border)',
        'Kigali Public Library (border)', 'Nyarugenge District Office', 'Gasabo Border Area',
        'City Plaza Building', 'Kigali Business Center'
    ]

    # Randomly sample 7 locations for testing
    sampled_locations = sample(locations, 7)

    # Interval set to 180 seconds (7 minutes)
    data_collector = RawDataCollector(sampled_locations, data_collection_interval=420)
    data_collector.run()
