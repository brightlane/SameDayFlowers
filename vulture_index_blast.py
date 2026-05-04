import requests
import json
import os

def trigger_index_blast():
    """
    Vulture 10K Protocol: IndexNow Instant Notification
    Notifies Search Engines that the Trillion-Scale Map has been updated.
    """
    
    # 1. Configuration
    BASE_URL = "https://brightlane.github.io/SameDayFlowers"
    SITEMAP_URL = f"{BASE_URL}/sitemap.xml"
    
    # IndexNow Endpoints
    ENDPOINTS = [
        "https://www.bing.com/indexnow",
        "https://yandex.com/indexnow",
        "https://api.indexnow.org" # Shared endpoint for DuckDuckGo/Others
    ]
    
    # This key should be a text file in your root (e.g., your-key.txt)
    # For now, we use a placeholder or your specific IndexNow Key
    INDEX_NOW_KEY = "fd610116b1404d65a8250c0b5cc86a23" 
    
    payload = {
        "host": "brightlane.github.io",
        "key": INDEX_NOW_KEY,
        "keyLocation": f"{BASE_URL}/{INDEX_NOW_KEY}.txt",
        "urlList": [SITEMAP_URL],
        "deleteAll": False
    }

    print(f"🚀 Vulture Indexing Blast Initialized...")
    
    # 2. Execution
    success_count = 0
    for url in ENDPOINTS:
        try:
            response = requests.post(url, json=payload, timeout=10)
            if response.status_code == 200:
                print(f"✅ Success: {url}")
                success_count += 1
            else:
                print(f"⚠️ Failed: {url} (Status: {response.status_code})")
        except Exception as e:
            print(f"❌ Connection Error: {url} - {str(e)}")

    print(f"--- BLAST REPORT ---")
    print(f"● Target: {SITEMAP_URL}")
    print(f"● Successful Pings: {success_count}/{len(ENDPOINTS)}")
    print(f"--------------------")

if __name__ == "__main__":
    trigger_index_blast()
