import os
import json
import requests
from datetime import date

# ================= CONFIG =================
SITE_URL = "https://brightlane.github.io/SameDayFlowers"
INDEXNOW_KEY = "fd610116b1404d65a8250c0b5cc86a23"
KEY_LOCATION = f"{SITE_URL}/{INDEXNOW_KEY}.txt"

BING_ENDPOINT = "https://www.bing.com/indexnow"

# folders where your 5,000 pages live
FOLDERS = ["blog", "shop", "guide", "dispatch", "now", "trending"]

BATCH_SIZE = 100  # safe limit per request

# =========================================

def collect_urls():
    urls = []

    for folder in FOLDERS:
        if not os.path.exists(folder):
            continue

        for f in os.listdir(folder):
            if f.endswith(".html"):
                urls.append(f"{SITE_URL}/{folder}/{f}")

    return urls


def chunk_list(data, size):
    for i in range(0, len(data), size):
        yield data[i:i + size]


def send_batch(urls):
    payload = {
        "host": "brightlane.github.io",
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls
    }

    try:
        r = requests.post(BING_ENDPOINT, json=payload, timeout=10)
        return r.status_code, r.text
    except Exception as e:
        return None, str(e)


def main():
    urls = collect_urls()

    print(f"🚀 Found {len(urls)} pages to submit")

    if not urls:
        print("❌ No pages found")
        return

    batches = list(chunk_list(urls, BATCH_SIZE))

    success = 0
    failed = 0

    for i, batch in enumerate(batches):
        status, resp = send_batch(batch)

        if status == 200:
            success += len(batch)
            print(f"✅ Batch {i+1}/{len(batches)} OK ({len(batch)} URLs)")
        else:
            failed += len(batch)
            print(f"❌ Batch {i+1} FAILED: {resp}")

    print("\n📊 INDEXNOW REPORT")
    print("-------------------")
    print("Total URLs:", len(urls))
    print("Success:", success)
    print("Failed:", failed)


if __name__ == "__main__":
    main()
