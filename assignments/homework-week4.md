# Week 4 Homework: APIs and HTTP Requests

## Due: [Insert Due Date]

Complete the homework assignment that matches your level. Read the descriptions carefully to choose the right level - you should be challenged but not overwhelmed.

---

## Level 1: Not Yet

### Task: API Basics Practice

**Objective:** Demonstrate understanding of basic API concepts

**Requirements:**
1. Use the JSONPlaceholder API (no API key needed)
2. Make a GET request to fetch a single post
3. Print the post's title and body

**Starter Code:**
```python
import requests

# Fetch post #1
url = "https://jsonplaceholder.typicode.com/posts/1"

# Add your code here:
# 1. Make a GET request
# 2. Check if successful (status code 200)
# 3. Convert to JSON
# 4. Print the title and body
```

**Example Output:**
```
Title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
Body: quia et suscipit\nsuscipit recusandae consequuntur ...
```

**Grading:**
- Uses requests.get() correctly: 2 points
- Checks status code: 2 points
- Correctly parses JSON: 2 points
- Prints title and body: 2 points
- Code runs without errors: 2 points

---

## Level 2: Developing

### Task: Country Information Fetcher

**Objective:** Fetch and display data from a real API

**Requirements:**
1. Use REST Countries API: `https://restcountries.com/v3.1/name/{country}`
2. Ask user to input a country name
3. Display the following information:
   - Country name
   - Capital
   - Population
   - Region
   - Language(s)
4. Handle errors (country not found, network error)
5. Allow the user to search again or quit

**Starter Code:**
```python
import requests

def search_country():
    # Ask user for country name
    country = input("Enter a country name (or 'quit' to exit): ")
    
    if country.lower() == 'quit':
        return False
    
    # Make API request
    url = f"https://restcountries.com/v3.1/name/{country}"
    
    # Add your code here:
    # 1. Make GET request
    # 2. Check status code
    # 3. Parse JSON
    # 4. Extract and display country info
    # 5. Handle errors (try/except)
    
    return True

# Main loop
while search_country():
    print()

print("Goodbye!")
```

**Example Output:**
```
Enter a country name: Japan
Country: Japan 🇯🇵
Capital: Tokyo
Population: 125,800,000
Region: Asia
Languages: Japanese

Enter a country name: France
Country: France 🇫🇷
Capital: Paris
Population: 67,390,000
Region: Europe
Languages: French

Enter a country name (or 'quit' to exit): quit
Goodbye!
```

**Grading:**
- Successful API call: 2 points
- Displays all 5 fields correctly: 5 points
- Error handling (not found): 2 points
- Error handling (network error): 2 points
- Loop allows multiple searches: 2 points
- Code quality and comments: 2 points

---

## Level 3: Proficient

### Task: Weather Dashboard

**Objective:** Build a useful application using a weather API

**Requirements:**
1. Use Open-Meteo API (free, no API key): `https://api.open-meteo.com/v1/forecast`
2. Ask user for a city name (you can use hardcoded coordinates or geocoding)
3. Display:
   - Current temperature
   - Weather condition (sunny, cloudy, rainy, etc.)
   - Humidity
   - Wind speed
   - High/Low for the day
4. Show a 3-day forecast
5. Proper error handling

**Geocoding Option:** Use `https://geocoding-api.open-meteo.com/v1/search?name={city}`

**Starter Code:**
```python
import requests

def get_coordinates(city_name):
    """Get latitude and longitude for a city"""
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}"
    # Add your code here
    
def get_weather(lat, lon):
    """Get weather data for coordinates"""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
    # Add your code here

def main():
    city = input("Enter a city name: ")
    
    # Step 1: Get coordinates
    coords = get_coordinates(city)
    if not coords:
        print("City not found!")
        return
    
    # Step 2: Get weather
    weather = get_weather(coords['lat'], coords['lon'])
    
    # Step 3: Display current weather
    print(f"\nWeather in {city}:")
    print(f"Temperature: {weather['current']['temperature_2m']}°C")
    # Add more...
    
    # Step 4: Display 3-day forecast
    print("\n3-Day Forecast:")
    # Add your code here

if __name__ == "__main__":
    main()
```

**Example Output:**
```
Enter a city name: Shanghai
Weather in Shanghai:
Temperature: 18°C
Condition: Partly Cloudy
Humidity: 65%
Wind: 12 km/h
High: 22°C | Low: 15°C

3-Day Forecast:
Tue: ⛅ 22°C / 16°C
Wed: 🌧️ 19°C / 14°C
Thu: ⛅ 21°C / 15°C
```

**Grading:**
- Geocoding works: 2 points
- Current weather displays correctly: 3 points
- All 5 metrics shown: 2 points
- 3-day forecast displayed: 3 points
- Error handling: 2 points
- Clean output formatting: 2 points
- Code quality: 1 point

---

## Level 4: Advanced

### Task: Cryptocurrency Portfolio Tracker

**Objective:** Build a comprehensive portfolio tracking application

**Requirements:**
1. Use CoinGecko API (free, no key): `https://api.coingecko.com/api/v3/`
2. Features required:
   - Show top 10 cryptocurrencies by market cap
   - Search for any coin by name
   - **Portfolio tracking:** Allow user to add holdings (coin, amount)
   - Calculate total portfolio value in USD
   - Show 24h price change for each coin
   - Calculate profit/loss for portfolio
3. Save portfolio to a JSON file
4. Load portfolio on startup

**API Endpoints:**
- Top coins: `/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10`
- Search: `/search?query={term}`
- Coin details: `/coins/{id}?localization=false&tickers=false&community_data=false&developer_data=false`

**Bonus Challenges (choose at least 2):**
- [ ] Add price alerts (notify when coin crosses threshold)
- [ ] Show 7-day price history chart (use matplotlib)
- [ ] Add coin comparison feature
- [ ] Implement portfolio diversification analysis
- [ ] Add "watchlist" feature separate from portfolio

**Starter Code:**
```python
import requests
import json
from datetime import datetime

class CryptoPortfolio:
    def __init__(self):
        self.portfolio = {}  # {coin_id: amount}
        self.load()
    
    def load(self):
        """Load portfolio from file"""
        try:
            with open('portfolio.json', 'r') as f:
                self.portfolio = json.load(f)
        except FileNotFoundError:
            self.portfolio = {}
    
    def save(self):
        """Save portfolio to file"""
        with open('portfolio.json', 'w') as f:
            json.dump(self.portfolio, f, indent=2)
    
    def get_top_coins(self):
        """Get top 10 cryptocurrencies"""
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 10,
            'page': 1
        }
        response = requests.get(url, params=params)
        return response.json()
    
    def search_coin(self, query):
        """Search for a coin"""
        # Add your code
    
    def add_holding(self, coin_id, amount):
        """Add coins to portfolio"""
        # Add your code
    
    def calculate_value(self, prices):
        """Calculate total portfolio value"""
        # Add your code
    
    def display_top(self):
        """Display top 10 coins"""
        # Add your code
    
    def display_portfolio(self, prices):
        """Display current holdings"""
        # Add your code

def main():
    portfolio = CryptoPortfolio()
    
    while True:
        print("\n=== Crypto Portfolio Tracker ===")
        print("1. View Top 10 Cryptocurrencies")
        print("2. Search for a Coin")
        print("3. Add to Portfolio")
        print("4. View Portfolio")
        print("5. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            # Display top coins
            pass
        elif choice == '2':
            # Search coin
            pass
        elif choice == '3':
            # Add holding
            pass
        elif choice == '4':
            # View portfolio
            pass
        elif choice == '5':
            portfolio.save()
            print("Portfolio saved. Goodbye!")
            break

if __name__ == "__main__":
    main()
```

**Example Output:**
```
=== Crypto Portfolio Tracker ===
1. View Top 10 Cryptocurrencies
2. Search for a Coin
3. Add to Portfolio
4. View Portfolio
5. Exit

Enter your choice: 1

Top 10 Cryptocurrencies:
1. Bitcoin (BTC)     $45,234.56   +2.34%
2. Ethereum (ETH)     $2,567.89    +1.56%
3. Tether (USDT)     $1.00        +0.01%
...
```

**Grading:**
- Top 10 display: 2 points
- Coin search: 2 points
- Add holdings: 2 points
- Portfolio value calculation: 3 points
- 24h change display: 2 points
- JSON file save/load: 2 points
- Error handling: 2 points
- Bonus features: 2 points each (max 4 points)
- Code quality: 1 point

---

## Submission Instructions

1. Save your code with a clear filename (e.g., `homework_week4.py`)
2. Test with multiple inputs
3. Take a screenshot of your output
4. Submit on Canvas

**Late submissions:** -10% per day
