import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

# Load dataset
data = pd.read_csv("collected_sensor_data.csv")  # Replace with your dataset path
data['timestamp'] = pd.to_datetime(data['timestamp'])
data.set_index('timestamp', inplace=True)

# Choose the target variable
target_variable = 'water_level'
series = data[target_variable].dropna()

# Visualize the time-series
plt.figure(figsize=(10, 5))
plt.plot(series, label='Water Level')
plt.title('Time Series of Water Level')
plt.xlabel('Time')
plt.ylabel('Water Level')
plt.legend()
plt.show()

# Test for stationarity using ADF (Augmented Dickey-Fuller) test
result = adfuller(series)
print(f"ADF Statistic: {result[0]}")
print(f"p-value: {result[1]}")
if result[1] > 0.05:
    print("Data is non-stationary. Differencing is required.")
else:
    print("Data is stationary. Proceeding with ARIMA.")

# Differencing if necessary
if result[1] > 0.05:
    series_diff = series.diff().dropna()
else:
    series_diff = series

# Fit the ARIMA model
model = ARIMA(series_diff, order=(1, 1, 1))  # Replace (p, d, q) with appropriate values
model_fit = model.fit()

# Summary of the model
print(model_fit.summary())

# Forecast future values
forecast_steps = 30  # Predict next 30 steps (e.g., days)
forecast = model_fit.forecast(steps=forecast_steps)
forecast_index = pd.date_range(series.index[-1], periods=forecast_steps + 1, freq='D')[1:]

# Plot forecast
plt.figure(figsize=(10, 5))
plt.plot(series, label='Historical Data')
plt.plot(forecast_index, forecast, label='Forecast', linestyle='--')
plt.title('ARIMA Forecast for Water Level')
plt.xlabel('Time')
plt.ylabel('Water Level')
plt.legend()
plt.show()
