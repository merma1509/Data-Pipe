import random
from datetime import datetime
import logging


class SensorDataCollector:
    """A class to simulate sensor data collection from various environmental sensors."""

    def __init__(self, sensor_id='TheOpCli0915', locations=None, datetime_format='%Y-%m-%d %H:%M:%S'):
        """
        Initialize the SensorDataCollector.
        Args:
            sensor_id (str, optional): Unique identifier for the sensor. Defaults to 'TheOpCli0915'.
            locations (list, optional): List of possible locations for data collection. Defaults to None.
            datetime_format (str, optional): The format in which the date and time should be stored. Defaults to '%Y-%m-%d %H:%M:%S'.
        """
        self.sensor_id = sensor_id
        self.datetime_format = datetime_format
        self.locations = locations if locations is not None else [
            'Unknown Location']

    def collect_data(self):
        """
        Simulate the collection of sensor data for various environmental parameters.
        Returns:
            dict: Simulated sensor data with various environmental metrics.
        """
        data = {
            'sensor_id': self.sensor_id,                                       # Sensor Id
            'timestamp': datetime.now().strftime(self.datetime_format),        # Time and Date 
            'location': random.choice(self.locations),                         # Location Where Sensor Deployed
            "barometric_pressure": round(random.uniform(680, 1050), 2),        # Air (Barometric) Pressure in hPa
            "temperature": round(random.uniform(-30, 60), 2),                  # Temperature in C
            'wind_direction': round(random.uniform(0, 360), 2),                # Wind Direction in Degrees
            "humidity": round(random.uniform(0, 100), 2),                      # Humidity in %
            "wind_speed": round(random.uniform(0, 50), 2),                     # Wind Speed in m/s (to be converted in Km/h)
            'precipitation': round(random.uniform(0, 1170), 2),                # Precipitation (Rainfall) in mm
            'soil_moisture': round(random.uniform(10, 70), 2),                 # Soil Moisture in %
            'evapotranspiration': round(random.uniform(0, 10), 2),             # Amount of water (moisture) being transferred from land to atmospher in mm/day
            "rainfall_duration": round(random.uniform(0, 24), 2),              # How long it was raining in hours
            "water_level": round(random.uniform(0, 10), 2),                    # Water Body level in m
            "river_flow_rate": round(random.uniform(0, 300), 2),               # River Flow Rate in cubic meter per second
            "elevation": round(random.uniform(0, 3000), 2),                    # Elevation in m
            "solar_radiation": round(random.uniform(0, 1500), 2),              # Solar Radition in power per sqaure meter (w/m2)
            "groundwater_level": round(random.uniform(0, 20), 2),              # Level of water in ground in m
            "air_quality_index": round(random.uniform(0, 500), 2),             # Air Quality Index
        }
        return data

    def get_sensor_data(self):
        """
        Collect sensor data without performing any risk calculations.
        Returns:
            dict: Collected sensor data.
        """
        data = self.collect_data()
        logging.info(f"Simulated sensor data: `{list(data.keys())}`")
        return data