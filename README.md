# ⚡ EnergiSense - Smart Energy Forecast & Scheduling System
🌟 Overview

The Smart Energy Forecast & Scheduling System is an AI-powered prototype that demonstrates advanced energy management through machine learning and reinforcement learning techniques. The system provides:


- Energy Demand Forecasting using LSTM neural networks
- Renewable Energy Prediction using ConvLSTM models
- Intelligent Energy Scheduling using Reinforcement Learning

# 🎯 Key Features

🔋 LSTM Energy Demand Forecasting

- Predicts energy consumption for the next 24 hours
- Uses historical consumption patterns
- Handles seasonal and daily variations
- Achieves high accuracy with deep learning

🌞 ConvLSTM Renewable Energy Forecasting

- Forecasts solar and wind energy production
- Incorporates weather data (sunlight, wind speed, cloud cover)
- Spatiotemporal pattern recognition
- Real-time renewable energy optimization

🤖 RL-Based Smart Scheduling

- Optimizes energy usage decisions in real-time
- Balances cost, sustainability, and reliability
- Battery management and grid interaction
- Dynamic pricing adaptation

🚀 Quick Start
-
- Prerequisites

``` Python 3.8 or higher ```

``` pip package manager ```


- Installation

1. Clone the repository
```bash
git clone https://github.com/AtharvaAdmile/EnergiSense
```

```bash
cd EnergiSense
```
2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
streamlit run src/app.py
```
4. Open your browser and navigate to
```bash
http://localhost:8501
```
# 🏗️ System Architecture
graph TB

   A[Historical Energy Data] --> B[LSTM Model]

  C[Weather Data] --> D[ConvLSTM Model]

  B --> E[Energy Demand Forecast]

  D --> F[Renewable Energy Forecast]

  E --> G[RL Scheduler]

  F --> G

  G --> H[Optimal Energy Schedule]

  H --> I[Cost Optimization]    

  H --> J[Battery Management]

  H --> K[Grid Interaction]
# 📊 Usage Guide
Step 1: Generate Energy Demand Forecast

1. Navigate to "LSTM (Energy Demand)" in the sidebar
2. The system will automatically generate synthetic historical data
3. View the 24-hour energy demand prediction
4. Review consumption patterns and peak hours

Step 2: Generate Renewable Energy Forecast

Navigate to "ConvLSTM (Renewables)" in the sidebar
System generates weather data and renewable patterns
View solar and wind energy forecasts
Analyze renewable energy availability
