import os
import random
import datetime
import urllib.request
import json

# --- CONFIGURATION (UPDATE BASE_URL FOR REPO 5) ---
BASE_URL = "https://brightlane.github.io/Flowers-Now-Mobile"
PROJECT_DIR = "app"
INDEX_NOW_KEY = "fd610116b1404d65a8250c0b5cc86a23" 
AFFILIATE_ID = "2013017799" 
MANYCHAT_LINK = f"https://m.me/brightlane?ref={AFFILIATE_ID}"

# --- THE VULTURE 100: MOBILE & "NEAR ME" INTENT ---
ACTIONS = ["Send", "Order", "Find", "Get", "Buy"]
SUBJECTS = ["Flowers Near Me", "Same Day Bouquet", "Local Delivery", "Mother's Day Flowers", "Flower Shop"]
URGENCY = ["Open Now", "Delivering Today", "Instant", "Verified", "Fast"]

HOOKS = [f"{s} in {{city}} - {u}" for a in ACTIONS for s in SUBJECTS for u in URGENCY]

def generate_page_html(city, state):
    title_hook = random.choice(HOOKS).format(city=city)
    filename = f"now-{city.lower().replace(' ', '-')}-{state.lower()}.html"
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>{title_hook}</title>
    <style>
        body {{ font-family: -apple-system, system-ui, sans-serif; background: #ffffff; color: #1a1a1a; margin: 0; padding: 0; }}
        .app-container {{ padding: 20px; text-align: center; }}
        .nav-header {{ background: #fdf2f8; padding: 15px; border-bottom: 1px solid #fce7f3; display: flex; align-items: center; justify-content: center; }}
        .dot {{ height: 8px; width: 8px; background-color: #ec4899; border-radius: 50%; display: inline-block; margin-right: 8px; animation: blink 1s infinite; }}
        @keyframes blink {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.3; }} 100% {{ opacity: 1; }} }}
        h1 {{ font-size: 1.5rem; margin: 25px 0 10px 0; color: #831843; }}
        .meta-info {{ font-size: 0.9rem; color: #6b7280; margin-bottom: 30px; }}
        .action-card {{ background: #fff1f2; border: 1.5px solid #fb7185; border-radius: 16px; padding: 25px; margin-bottom: 20px; }}
        .cta-btn {{ display: block; background: #e11d48; color: #fff; text-align: center; padding: 20px; text-decoration: none; font-weight: bold; border-radius: 50px; font-size: 1.2rem; box-shadow: 0 4px 6px -1px rgba(225, 29, 72, 0.4); }}
        .footer-note {{ font-size: 0.7rem; color: #9ca3af; margin-top: 40px; padding: 20px; border-top: 1px solid #f3f4f6; }}
    </style>
</head>
<body>
    <div class="nav-header">
        <span class="dot"></span> <span style="font-size: 0.75rem; font-weight: bold; color: #be185d;">LIVE DELIVERY UPDATES: {city.upper()}</span>
    </div>
    <div class="app-container">
        <h1>{title_hook}</h1>
        <p class="meta-info">Top local floral couriers in {city} are currently accepting same-day orders.</p>
        
        <div class="action-card">
            <div style="font-size: 0.8rem; color: #e11d48; font-weight: bold; margin-bottom: 10px;">AVAILABLE FOR {city.upper()} TODAY</div>
            <div style="font-size: 2rem; font-weight: bold; margin-bottom: 15px;">$39.00+</div>
            <a href="{MANYCHAT_LINK}" class="cta-btn">ORDER ON MESSENGER</a>
        </div>

        <p style="font-size: 0.8rem;">Tap above to check real-time stock and secure your delivery slot for {city}.</p>
        
        <div class="footer-note">
            This "Near Me" guide is an affiliate-supported service. We help you find local florists in {city} and may receive a commission on successful orders.
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

if __name__ == "__main__":
    if not os.path.exists(PROJECT_DIR): os.makedirs(PROJECT_DIR)
    
    # Global Catch-All Block: Top 2,000 cities again (or a new random mix)
    with open('cities.json', 'r') as f:
        cities = json.load(f)[0:2000]

    print(f"🚀 Deploying Block 1-2000 (Mobile-First UI)...")
    new_files = [generate_page_html(c['city'], c['state']) for c in cities]
    update_sitemap()
