import os
import random
import datetime
import urllib.request
import json

# --- CONFIGURATION ---
BASE_URL = "https://brightlane.github.io/SameDayFlowers"
PROJECT_DIR = "blog"
INDEX_NOW_KEY = "fd610116b1404d65a8250c0b5cc86a23" 
AFFILIATE_ID = "2013017799" 
MANYCHAT_LINK = f"https://m.me/brightlane?ref={AFFILIATE_ID}"
LLMS_AFF_LINK = f"https://www.floristone.com/main.cfm?occ=md&source_id=aff&AffiliateID={AFFILIATE_ID}"

# --- THE VULTURE 100: EXPANDED 2025 SEARCH INTENT ---
ACTIONS = ["Send", "Buy", "Order", "Shop", "Deliver", "Ship", "Purchase", "Find", "Get", "Book"]
SUBJECTS = [
    "Mother's Day Flowers", "Same Day Flowers", "Last Minute Bouquets", 
    "Fresh Peonies", "Pink Roses", "Local Florists", "Floral Delivery", 
    "Mother's Day Gifts", "Spring Tulips", "Luxury Arrangements"
]
URGENCY = [
    "Today", "Now", "by 1PM", "Guaranteed", "Fast", "Express", 
    "Online", "Same Day", "Instant", "Last Minute"
]

# This creates the matrix of 100+ high-velocity hooks
HOOKS = [f"{a} {s} in {{city}} - {u}" for a in ACTIONS for s in SUBJECTS for u in URGENCY]

# Secondary keywords for H2 tags and meta descriptions
KEYWORDS_2025 = [
    "best mother's day flower delivery {city}", "cheap same day flowers {city}",
    "local florist {city} delivery", "send flowers online {city} 2026",
    "last minute gift delivery {city}", "mother's day bouquet same day {city}",
    "order peonies online {city}", "affordable flowers delivered {city}"
]

def generate_page_html(city, state):
    title_hook = random.choice(HOOKS).format(city=city)
    secondary_seo = random.choice(KEYWORDS_2025).format(city=city)
    filename = f"flowers-{city.lower().replace(' ', '-')}-{state.lower()}.html"
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title_hook} | {city}, {state}</title>
    <style>
        body {{ font-family: sans-serif; background: #0a192f; color: #ccd6f6; padding: 2rem; line-height: 1.5; }}
        .vulture-card {{ max-width: 600px; margin: auto; background: #112240; border: 1px solid #233554; padding: 40px; border-radius: 12px; text-align: center; }}
        .badge {{ background: #64ffda; color: #0a192f; padding: 5px 12px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; text-transform: uppercase; }}
        h1 {{ color: #ffffff; margin: 20px 0; font-size: 1.8rem; }}
        h2 {{ color: #8892b0; font-size: 1.1rem; font-weight: normal; margin-bottom: 25px; }}
        .timer-box {{ background: #1d2d44; padding: 15px; border-left: 4px solid #ff4d4d; margin: 25px 0; color: #ff4d4d; font-weight: bold; font-size: 0.9rem; }}
        .cta {{ display: block; background: #64ffda; color: #0a192f; padding: 22px; text-decoration: none; font-weight: bold; border-radius: 6px; font-size: 1.4rem; transition: 0.3s; }}
        .cta:hover {{ background: #ffffff; transform: translateY(-2px); }}
        .footer {{ font-size: 0.7rem; opacity: 0.4; margin-top: 35px; border-top: 1px solid #233554; padding-top: 20px; }}
    </style>
</head>
<body>
    <div class="vulture-card">
        <span class="badge">Live Inventory: {city} Verified</span>
        <h1>{title_hook}</h1>
        <h2>Found: {secondary_seo}</h2>
        
        <div class="timer-box">
            PANIC WINDOW: Only 4 hours left for same-day {city} delivery.
        </div>

        <a href="{MANYCHAT_LINK}" class="cta">CHECK {city.upper()} STOCK NOW</a>
        
        <div class="footer">
            <strong>Radical Transparency:</strong> We are an independent affiliate. When you {random.choice(ACTIONS).lower()} flowers in {city} via our links, we may earn a commission.
        </div>
    </div>
</body>
</html>"""
    
    with open(f"{PROJECT_DIR}/{filename}", "w", encoding="utf-8") as f:
        f.write(html_content)
    return filename

# --- REMAINDER OF SCRIPT (Sitemap, IndexNow, Execution) REMAINS SAME ---
