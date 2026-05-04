import os
import random
import datetime
import urllib.request
import json

# --- CONFIGURATION (UPDATE BASE_URL FOR REPO 2) ---
BASE_URL = "https://brightlane.github.io/SameDayFlowers-Retail"
PROJECT_DIR = "shop"
INDEX_NOW_KEY = "fd610116b1404d65a8250c0b5cc86a23" 
AFFILIATE_ID = "2013017799" 
MANYCHAT_LINK = f"https://m.me/brightlane?ref={AFFILIATE_ID}"

# --- THE VULTURE 100: RETAIL-FOCUSED STRINGS ---
ACTIONS = ["Send", "Buy", "Order", "Deliver", "Get", "Ship"]
SUBJECTS = ["Luxury Bouquets", "Premium Roses", "Mother's Day Flowers", "Spring Tulips", "Designer Arrangements"]
URGENCY = ["Express", "Same-Day", "Today", "Now", "Guaranteed"]

HOOKS = [f"{a} {s} in {{city}} - {{urgency}}" for a in ACTIONS for s in SUBJECTS for u in URGENCY]

def generate_page_html(city, state):
    title_hook = random.choice(HOOKS).format(city=city, urgency=random.choice(URGENCY))
    filename = f"delivery-{city.lower().replace(' ', '-')}-{state.lower()}.html"
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title_hook} | {city} Florist</title>
    <style>
        body {{ font-family: 'Helvetica Neue', Arial, sans-serif; background: #fff5f7; color: #4a4a4a; padding: 2rem; }}
        .retail-card {{ max-width: 600px; margin: auto; background: #ffffff; border: 1px solid #ffccd5; padding: 40px; text-align: center; box-shadow: 0 4px 15px rgba(255,182,193,0.3); border-radius: 8px; }}
        .shipping-banner {{ background: #ff4d6d; color: #fff; padding: 10px; font-size: 0.8rem; font-weight: bold; letter-spacing: 1px; border-radius: 4px 4px 0 0; }}
        h1 {{ color: #c9184a; margin: 25px 0; font-size: 2.2rem; }}
        .price-hero {{ font-size: 2.8rem; color: #ff4d6d; margin: 15px 0; font-weight: bold; }}
        .cta {{ display: block; background: #ff4d6d; color: #ffffff; padding: 22px; text-decoration: none; font-weight: bold; border-radius: 4px; font-size: 1.5rem; }}
        .urgency-text {{ color: #590d22; font-size: 0.9rem; margin-top: 20px; border-top: 1px solid #ffccd5; padding-top: 15px; font-style: italic; }}
    </style>
</head>
<body>
    <div class="retail-card">
        <div class="shipping-banner">FREE DELIVERY CONFIRMED FOR {city.upper()}</div>
        <h1>{title_hook}</h1>
        <p>Hand-crafted for Mother's Day 2026</p>
        <div class="price-hero">$34.99</div>
        <a href="{MANYCHAT_LINK}" class="cta">SEND TO {city.upper()} NOW</a>
        <div class="urgency-text">
            <strong>NOTICE:</strong> Local {city} floral artisans are at 89% capacity. Order in 01:52:10 to secure {random.choice(URGENCY)} arrival.
        </div>
    </div>
</body>
</html>"""
    
    with open(f"{PROJECT_DIR}/{filename}", "w", encoding="utf-8") as f:
        f.write(html_content)
    return filename

def update_sitemap():
    today = datetime.date.today().isoformat()
    all_files = [f for f in os.listdir(PROJECT_DIR) if f.endswith('.html')]
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for name in all_files:
            f.write(f'  <url><loc>{BASE_URL}/{PROJECT_DIR}/{name}</loc><lastmod>{today}</lastmod></url>\n')
        f.write('</urlset>')

def ping_index_now(filenames):
    url_list = [f"{BASE_URL}/{PROJECT_DIR}/{f}" for f in filenames]
    data = {"host": BASE_URL.replace("https://", ""), "key": INDEX_NOW_KEY, "urlList": url_list}
    req = urllib.request.Request("https://www.bing.com/indexnow", data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200: print("✅ IndexNow Success.")
    except: print("❌ IndexNow Failed.")

if __name__ == "__main__":
    if not os.path.exists(PROJECT_DIR): os.makedirs(PROJECT_DIR)
    
    # Targeting the NEXT Vulture Block: 4001-6000
    with open('cities.json', 'r') as f:
        cities = json.load(f)[4000:6000]

    print(f"🚀 Deploying Block 4001-6000 (Retail UI)...")
    new_files = [generate_page_html(c['city'], c['state']) for c in cities]
    
    update_sitemap()
    ping_index_now(new_files)
