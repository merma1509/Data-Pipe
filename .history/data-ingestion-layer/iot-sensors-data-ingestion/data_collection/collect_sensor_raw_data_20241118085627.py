import random
from datetime import datetime
import logging


class SensorDataCollector:
    """A class to simulate sensor data collection from various environmental sensors."""

    def __init__(self, sensor_id='TheOpCli0915', locations=None, datetime_format='%Y-%m-%d %H:%M:%S'):
        """
        Initialize the SensorDataCollector.
        Args:
            sensor_id (str): Unique identifier for the sensor. Defaults to 'TheOpCli0915'.
            locations (list): List of possible locations for data collection. Defaults to None.
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
            'sensor_id': self.sensor_id,
            'time_and_date': datetime.now().strftime(self.datetime_format),
            'location': random.choice(self.locations),
            "barometric_pressure_hpa": round(random.uniform(680, 1050), 2),
            "temperature_c": round(random.uniform(-30, 60), 2),
            'wind_direction_deg': round(random.uniform(0, 360), 2),
            "humidity_percent": round(random.uniform(0, 100), 2),
            "wind_speed_mps": round(random.uniform(0, 50), 2),
            'precipitation_mm': round(random.uniform(0, 1170), 2),
            'soil_moisture_percent': round(random.uniform(10, 70), 2),
            'evapotranspiration_mm_day': round(random.uniform(0, 10), 2),
            "rainfall_mm": round(random.uniform(0, 500), 2),
            "rainfall_duration_hours": round(random.uniform(0, 24), 2),
            "water_level_m": round(random.uniform(0, 10), 2),
            "river_flow_rate_m3s": round(random.uniform(0, 300), 2),
            "elevation_m": round(random.uniform(0, 3000), 2),
            "solar_radiation_wm2": round(random.uniform(0, 1500), 2),
            "groundwater_level_m": round(random.uniform(0, 20), 2),
            "air_quality_index": round(random.uniform(0, 500), 2),
        }
        return data

    def get_sensor_data(self):
        """
        Collect sensor data without performing any risk calculations.
        Returns:
            dict: Collected sensor data.
        """
        data = self.collect_data()
        logging.info(f"Simulated sensor data: {data}")
        return data
