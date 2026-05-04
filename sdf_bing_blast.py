import os
import json
import hashlib
import urllib.request
import re
import random
from datetime import datetime

# ─────────────────────────────────────────────
# 1. UPDATED CONFIG (Verified ID: 2013017799)
# ─────────────────────────────────────────────
AFF_BASE = "https://www.floristone.com/main.cfm?source_id=brightlane&AffiliateID=2013017799"
BASE_URL = "https://brightlane.github.io/SameDayFlowers"
TODAY = datetime.now().strftime("%Y-%m-%d")
YEAR = datetime.now().strftime("%Y")
INDEXNOW_KEY = "3dd8ef03a39841008c6f5fe0c38144d5"

# Seed-based rotation so everyday generates a different city batch
seed_val = int(hashlib.md5(TODAY.encode()).hexdigest()[:8], 16)
random.seed(seed_val)

# ─────────────────────────────────────────────
# 2. CHAMELEON CONTENT LOGIC (Anti-Spam)
# ─────────────────────────────────────────────
def get_variation(options):
    return random.choice(options)

def generate_dynamic_intro(lang, city, occasion):
    if lang == "en":
        v1 = [f"Need to send {occasion} to {city}?", f"Searching for {occasion} in {city}?", f"Best {occasion} delivery in {city}."]
        v2 = ["Floristone offers farm-fresh blooms.", "Our local florists craft stunning arrangements.", "Get premium flowers hand-delivered."]
        return f"{get_variation(v1)} {get_variation(v2)} We guarantee same-day arrival with $0 service fees."
    return "" # Add variations for other langs as needed

# ... [ALL_CITIES and OCCASIONS lists remain as provided] ...

# ─────────────────────────────────────────────
# 3. IMPROVED MULTILINGUAL TEMPLATE
# ─────────────────────────────────────────────
# Note: I've updated the 'note' to include your "Radical Transparency" value
LANGS = {
    "en": {
        "dir": "bing",
        "title": lambda o,c: f"Send {o['en']} to {c} | 2026 Same-Day Delivery",
        "h1": lambda o,c: f"Premium {o['en']} Delivery in {c}",
        "meta": lambda o,c: f"Fast {o['en']} in {c}. Hand-delivered by local shops. No hidden fees. Order by 1PM for same-day arrival.",
        "note": "Radical Transparency: $0 Fees · Free Delivery · 4.8★",
        "back": "← Home",
        "footer": f"© {YEAR} SameDayFlowers · Affiliate: 2013017799",
    },
    # [Other languages continue with similar structure...]
}

# ─────────────────────────────────────────────
# 4. GENERATION ENGINE (Modified for Uniqueness)
# ─────────────────────────────────────────────
# [Logic for city_batch remains, but ensure we use random.sample for diversity]
city_batch = random.sample(ALL_CITIES, 50) 

all_urls = []
total = 0

# BUILD LOOP
for lang_key, lang in LANGS.items():
    folder = lang['dir']
    os.makedirs(folder, exist_ok=True)
    for city in city_batch:
        city_slug = city.lower().replace(" ", "-").replace("'", "")
        for occasion in OCCASIONS:
            slug = f"send-{occasion['slug']}-online-{city_slug}.html"
            
            # UNIQUE CONTENT INJECTION
            intro_text = generate_dynamic_intro(lang_key, city, occasion[lang_key])
            
            # BUILD HTML (Using the build_page function from your original code)
            # Ensure the build_page function uses the new 'intro_text' variable
            
            # [Write to File Logic...]
            all_urls.append(f"{BASE_URL}/{folder}/{slug}")
            total += 1

# ─────────────────────────────────────────────
# 5. INDEXNOW & SITEMAP PING
# ─────────────────────────────────────────────
# [Your existing IndexNow/Sitemap logic is correct, just keep the 10k limit]
