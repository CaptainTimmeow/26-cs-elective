"""
Week 4 Homework - Level 3: Proficient
Weather Lookup with 3-Day Forecast
"""

import requests

# Weather code meanings
WEATHER = {
    0: "Clear", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 51: "Drizzle", 61: "Rain", 63: "Rain",
    71: "Snow", 80: "Showers", 95: "Thunderstorm"
}

city = input("Enter city name: ")

# ============================================
# Step 1: Get coordinates using geocoding API
# ============================================
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
geo_response = requests.get(geo_url).json()

if 'results' not in geo_response:
    print(f"City '{city}' not found!")
    exit()

# Extract coordinates
lat = geo_response['results'][0]['latitude']
lon = geo_response['results'][0]['longitude']
display_name = geo_response['results'][0]['name']

# ============================================
# Step 2: Get weather data
# ============================================
weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code&daily=temperature_2m_max,temperature_2m_min&timezone=auto&forecast_days=3"
weather = requests.get(weather_url).json()

# ============================================
# Step 3: Display current weather
# ============================================
current = weather['current']
temp = current['temperature_2m']
code = current['weather_code']
condition = WEATHER.get(code, "Unknown")

print(f"\n{'='*40}")
print(f"Weather in {display_name}")
print(f"{'='*40}")
print(f"Current: {temp}°C - {condition}")

# ============================================
# Step 4: Display 3-day forecast
# ============================================
daily = weather['daily']
dates = daily['time']
maxTemps = daily['temperature_2m_max']
minTemps = daily['temperature_2m_min']

print(f"\n3-Day Forecast:")
for i in range(len(dates)):
    print(f"  {dates[i]}: {maxTemps[i]}°C / {minTemps[i]}°C")

print(f"{'='*40}")
