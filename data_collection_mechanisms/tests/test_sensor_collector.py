import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) # Add the parent directory to the sys.path
from src.services.sensor_collector import SensorDataCollector

class TestSensorDataCollector(unittest.TestCase):

    def test_collect_data(self):
        sensor = SensorDataCollector(sensor_id="District1_Sensor_1", district="District1", location="Location_1")
        data = sensor.collect_data()
        self.assertIn("sensor_id", data)
        self.assertIn("timestamp", data)
        self.assertIn("temperature", data)
        self.assertIn("precipitation", data)
        print(data)

    def test_get_sensor_data(self):
        sensor = SensorDataCollector(sensor_id="District1_Sensor_1", district="District1", location="Location_1")
        data = sensor.get_sensor_data()
        self.assertIsInstance(data, dict)
        self.assertGreater(len(data), 0)
        print(len(data))

if __name__ == "__main__":
    unittest.main()
