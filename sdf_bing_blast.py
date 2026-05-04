import sys
import subprocess
import os
import json
import random
from datetime import datetime

try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

# --- CONFIG ---
SITE_URL = "https://brightlane.github.io/SameDayFlowers"
INDEXNOW_KEY = "eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ"
KEY_LOCATION = f"{SITE_URL}/{INDEXNOW_KEY}.txt"

ENDPOINTS = [
    "https://www.bing.com/indexnow"
]

def load_cities():
    if not os.path.exists("cities.json"):
        return []

    with open("cities.json", "r", encoding="utf-8") as f:
        return json.load(f)


def safe_slug(text):
    return (
        text.lower()
        .replace("&", "and")
        .replace("'", "")
        .replace(" ", "-")
    )


def broadcast(urls):
    payload = {
        "host": "brightlane.github.io",
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": list(set(urls))  # dedupe
    }

    for endpoint in ENDPOINTS:
        try:
            r = requests.post(endpoint, json=payload, timeout=15)

            if r.status_code == 200:
                print(f"✅ IndexNow success → {endpoint}")
            else:
                print(f"⚠️ Failed ({r.status_code}) → {endpoint}")
                print(r.text[:200])

        except Exception as e:
            print(f"❌ Error → {endpoint}: {e}")


def main():
    print("🚀 Vulture IndexNow Engine Starting...")

    cities = load_cities()
    if not cities:
        print("❌ No cities found")
        return

    start, end = 2000, 4000
    segment = cities[start:min(end, len(cities))]

    if not segment:
        print("⚠️ Segment empty")
        return

    sample = random.sample(segment, min(100, len(segment)))

    urls = []

    for c in sample:
        if "city" not in c or "state" not in c:
            continue

        city = safe_slug(c["city"])
        state = safe_slug(c["state"])

        url = f"{SITE_URL}/blog/flowers-{city}-{state}.html"
        urls.append(url)

    # Always include core pages
    urls.extend([
        f"{SITE_URL}/",
        f"{SITE_URL}/index.html",
        f"{SITE_URL}/sitemap.xml"
    ])

    print(f"📦 Sending {len(urls)} URLs to IndexNow")

    broadcast(urls)


if __name__ == "__main__":
    main()
