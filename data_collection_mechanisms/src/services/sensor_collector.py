from src.models import SensorDataCollector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def initialize_sensors():
    """
    Initializes sensors for districts and locations specified in the .env file.

    Returns:
        list: List of initialized sensor objects.
    """
    sensors = []

    # Load districts and number of locations per district from environment variables
    districts = os.getenv("DISTRICTS", "District_1,District_2").split(",")
    locations_per_district = int(os.getenv("LOCATIONS_PER_DISTRICT", 7))

    for district in districts:
        for idx in range(locations_per_district):
            location = f"Location_{idx+1}"
            sensor_id = f"{district}_Sensor_{idx+1}"
            sensors.append(SensorDataCollector(sensor_id=sensor_id, district=district, location=location))

    return sensors

