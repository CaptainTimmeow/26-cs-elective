"""
Week 4 Homework - Level 2: Developing
Country Information Fetcher
"""

import requests

# Get input from user
country = input("Enter a country name: ")

# Build the API URL
url = f"https://restcountries.com/v3.1/name/{country}"

# ============================================
# YOUR CODE:
# ============================================
# 1. Make GET request
response = requests.get(url)

# 2. Check if country was found (status code 200)
if response.status_code == 200:
    # 3. Parse JSON - API returns a LIST!
    data = response.json()
    country_data = data[0]  # Get first result
    
    # 4. Extract information
    name = country_data['name']['common']
    capital = country_data['capital'][0]
    population = country_data['population']
    region = country_data['region']
    
    # 5. Print nicely
    print("\n" + "=" * 30)
    print(f"Country: {name}")
    print(f"Capital: {capital}")
    print(f"Population: {population:,}")
    print(f"Region: {region}")
    print("=" * 30)
else:
    print(f"Error: Country '{country}' not found!")
