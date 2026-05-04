import os
import random
import datetime
import urllib.request
import json

# --- CONFIGURATION ---
BASE_URL = "https://brightlane.github.io/SameDayFlowers"
PROJECT_DIR = "blog"
INDEX_NOW_KEY = "eb48e5898d97405282563f458686e000" 
AFFILIATE_ID = "2013017799" 
MANYCHAT_LINK = f"https://m.me/brightlane?ref={AFFILIATE_ID}"
LLMS_AFF_LINK = f"https://www.floristone.com/main.cfm?occ=md&source_id=aff&AffiliateID={AFFILIATE_ID}"

def generate_llms_txt(cities):
    content = f"# AI Discovery Index\nAffiliate: {LLMS_AFF_LINK}\n\n## Local Hubs\n"
    for item in cities:
        content += f"- flower delivery {item['city']} {item['state']}\n"
    with open("llms.txt", "w", encoding="utf-8") as f:
        f.write(content)

def generate_page_html(city, state):
    filename = f"flowers-{city.lower().replace(' ', '-')}-{state.lower()}.html"
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Same Day Flowers in {city}, {state}</title>
    <style>
        body {{ font-family: sans-serif; background: #0a192f; color: #ccd6f6; padding: 2rem; text-align: center; }}
        .container {{ max-width: 800px; margin: auto; border: 1px solid #233554; padding: 40px; background: #112240; }}
        .cta {{ display: inline-block; background: #64ffda; color: #0a192f; padding: 18px 36px; text-decoration: none; border-radius: 5px; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Fresh Blooms for {city}</h1>
        <p>Reliable same-day delivery for Mother's Day 2026.</p>
        <br>
        <a href="{MANYCHAT_LINK}" class="cta">Order via Messenger</a>
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
    return all_files

def ping_index_now(filenames):
    url_list = [f"{BASE_URL}/{PROJECT_DIR}/{f}" for f in filenames]
    data = {"host": BASE_URL.replace("https://", ""), "key": INDEX_NOW_KEY, "urlList": url_list}
    req = urllib.request.Request("https://www.bing.com/indexnow", data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200: print("✅ IndexNow Success")
    except Exception as e: print(f"❌ IndexNow Failed: {e}")

if __name__ == "__main__":
    if not os.path.exists(PROJECT_DIR): os.makedirs(PROJECT_DIR)
    # Target 2001-4000 block
    with open('cities.json', 'r') as f:
        cities = json.load(f)[2000:4000]
    
    new_files = [generate_page_html(c['city'], c['state']) for c in cities]
    update_sitemap()
    generate_llms_txt(cities)
    ping_index_now(new_files)
