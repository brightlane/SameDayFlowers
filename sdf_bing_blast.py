import sys
import subprocess
import os
import json
import random
from datetime import datetime

# --- SELF-HEALING DEPENDENCY CHECK ---
try:
    import requests
except ImportError:
    print("⚠️ Requests missing. Self-installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

# --- CONFIGURATION ---
SITE_URL = "https://brightlane.github.io/SameDayFlowers"
INDEXNOW_KEY = "eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ"
KEY_LOCATION = f"{SITE_URL}/{INDEXNOW_KEY}.txt"

def load_cities():
    """Loads the city database with error handling."""
    if os.path.exists('cities.json'):
        try:
            with open('cities.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ JSON Load Error: {e}")
            return []
    print("⚠️ cities.json not found.")
    return []

def broadcast_to_indexnow(urls):
    """Sends URLs to the IndexNow API."""
    endpoint = "https://api.indexnow.org/IndexNow"
    data = {
        "host": "brightlane.github.io",
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls
    }
    try:
        response = requests.post(endpoint, json=data, timeout=15)
        print(f"📡 IndexNow Pulse: {response.status_code}")
    except Exception as e:
        print(f"❌ API Connection Failed: {e}")

def main():
    print(f"🚀 Vulture Engine: Targeting Mother's Day May 10, 2026")
    
    ALL_CITIES = load_cities()
    if not ALL_CITIES:
        print("No cities to process. Exiting.")
        return

    # TARGETING RANGE 2001-4000
    try:
        start, end = 2000, 4000 # Slice for city 2001 to 4000
        segment = ALL_CITIES[start:min(end, len(ALL_CITIES))]
        
        # Velocity Control: 100 cities per daily blast
        city_batch = random.sample(segment, min(len(segment), 100))
        print(f"Selected {len(city_batch)} cities from the 2k-4k range.")
    except Exception as e:
        print(f"Sampling Error: {e}")
        city_batch = ALL_CITIES[:50]

    # GENERATE URLs
    urls_to_index = []
    for item in city_batch:
        city_slug = item['city'].lower().replace(" ", "-")
        state_slug = item['state'].lower()
        urls_to_index.append(f"{SITE_URL}/blog/flowers-{city_slug}-{state_slug}.html")

    # Add homepage and AI discovery files
    urls_to_index.append(f"{SITE_URL}/index.html")
    urls_to_index.append(f"{SITE_URL}/sitemap.xml")

    if urls_to_index:
        broadcast_to_indexnow(urls_to_index)

if __name__ == "__main__":
    main()
