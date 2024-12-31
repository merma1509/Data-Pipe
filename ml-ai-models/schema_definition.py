from pyspark.sql.types import StructType, StructField, IntegerType, FloatType, TimestampType, StringType

class SchemaDefinition:
    @staticmethod
    def weather_data_schema():
        return StructType([
            StructField("record_id", StringType(), True),          # Record Id
            StructField("source_id", IntegerType(), True),         # Source Id
            StructField("location", StringType(), True),           # Recording Location
            StructField("timestamp", TimestampType(), True),       # Recording Timestamp   
            StructField("temperature", FloatType(), True),         # Temperature in C
            StructField("precipitation", FloatType(), True),       # Precipitation in mm
            StructField("humidity", FloatType(), True),            # Humidity in %
            StructField("wind_speed", FloatType(), True),          # Wind Speed in km/h
            StructField("wind_direction", IntegerType(), True),    # Wind Direction 
            StructField("soil_moisture", FloatType(), True),       # Soil Moisture in %
            StructField("air_pressure", FloatType(), True),        # Barometric Pressure in Pa
        ])