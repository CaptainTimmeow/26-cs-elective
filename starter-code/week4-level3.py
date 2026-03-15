"""
Week 4 Starter Code - Level 3: Proficient
Weather Dashboard
"""

import requests

# Weather codes mapping (Open-Meteo)
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Foggy",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
}

def get_coordinates(city_name):
    """Get latitude and longitude for a city using geocoding API"""
    
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}"
    
    # ============================================
    # YOUR CODE HERE:
    # ============================================
    # 1. Make GET request
    # 2. Check status code
    # 3. Parse JSON
    # 4. Return dict with 'lat' and 'lon' keys
    # Return None if city not found
    
    return {'lat': 31.23, 'lon': 121.47}  # Placeholder - replace with real code

def get_weather(lat, lon):
    """Get weather data for coordinates"""
    
    url = f"https://api.open-meteo.com/v1/forecast"
    params = {
        'latitude': lat,
        'longitude': lon,
        'current': 'temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m',
        'daily': 'temperature_2m_max,temperature_2m_min,weather_code',
        'timezone': 'auto',
        'forecast_days': 3
    }
    
    # ============================================
    # YOUR CODE HERE:
    # ============================================
    # 1. Make GET request with params
    # 2. Parse JSON
    # 3. Return the weather data
    
    return {}  # Placeholder - replace with real code

def display_weather(city, weather_data):
    """Display weather information nicely"""
    
    current = weather_data.get('current', {})
    daily = weather_data.get('daily', {})
    
    # ============================================
    # YOUR CODE HERE:
    # ============================================
    # Extract and display:
    # - Current temperature
    # - Weather condition (use WEATHER_CODES mapping)
    # - Humidity
    # - Wind speed
    # - Daily high/low
    
    print("\n" + "=" * 40)
    print(f"Weather in {city}")
    print("=" * 40)
    # Add your print statements here
    
    # Display 3-day forecast
    print("\n3-Day Forecast:")
    # Loop through daily data and print

def main():
    city = input("Enter a city name: ")
    
    # Step 1: Get coordinates
    coords = get_coordinates(city)
    if not coords:
        print(f"City '{city}' not found!")
        return
    
    # Step 2: Get weather data
    weather = get_weather(coords['lat'], coords['lon'])
    
    # Step 3: Display weather
    display_weather(city, weather)

if __name__ == "__main__":
    main()
