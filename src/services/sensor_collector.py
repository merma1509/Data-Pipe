import random
from datetime import datetime

class SensorDataCollector:
    """A class to simulate sensor data collection from various environmental sensors."""

    def __init__(self, sensor_id, district, location, datetime_format='%Y-%m-%d %H:%M:%S'):
        """
        Initialize the SensorDataCollector.
        Args:
            sensor_id (str): Unique identifier for the sensor.
            district (str): The district where the sensor is deployed.
            location (str): The specific location within the district where the sensor is deployed.
            datetime_format (str, optional): The format in which the date and time should be stored. Defaults to '%Y-%m-%d %H:%M:%S'.
        """
        self.sensor_id = sensor_id
        self.district = district
        self.location = location
        self.datetime_format = datetime_format

    def collect_data(self):
        """
        Simulate the collection of sensor data for various environmental parameters.
        Returns:
            dict: Simulated sensor data with various environmental metrics.
        """
        data = {
            'sensor_id': self.sensor_id,                                       # Sensor Id
            'timestamp': datetime.now().strftime(self.datetime_format),        # Time and Date 
            'district': self.district,                                         # district Where Sensor Deployed
            'location': self.location,                                         # Specific Location in district
            "barometric_pressure": round(random.uniform(680, 1050), 2),        # Air (Barometric) Pressure in hPa
            "temperature": round(random.uniform(-30, 60), 2),                  # Temperature in °C
            'wind_direction': round(random.uniform(0, 360), 2),                # Wind Direction in Degrees
            "humidity": round(random.uniform(0, 100), 2),                      # Humidity in %
            "wind_speed": round(random.uniform(0, 50), 2),                     # Wind Speed in m/s (to be converted in Km/h)
            'precipitation': round(random.uniform(0, 1170), 2),                # Precipitation (Rainfall) in mm
            'soil_moisture': round(random.uniform(10, 70), 2),                 # Soil Moisture in %
            'evapotranspiration': round(random.uniform(0, 10), 2),             # Amount of water (moisture) being transferred from land to atmosphere in mm/day
            "rainfall_duration": round(random.uniform(0, 24), 2),              # How long it was raining in hours
            "water_level": round(random.uniform(0, 10), 2),                    # Water Body level in m
            "river_flow_rate": round(random.uniform(0, 300), 2),               # River Flow Rate in cubic meters per second
            "elevation": round(random.uniform(0, 3000), 2),                    # Elevation in m
            "solar_radiation": round(random.uniform(0, 1500), 2),              # Solar Radiation in power per square meter (W/m²)
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
        return data


def initialize_sensors():
    """
    Initializes sensors for two districts with distinct locations.
    Returns:
        list: List of initialized sensor objects.
    """
    sensors = []
    distr_locs = {
        "District1": [f"Location_{i+1}" for i in range(7)],  # 7 locations in District1
        "District2": [f"Location_{i+1}" for i in range(7)]   # 7 locations in District2
    }

    for district, locations in distr_locs.items():
        for idx, location in enumerate(locations):
            sensor_id = f"{district}_Sensor_{idx+1}"
            sensors.append(SensorDataCollector(sensor_id=sensor_id, district=district, location=location))

    return sensors
