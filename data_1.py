import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Configuration
START_TIME = "2025-08-04 00:00:00"
END_TIME = "2025-08-04 23:59:59"
INTERVAL_MINUTES = 30  # Data point every 30 minutes
OUTPUT_CSV = "energy_data.csv"
DEVICES = [
    {"id": "AC_01", "type": "AC", "room": "Living Room", "base_kwh": 1.0, "peak_hours": [(7, 10), (18, 22)]},
    {"id": "Light_01", "type": "Light", "room": "Kitchen", "base_kwh": 0.05, "peak_hours": [(6, 22)]},
    {"id": "Light_02", "type": "Light", "room": "Bedroom", "base_kwh": 0.03, "peak_hours": [(6, 22)]},
    {"id": "Fan_01", "type": "Fan", "room": "Living Room", "base_kwh": 0.07, "peak_hours": [(8, 20)]},
    {"id": "Geyser_01", "type": "Geyser", "room": "Bathroom", "base_kwh": 2.0, "peak_hours": [(6, 9), (19, 21)]}
]

# Function to generate realistic energy consumption
def generate_energy_usage(device, current_time):
    hour = current_time.hour
    base_kwh = device["base_kwh"]
    is_peak = any(start <= hour < end for start, end in device["peak_hours"])
    
    # Nighttime (00:00–05:59): Most devices idle
    if 0 <= hour < 6:
        if device["type"] in ["AC", "Geyser"]:
            return 0.0  # Idle at night
        return base_kwh * random.uniform(0.0, 0.2)  # Minimal usage for lights/fans
    
    # Peak hours: Higher usage
    if is_peak:
        if device["type"] in ["AC", "Geyser"]:
            return base_kwh * random.uniform(0.8, 1.2)  # High usage
        return base_kwh * random.uniform(0.7, 1.0)  # Moderate usage for lights/fans
    
    # Non-peak daytime: Moderate usage
    if device["type"] in ["Light", "Fan"]:
        return base_kwh * random.uniform(0.4, 0.8)
    return base_kwh * random.uniform(0.2, 0.5)  # Low usage for AC/geyser

# Generate timestamps
start = datetime.strptime(START_TIME, "%Y-%m-%d %H:%M:%S")
end = datetime.strptime(END_TIME, "%Y-%m-%d %H:%M:%S")
timestamps = []
current = start
while current <= end:
    timestamps.append(current)
    current += timedelta(minutes=INTERVAL_MINUTES)

# Generate data
data_stream = []  # Simulates queue/array for real-time streaming
records = []
for timestamp in timestamps:
    for device in DEVICES:
        energy_kwh = generate_energy_usage(device, timestamp)
        record = {
            "Timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "Device_ID": device["id"],
            "Energy_Consumption_kWh": round(energy_kwh, 3),
            "Room": device["room"]
        }
        records.append(record)
        data_stream.append(record)  # Add to data stream

# Save to CSV
df = pd.DataFrame(records)
df.to_csv(OUTPUT_CSV, index=False)
print(f"Data saved to {OUTPUT_CSV}")

# Example: Print first few records in data stream
print("\nSample Data Stream (first 5 records):")
for record in data_stream[:5]:
    print(record)