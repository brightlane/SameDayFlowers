import os
import random
import datetime
import urllib.request
import json

# --- CONFIGURATION (UPDATE BASE_URL FOR REPO 3) ---
BASE_URL = "https://brightlane.github.io/Local-Flower-Directory"
PROJECT_DIR = "guide"
INDEX_NOW_KEY = "fd610116b1404d65a8250c0b5cc86a23" 
AFFILIATE_ID = "2013017799" 
MANYCHAT_LINK = f"https://m.me/brightlane?ref={AFFILIATE_ID}"

# --- THE VULTURE 100: DIRECTORY/REVIEW SEARCH STRINGS ---
ACTIONS = ["Best", "Top Rated", "Find", "Compare", "Local", "Reviews for"]
SUBJECTS = ["Flower Delivery", "Florists", "Mother's Day Flowers", "Same Day Service", "Gift Shops"]
URGENCY = ["2026 Guide", "Today", "Now", "Verified", "Ranked"]

HOOKS = [f"{a} {s} in {{city}} - {u}" for a in ACTIONS for s in SUBJECTS for u in URGENCY]

def generate_page_html(city, state):
    title_hook = random.choice(HOOKS).format(city=city)
    filename = f"best-flowers-{city.lower().replace(' ', '-')}-{state.lower()}.html"
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title_hook} | Local Guide</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f8f9fa; color: #212529; padding: 1.5rem; }}
        .directory-box {{ max-width: 700px; margin: auto; background: #ffffff; border: 1px solid #dee2e6; border-radius: 4px; overflow: hidden; }}
        .header-bar {{ background: #004d40; color: #fff; padding: 15px; font-weight: bold; display: flex; justify-content: space-between; }}
        .content-body {{ padding: 30px; }}
        h1 {{ font-size: 1.75rem; color: #004d40; margin-top: 0; }}
        .rating {{ color: #ffc107; font-size: 1.2rem; margin-bottom: 10px; }}
        .feature-list {{ margin: 20px 0; padding: 0; list-style: none; }}
        .feature-list li {{ padding: 8px 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; }}
        .cta-btn {{ display: block; background: #ffc107; color: #000; text-align: center; padding: 18px; text-decoration: none; font-weight: bold; border-radius: 4px; margin-top: 20px; text-transform: uppercase; }}
        .footer {{ font-size: 0.75rem; color: #6c757d; margin-top: 30px; text-align: center; }}
    </style>
</head>
<body>
    <div class="directory-box">
        <div class="header-bar">
            <span>DIRECTORY 2026</span>
            <span>VERIFIED: {city.upper()}</span>
        </div>
        <div class="content-body">
            <div class="rating">★★★★★ 4.9/5 Average Rating</div>
            <h1>{title_hook}</h1>
            <p>We've analyzed local delivery data to find the highest-performing same-day floral services in <strong>{city}, {state}</strong> for Mother's Day.</p>
            
            <ul class="feature-list">
                <li><span>Same-Day Availability</span> <span style="color: green;">✔ High</span></li>
                <li><span>Mother's Day Slots</span> <span style="color: orange;">⚠ Limited</span></li>
                <li><span>Average Delivery Time</span> <span>3.5 Hours</span></li>
            </ul>

            <a href="{MANYCHAT_LINK}" class="cta-btn">View Best Available Florists in {city}</a>
            
            <div class="footer">
                Disclaimer: This directory is supported by affiliate partnerships. When you order via our guide, we may receive compensation.
            </div>
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
    
    # Targeting the THIRD Vulture Block: 6001-8000
    with open('cities.json', 'r') as f:
        cities = json.load(f)[6000:8000]

    print(f"🚀 Deploying Block 6001-8000 (Directory UI)...")
    new_files = [generate_page_html(c['city'], c['state']) for c in cities]
    update_sitemap()
