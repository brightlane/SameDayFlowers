import os
import random
import datetime
import urllib.request
import json

# --- CONFIGURATION (UPDATE BASE_URL FOR REPO 4) ---
BASE_URL = "https://brightlane.github.io/Flower-Dispatch-Network"
PROJECT_DIR = "dispatch"
INDEX_NOW_KEY = "fd610116b1404d65a8250c0b5cc86a23" 
AFFILIATE_ID = "2013017799" 
MANYCHAT_LINK = f"https://m.me/brightlane?ref={AFFILIATE_ID}"

# --- THE VULTURE 100: LOGISTICS & DISPATCH STRINGS ---
ACTIONS = ["Dispatch", "Track", "Locate", "Send", "Rush", "Express"]
SUBJECTS = ["Flower Courier", "Local Delivery", "Mother's Day Flowers", "Floral Dispatch", "Gift Delivery"]
URGENCY = ["Priority", "ASAP", "Immediate", "Scheduled", "Confirmed"]

HOOKS = [f"{a} {s} in {{city}} - {u}" for a in ACTIONS for s in SUBJECTS for u in URGENCY]

def generate_page_html(city, state):
    title_hook = random.choice(HOOKS).format(city=city)
    filename = f"dispatch-{city.lower().replace(' ', '-')}-{state.lower()}.html"
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title_hook} | Dispatch Center</title>
    <style>
        body {{ font-family: "Courier New", Courier, monospace; background: #e9ecef; color: #2b2d42; padding: 1rem; }}
        .dispatch-card {{ max-width: 650px; margin: auto; background: #fff; border: 2px solid #2b2d42; padding: 0; box-shadow: 10px 10px 0px #8d99ae; }}
        .header {{ background: #2b2d42; color: #edf2f4; padding: 10px; font-weight: bold; text-transform: uppercase; }}
        .body-content {{ padding: 30px; }}
        .status-line {{ border-bottom: 1px dashed #8d99ae; margin-bottom: 15px; padding-bottom: 5px; display: flex; justify-content: space-between; }}
        .active {{ color: #d90429; font-weight: bold; }}
        h1 {{ font-size: 1.5rem; text-transform: uppercase; margin: 20px 0; }}
        .cta-dispatch {{ display: block; background: #d90429; color: #fff; text-align: center; padding: 20px; text-decoration: none; font-weight: bold; font-size: 1.2rem; border: 2px solid #2b2d42; }}
        .cta-dispatch:hover {{ background: #2b2d42; color: #fff; }}
        .barcode {{ font-family: sans-serif; font-size: 0.7rem; letter-spacing: 5px; margin-top: 20px; opacity: 0.5; }}
    </style>
</head>
<body>
    <div class="dispatch-card">
        <div class="header">System Status: Priority Dispatch Active</div>
        <div class="body-content">
            <div class="status-line"><span>REGION:</span> <span>{city.upper()}, {state.upper()}</span></div>
            <div class="status-line"><span>NETWORK:</span> <span class="active">LOCAL COURIER ONLINE</span></div>
            <div class="status-line"><span>AVAILABILITY:</span> <span>SAME-DAY SLOTS REMAINING</span></div>
            
            <h1>{title_hook}</h1>
            <p>Direct floral dispatch available for Mother's Day 2026. Routing order to the nearest verified {city} florist for immediate fulfillment.</p>

            <a href="{MANYCHAT_LINK}" class="cta-dispatch">INITIALIZE {city.upper()} DISPATCH</a>
            
            <div class="barcode">|||| || ||||| ||| || |||| ||| ||||</div>
            <p style="font-size: 0.6rem; margin-top: 10px;">Vulture Logistics Engine v3.0 | Affiliate Disclosure: Commission may be earned on orders.</p>
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
    
    # Final Vulture Block: 8001-10000
    with open('cities.json', 'r') as f:
        cities = json.load(f)[8000:10000]

    print(f"🚀 Deploying Block 8001-10000 (Dispatch UI)...")
    new_files = [generate_page_html(c['city'], c['state']) for c in cities]
    update_sitemap()
