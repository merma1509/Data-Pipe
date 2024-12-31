import os
from pyspark.sql import SparkSession, DataFrame, functions as F
from schema_definition import SchemaDefinition  
from pyspark.sql.types import StructType
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

class RealTimeDataCollector:
    def __init__(self, kafka_broker: str, kafka_topics: list, schema: StructType):
        """Initialize the real-time data collector."""
        self.spark = SparkSession.builder.appName("RealTimeFloodPrediction").getOrCreate()
        self.kafka_broker = kafka_broker
        self.kafka_topics = ",".join(kafka_topics)
        self.schema = schema

    def collect_data(self) -> DataFrame:
        """Collect real-time data from Kafka."""
        raw_stream = self.spark.readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", self.kafka_broker) \
            .option("subscribe", self.kafka_topics) \
            .load()

        # Parse and transform data
        transformed_stream = raw_stream.selectExpr("CAST(value AS STRING)") \
            .select(F.from_json(F.col("value"), self.schema).alias("data")) \
            .select("data.*")

        return transformed_stream


class HistoricalDataCollector:
    def __init__(self, spark_session: SparkSession, db_url: str, db_properties: dict):
        """Initialize the historical data collector for PostgreSQL."""
        self.spark = spark_session
        self.db_url = db_url
        self.db_properties = db_properties

    def collect_data(self, table_name: str) -> DataFrame:
        """Collect historical data from PostgreSQL."""
        df = self.spark.read \
            .format("jdbc") \
            .option("url", self.db_url) \
            .option("dbtable", table_name) \
            .option("driver", self.db_properties["driver"]) \
            .option("user", self.db_properties["user"]) \
            .option("password", self.db_properties["password"]) \
            .load()
        return df


class S3DataCollector:
    def __init__(self, spark_session: SparkSession, s3_path: str):
        """Initialize the S3 data collector."""
        self.spark = spark_session
        self.s3_path = s3_path

    def collect_data(self, file_format: str = "parquet") -> DataFrame:
        """Collect historical data from S3."""
        df = self.spark.read.format(file_format).load(self.s3_path)
        return df


class DataCollectorPipeline:
    def __init__(self, real_time_collector: RealTimeDataCollector, historical_pg_collector: HistoricalDataCollector, historical_s3_collector: Optional[S3DataCollector] = None):
        """Initialize the data collector pipeline."""
        self.real_time_collector = real_time_collector
        self.historical_pg_collector = historical_pg_collector
        self.historical_s3_collector = historical_s3_collector

    def collect_and_combine_data(self, pg_table: str) -> DataFrame:
        """Collect and combine real-time and historical data into a unified dataset."""
        print("Collecting real-time data...")
        real_time_data = self.real_time_collector.collect_data()

        print("Collecting historical data from PostgreSQL...")
        historical_data_pg = self.historical_pg_collector.collect_data(pg_table)

        # Collect data from S3
        if self.historical_s3_collector:
            print("Collecting historical data from S3...")
            historical_data_s3 = self.historical_s3_collector.collect_data()
            combined_historical_data = historical_data_pg.unionByName(historical_data_s3)
        else:
            combined_historical_data = historical_data_pg

        # Combine real-time and historical datasets
        unified_dataset = real_time_data.unionByName(combined_historical_data)
        return unified_dataset


if __name__ == "__main__":
    # Initialize Spark
    spark = SparkSession.builder.appName("FloodPredictionPipeline").getOrCreate()

    # Load environment variables
    kafka_broker = os.getenv("KAFKA_BROKER", "kafka:9092")
    kafka_topics = os.getenv("KAFKA_TOPICS", "weather-data").split(",")
    db_url = f"jdbc:postgresql://postgres:5432/{os.getenv('POSTGRES_DB')}"
    db_properties = {
        "driver": "org.postgresql.Driver",
        "user": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD"),
    }
    s3_path = os.getenv("S3_PATH", None)
# Define schema for real-time data
schema = SchemaDefinition.weather_data_schema()

# Initialize collectors
real_time_collector = RealTimeDataCollector(kafka_broker, kafka_topics, schema)
historical_collector_pg = HistoricalDataCollector(spark, db_url, db_properties)
historical_collector_s3 = S3DataCollector(spark, s3_path) if s3_path else None

# Combine all data into a single dataset
data_pipeline = DataCollectorPipeline(real_time_collector, historical_collector_pg, historical_collector_s3)
unified_dataset = data_pipeline.collect_and_combine_data("validated_data")

# Save or process the unified dataset
output_path = "./output/unified_dataset.parquet"
unified_dataset.write.mode("overwrite").parquet(output_path)
print(f"Unified dataset saved to {output_path}.")
