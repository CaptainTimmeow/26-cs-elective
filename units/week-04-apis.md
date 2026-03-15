# Week 4: APIs and HTTP Requests

## Objective

Students will understand how web APIs work and use Python's `requests` library to fetch and display data from real APIs.

## Standards

- Understand HTTP methods (GET, POST)
- Use requests library to make API calls
- Parse JSON responses
- Handle API errors gracefully
- Display API data in meaningful ways

---

## Lesson Plan (90 min)

### 1. Hook (10 min)

**Demo:** Show a weather app or stock ticker
"How does this app know it's 22°C in Shanghai right now? It's not magic - it's APIs!"

**Ask:** "What other apps get data from the internet?"

---

### 2. Direct Instruction (25 min)

**Topic 1: What is an API? (5 min)**
- API = Application Programming Interface
- Like a restaurant menu - you ask, you get something back
- HTTP methods: GET (ask for data), POST (send data)
- JSON format - Python dictionaries' cousin

**Topic 2: The requests Library (5 min)**
```python
import requests

response = requests.get("https://api.example.com/data")
print(response.status_code)  # 200 = success!
data = response.json()  # Convert to Python
```

**Topic 3: JSON Basics (5 min)**
- JSON looks like Python dicts/lists
- Accessing nested data: `data["results"][0]["name"]`
- Common API response patterns

**Topic 4: Real API Examples (5 min)**
- OpenWeatherMap (weather)
- JSONPlaceholder (fake data for testing)
- REST Countries (country info)
- CoinGecko (crypto prices)

**Topic 5: Error Handling (5 min)**
- Check status codes
- Try/except for network errors
- API rate limits

---

### 3. Guided Practice (25 min)

**Activity: API Explorer**

Use JSONPlaceholder (free, no API key needed):

```python
import requests

# Task 1: Get all posts
response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(f"Status: {response.status_code}")
posts = response.json()
print(f"Got {len(posts)} posts")

# Task 2: Get post #1
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
post = response.json()
print(f"Title: {post['title']}")

# Task 3: Get comments for post #1
response = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
comments = response.json()
for c in comments:
    print(f"- {c['email']}: {c['body'][:50]}...")
```

---

### 4. Independent Practice (25 min)

**Challenge: Country Info Finder**

Build a country lookup tool:

```python
# Use: https://restcountries.com/v3.1/name/{name}

# Features:
# 1. Ask user for country name
# 2. Fetch country data from API
# 3. Display: Capital, Population, Region, Languages
# 4. Handle "country not found" error
# 5. Allow multiple searches

# Example output:
# Enter country: Japan
# Capital: Tokyo
# Population: 125,800,000
# Region: Asia
# Languages: Japanese
```

**Extension:** Add flag display, currency info, or borders

---

### 5. Wrap-up (5 min)

**Exit Ticket:**
1. What does `requests.get()` return?
2. How do you convert JSON to a Python dictionary?
3. Why do we need error handling with APIs?

**Preview:** "Next week we'll build GUIs - graphical interfaces where users can click buttons!"

---

## Materials

- API Cheat Sheet: [[API-Cheat-Sheet]]
- Starter code: [[Week4-API-Starter]]
- Video: [Bro Code - Requests](https://youtube.com/JVQNywo4AbU)

---

## Differentiation

**Advanced:** Use a weather API with API key, parse nested JSON

**Support:** Provide pre-fetched data, focus on parsing

---

## Assessment

- Working API call
- Proper error handling
- Clean output display
