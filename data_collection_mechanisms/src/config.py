import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# General settings
DATA_COLLECTION_INTERVAL = int(os.getenv("DATA_COLLECTION_INTERVAL", 7))
DISTRICTS = os.getenv("DISTRICTS", "District_1,District_2").split(",")
SENSORS_PER_DISTRICT = int(os.getenv("SENSORS_PER_DISTRICT", 7))

# PostgreSQL configuration
POSTGRES_CONFIG = {
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": int(os.getenv("POSTGRES_PORT", 5432)),
    "database": os.getenv("POSTGRES_DATABASE", "weather_data"),
    "user": os.getenv("POSTGRES_USER", "opecli_cdo"),
    "password": os.getenv("POSTGRES_PASSWORD"),
}

# CSV backup settings
BACKUP_DIRECTORY = os.getenv("BACKUP_DIRECTORY", os.path.join(os.getcwd(), "backups"))
