import os
import json
import random
import requests
from datetime import datetime

# --- CONFIGURATION ---
SITE_URL = "https://brightlane.github.io/SameDayFlowers"
INDEXNOW_KEY = "eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ"
KEY_LOCATION = f"{SITE_URL}/{INDEXNOW_KEY}.txt"

def load_cities():
    """Loads cities with strict error handling for 10k scale."""
    if os.path.exists('cities.json'):
        try:
            with open('cities.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                if not data:
                    raise ValueError("cities.json is empty")
                return data
        except json.JSONDecodeError as e:
            print(f"❌ JSON SYNTAX ERROR: {e}")
            print("Check for missing/extra commas around the line mentioned in the error.")
            # Fallback to a small list so the script doesn't crash
            return [{"city": "New York", "state": "NY"}]
    else:
        print("⚠️ cities.json not found.")
        return [{"city": "New York", "state": "NY"}]

def broadcast_to_indexnow(urls):
    endpoint = "https://api.indexnow.org/IndexNow"
    data = {
        "host": "brightlane.github.io",
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls
    }
    try:
        response = requests.post(endpoint, json=data, timeout=10)
        print(f"📡 IndexNow Response: {response.status_code}")
    except Exception as e:
        print(f"❌ Connection Failed: {e}")

def main():
    print(f"🚀 Vulture 10K Blast Engine Initialized")
    
    # 1. LOAD DATA
    ALL_CITIES = load_cities()
    
    # 2. SELECT RANGE (2001-4000)
    # Python slices are 0-indexed: [2000:4000] gives cities 2001 to 4000
    try:
        total = len(ALL_CITIES)
        start, end = 2000, 4000
        
        # Ensure we don't go out of bounds
        segment = ALL_CITIES[start:min(end, total)]
        
        # Sample 100 for Mother's Day Velocity
        city_batch = random.sample(segment, min(len(segment), 100))
        print(f"Processing {len(city_batch)} cities from the 2k-4k block.")
    except Exception as e:
        print(f"Selection Error: {e}")
        city_batch = ALL_CITIES[:10]

    # 3. URL GENERATION
    urls_to_index = []
    for item in city_batch:
        city_slug = item['city'].lower().replace(" ", "-")
        state_slug = item['state'].lower()
        urls_to_index.append(f"{SITE_URL}/blog/flowers-{city_slug}-{state_slug}.html")

    urls_to_index.append(f"{SITE_URL}/index.html")

    # 4. EXECUTE
    if urls_to_index:
        broadcast_to_indexnow(urls_to_index)

if __name__ == "__main__":
    main()
