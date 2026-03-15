"""
Week 4 Homework - Level 1: Not Yet
Simple API Request
"""

import requests

# JSONPlaceholder API - free, no key needed
url = "https://jsonplaceholder.typicode.com/posts/1"

# ============================================
# YOUR CODE:
# ============================================
# 1. Make a GET request
response = requests.get(url)

# 2. Check if successful (status code 200)
if response.status_code == 200:
    # 3. Convert to JSON (dictionary)
    data = response.json()
    
    # 4. Print the title and body
    print("Title:", data['title'])
    print("Body:", data['body'])
else:
    print("Error: Status code", response.status_code)
