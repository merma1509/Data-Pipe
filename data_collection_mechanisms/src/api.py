from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import os
import sys

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.logger import Logger

app = FastAPI()

# Log API start (this doesn't require district or sensor_id)
logger = Logger(district='default_district', sensor_id='default_sensor')
logger.log_api_start()

# Define a Pydantic model for the sensor data
class SensorData(BaseModel):
    sensor_id: str
    timestamp: str
    district: str
    location: str
    barometric_pressure: float
    temperature: float
    wind_direction: float
    humidity: float
    wind_speed: float
    precipitation: float
    soil_moisture: float
    evapotranspiration: float
    rainfall_duration: float
    water_level: float
    river_flow_rate: float
    elevation: float
    solar_radiation: float
    groundwater_level: float
    air_quality_index: float

# Initialize an empty list of sensor data for testing
sensor_data_storage = []

@app.get("/get_sensor_data")
async def get_sensor_data():
    """
    Endpoint to fetch the last collected sensor data.
    Returns:
        list: List of sensor data dictionaries.
    """
    return sensor_data_storage

@app.post("/collect_sensor_data")
async def collect_sensor_data(sensor_data: SensorData):
    """
    Endpoint to receive and store sensor data.
    Args:
        sensor_data (SensorData): The sensor data collected from IoT devices.
    """
    # Initialize the Logger with sensor_id and district from the request
    logger = Logger(district=sensor_data.district, sensor_id=sensor_data.sensor_id)
    
    # Log the incoming sensor data request
    logger.log_incoming_request(sensor_data.dict())
    
    # Simulate storing the sensor data
    sensor_data_storage.append(sensor_data.dict())
    return {"message": "Sensor data collected successfully"}

@app.post("/collect_multiple_sensor_data")
async def collect_multiple_sensor_data(sensor_data_list: List[SensorData]):
    """
    Endpoint to receive and store multiple sensor data entries.
    Args:
        sensor_data_list (List[SensorData]): List of sensor data collected from multiple sensors.
    """
    for sensor_data in sensor_data_list:
        # Initialize the Logger with sensor_id and district from the request
        logger = Logger(district=sensor_data.district, sensor_id=sensor_data.sensor_id)
        
        # Log each incoming sensor data request
        logger.log_incoming_request(sensor_data.dict())
        
        # Simulate storing the sensor data
        sensor_data_storage.append(sensor_data.dict())
        
    return {"message": "Multiple sensor data collected successfully"}

# Log API shutdown (this doesn't require district or sensor_id)
@app.on_event("shutdown")
def shutdown_event():
    logger = Logger(district='default_district', sensor_id='default_sensor')
    logger.log_api_shutdown()
