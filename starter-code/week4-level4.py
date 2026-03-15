"""
Week 4 Homework - Level 4: Advanced
Combined API Explorer

BONUS: Save search history!
"""

import requests
import json

# Weather code meanings
WEATHER = {
    0: "Clear", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 51: "Drizzle", 61: "Rain", 63: "Rain",
    71: "Snow", 80: "Showers", 95: "Thunderstorm"
}

history = []

def search_country():
    """Look up country information"""
    country = input("Enter country name: ")
    url = f"https://restcountries.com/v3.1/name/{country}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()[0]
        result = f"Country: {data['name']['common']}\n"
        result += f"Capital: {data['capital'][0]}\n"
        result += f"Population: {data['population']:,}\n"
        result += f"Region: {data['region']}"
        print(result)
        history.append(f"Country: {data['name']['common']}")
    else:
        print("Country not found!")

def check_weather():
    """Check weather for a city"""
    city = input("Enter city name: ")
    
    # Get coordinates
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo = requests.get(geo_url).json()
    
    if 'results' not in geo:
        print("City not found!")
        return
    
    lat = geo['results'][0]['latitude']
    lon = geo['results'][0]['longitude']
    
    # Get weather
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code"
    w = requests.get(weather_url).json()
    
    temp = w['current']['temperature_2m']
    code = w['current']['weather_code']
    
    result = f"Weather in {city}: {temp}°C - {WEATHER.get(code, 'Unknown')}"
    print(result)
    history.append(result)

def get_joke():
    """Get a random joke"""
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url).json()
    
    print(f"\n{response['setup']}")
    print(f"{response['punchline']}\n")
    history.append(f"Joke: {response['setup']}")

def show_history():
    """Show search history"""
    if not history:
        print("No history yet!")
    else:
        print("\n--- Search History ---")
        for item in history:
            print(f"  - {item}")
        print()

def main():
    while True:
        print("\n=== API Explorer ===")
        print("1. Country Info")
        print("2. Weather")
        print("3. Random Joke")
        print("4. Search History")
        print("5. Exit")
        
        choice = input("\nChoice: ")
        
        if choice == '1':
            search_country()
        elif choice == '2':
            check_weather()
        elif choice == '3':
            get_joke()
        elif choice == '4':
            show_history()
        elif choice == '5':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
