# Data Collection Mechanisms

## Overview
The **Data Collection Mechanisms** module is responsible for collecting and managing sensor data for the OpenClimate project. This module plays a critical role in acquiring raw data from IoT sensors, pre-processing it, and preparing it for ingestion into the broader data pipeline. The collected data is stored in CSV files and used as input for further analysis and processing.

## Features
- **Sensor Integration**: Interfaces with IoT sensors to gather real-time environmental data.
- **Configurable Parameters**: Allows dynamic configuration of sensor collection intervals and data storage settings.
- **Data Validation**: Ensures incoming data is valid, clean, and consistent.
- **CSV Storage**: Stores collected data in daily CSV files for easy backup and portability.
- **Scalable Architecture**: Modular design supports integration of new sensors and data types.
- **Error Logging**: Logs errors and anomalies during data collection.


## Folder Structure

```
data_collection_mechanims/
├── README.md           # Documentation for the module
├── requirements.txt    # Python dependencies for the module
├── src/                # Source code for the module
│   ├── __init__.py     # Initializes the package
│   ├── config.py       # Configuration settings
│   ├── main.py         # Entry point for data collection
│   ├── models.py       # Data models for the collected data
│   ├── services/       # Business logic for data collection
│   ├── utils/          # Utility functions
├── tests/              # Unit tests for the module
│   ├── __init__.py     # Initializes the test package
│   ├── test_sensor_collector.py # Tests for the data collection logic
├── venv/               # Virtual environment for the module
```

## Prerequisites
- Python 3.8+
- Virtual environment (venv) for managing dependencies

## Installation
1. Clone the repository and navigate to the `Data_collection_mechanims` directory:
   ```bash
   git clone https://github.com/github-username/OpenClimate/data_collection_mechanisms.git
   cd data_collection_mechanims
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # For Linux/MacOS
   venv\Scripts\activate      # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. Configure the collection settings in `src/config.py`:
   - Set the data collection interval.
   - Specify output file paths for CSV storage.

2. Run the main script to start data collection:
   ```bash
   python3 src/main.py   # For Linux/MacOs
   python scr/main.py    # For Windows
   ```

3. Collected data will be stored in CSV files organized by date.

## Testing
Run unit tests to verify functionality:
```bash
pytest tests/
```

## Configuration
Modify the `config.py` file to customize the following:
- Sensor connection parameters (e.g., API keys, serial ports).
- Data collection intervals.
- Output directory for CSV files.

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature-name'`).
4. Push the branch (`git push origin feature-name`).
5. Open a pull request.

## Contact
For any questions or contributions, please contact the project team at [info@topenclimate.org](mailto:info@theopenclimate.org).

