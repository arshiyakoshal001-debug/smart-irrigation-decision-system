# Smart Irrigation Decision System
# Simple rule-based prototype for learning.

import pandas as pd

df = pd.read_csv("irrigation_dataset.csv")

def recommend_irrigation(soil_moisture, rain_forecast):
    if soil_moisture < 30 and rain_forecast < 10:
        return "Irrigate"
    elif soil_moisture < 40 and rain_forecast < 5:
        return "Consider irrigation"
    return "No irrigation"

df["generated_recommendation"] = df.apply(
    lambda row: recommend_irrigation(row["soil_moisture_pct"], row["rain_forecast_mm"]),
    axis=1
)

print(df.head(10))
