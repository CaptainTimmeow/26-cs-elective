"""
Week 4 Starter Code - Level 2: Developing
Country Information Fetcher
"""

import requests

def search_country():
    """Search for a country and display its information"""
    
    # Ask user for country name
    country = input("Enter a country name (or 'quit' to exit): ")
    
    if country.lower() == 'quit':
        return False
    
    # ============================================
    # YOUR CODE HERE:
    # ============================================
    
    # 1. Build the API URL
    # API: https://restcountries.com/v3.1/name/{name}
    url = f"https://restcountries.com/v3.1/name/{country}"
    
    # 2. Make a GET request
    # Use try/except to handle errors
    
    # 3. Check if the request was successful (status code 200)
    
    # 4. Parse the JSON response
    # The API returns a LIST, so use data[0] to get the first result
    
    # 5. Extract and display:
    # - name['common'] (country name)
    # - capital[0] (capital city)
    # - population (population number)
    # - region (region like Asia, Europe)
    # - languages (dictionary of languages)
    
    # ============================================
    # EXPECTED OUTPUT:
    # ============================================
    # Enter a country name: Japan
    # Country: Japan
    # Capital: Tokyo
    # Population: 125800000
    # Region: Asia
    # Languages: {'jpn': 'Japanese'}
    
    return True

# Main loop
while search_country():
    print()

print("Goodbye!")
