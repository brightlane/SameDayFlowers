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
    """Loads cities from cities.json or uses a fallback if file missing."""
    if os.path.exists('cities.json'):
        with open('cities.json', 'r') as f:
            return json.load(f)
    else:
        # Emergency Fallback if file isn't found in GitHub Action environment
        print("⚠️ cities.json not found. Using emergency sample list.")
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
        if response.status_code == 200:
            print(f"✅ Vulture Blast Successful: {len(urls)} URLs indexed.")
        else:
            print(f"❌ IndexNow Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Connection Failed: {e}")

def main():
    print(f"🚀 Initializing Vulture 10K Blast: Range 2001-4000")
    
    # 1. LOAD THE DATA
    ALL_CITIES = load_cities()
    
    # 2. SELECT THE RANGE 2001 to 4000
    # Python indexing starts at 0, so 2000:4000 grabs the 2001st through 4000th city
    try:
        city_range = ALL_CITIES[2000:4000]
        
        # We sample 50 daily to maintain "Natural Velocity"
        # but you can increase this to 100+ for the Mother's Day push
        city_batch = random.sample(city_range, 100) 
        print(f"Sampling 100 cities from the 2001-4000 segment.")
    except Exception as e:
        print(f"Range error: {e}. Defaulting to full list shuffle.")
        city_batch = random.sample(ALL_CITIES, 50)

    # 3. URL GENERATION
    urls_to_index = []
    for item in city_batch:
        city_slug = item['city'].lower().replace(" ", "-")
        state_slug = item['state'].lower()
        url = f"{SITE_URL}/blog/flowers-{city_slug}-{state_slug}.html"
        urls_to_index.append(url)

    # Refresh homepage and sitemap authority
    urls_to_index.append(f"{SITE_URL}/index.html")
    urls_to_index.append(f"{SITE_URL}/sitemap.xml")

    # 4. EXECUTE
    if urls_to_index:
        broadcast_to_indexnow(urls_to_index)

if __name__ == "__main__":
    main()
