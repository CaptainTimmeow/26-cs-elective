# Week 4 Homework: APIs and HTTP Requests

## Due: [Insert Due Date]

Complete the homework assignment that matches your level. Choose the level that challenges you appropriately.

---

## Level 1: Not Yet

### Task: API Basics Practice

**Objective:** Learn to make a simple API request

**Requirements:**
1. Use JSONPlaceholder API (no API key needed)
2. Make a GET request to fetch a single post
3. Print the post's title and body

**Starter Code:**
```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

# Your task:
# 1. Make a GET request: requests.get(url)
# 2. Check if successful (response.status_code)
# 3. Convert to JSON: response.json()
# 4. Print title and body
```

**Example Output:**
```
Title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
Body: quia et suscipit\nsuscipit recusandae consequuntur ...
```

---

## Level 2: Developing

### Task: Country Information Fetcher

**Objective:** Fetch and display real data from an API

**Requirements:**
1. Use REST Countries API: `https://restcountries.com/v3.1/name/{country}`
2. Ask user for a country name
3. Display: Country name, Capital, Population, Region
4. Handle "country not found" error

**Starter Code:**
```python
import requests

country = input("Enter a country name: ")
url = f"https://restcountries.com/v3.1/name/{country}"

# Your task:
# 1. Make GET request
# 2. Check if found (status code 200)
# 3. Parse JSON (returns a list!)
# 4. Print: name, capital[0], population, region
```

**Example Output:**
```
Enter a country name: Japan
Country: Japan
Capital: Tokyo
Population: 125800000
Region: Asia
```

---

## Level 3: Proficient

### Task: Weather Lookup

**Objective:** Use two APIs together (geocoding + weather)

**Requirements:**
1. Use Open-Meteo APIs (free, no key)
2. Ask user for a city name
3. Use geocoding API to get coordinates
4. Use weather API to get current temp and conditions
5. Show 3-day forecast

**Starter Code:**
```python
import requests

city = input("Enter city name: ")

# Step 1: Get coordinates
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
geo_response = requests.get(geo_url).json()

if geo_response.get('results'):
    lat = geo_response['results'][0]['latitude']
    lon = geo_response['results'][0]['longitude']
    
    # Step 2: Get weather
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
    weather = requests.get(weather_url).json()
    
    # Step 3: Display current weather
    temp = weather['current']['temperature_2m']
    code = weather['current']['weather_code']
    print(f"Current temp in {city}: {temp}°C")
    
    # Step 4: Display 3-day forecast
    # ... your code here
else:
    print("City not found!")
```

**Example Output:**
```
Enter city name: Shanghai
Current temp in Shanghai: 18°C
3-Day Forecast:
Today: 22°C/15°C
Tomorrow: 20°C/14°C
Wed: 21°C/15°C
```

---

## Level 4: Advanced

### Task: Combined API Explorer

**Objective:** Build a useful tool combining multiple APIs

**Requirements:**
1. Create a menu with 3 options:
   - Look up a country
   - Check weather for a city
   - Get a random joke
2. Use at least 2 different APIs
3. Handle errors gracefully
4. Allow user to use multiple times

**Bonus (optional):**
- Add currency conversion using the country API
- Save search history to a list

**API Options:**
- Countries: `https://restcountries.com/v3.1/name/{name}`
- Weather: `https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m`
- Jokes: `https://official-joke-api.appspot.com/random_joke`

**Example Output:**
```
=== API Explorer ===
1. Country Info
2. Weather
3. Random Joke
4. Exit

Choice: 1
Enter country: Brazil
Country: Brazil
Capital: Brasilia
Population: 212559417
Region: Americas

Choice: 2
Enter city: Tokyo
Weather in Tokyo: 20°C

Choice: 3
Here's a random joke:
Why don't scientists trust atoms?
Because they make up everything!

Choice: 4
Goodbye!
```

---

## Submission

1. Save your code as `homework_week4.py`
2. Test with at least 3 different inputs
3. Submit on Canvas
