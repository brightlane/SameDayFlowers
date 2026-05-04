import os
import random
import datetime
import urllib.request
import json

# --- CONFIGURATION ---
BASE_URL = "https://brightlane.github.io/SameDayFlowers-Retail"
PROJECT_DIR = "shop"
INDEX_NOW_KEY = "fd610116b1404d65a8250c0b5cc86a23"
AFFILIATE_ID = "2013017799"
MANYCHAT_LINK = f"https://m.me/brightlane?ref={AFFILIATE_ID}"

# --- RETAIL HOOK SYSTEM (FIXED) ---
ACTIONS = ["Send", "Buy", "Order", "Deliver", "Get", "Ship"]
SUBJECTS = [
    "Luxury Bouquets",
    "Premium Roses",
    "Mother's Day Flowers",
    "Spring Tulips",
    "Designer Arrangements"
]
URGENCY = ["Express", "Same-Day", "Today", "Now", "Guaranteed"]

def generate_hook(city):
    a = random.choice(ACTIONS)
    s = random.choice(SUBJECTS)
    u = random.choice(URGENCY)
    return f"{a} {s} in {city} - {u}"

# --- PAGE GENERATION ---
def generate_page_html(city, state):
    title_hook = generate_hook(city)
    filename = f"delivery-{city.lower().replace(' ', '-')}-{state.lower()}.html"

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_hook} | {city} Florist</title>

<style>
body {{
    font-family: Arial, sans-serif;
    background: #fff5f7;
    color: #4a4a4a;
    padding: 2rem;
}}
.card {{
    max-width: 600px;
    margin: auto;
    background: #fff;
    border: 1px solid #ffccd5;
    padding: 40px;
    text-align: center;
    border-radius: 10px;
}}
.banner {{
    background: #ff4d6d;
    color: white;
    padding: 10px;
    font-weight: bold;
}}
h1 {{
    color: #c9184a;
}}
.price {{
    font-size: 2.5rem;
    color: #ff4d6d;
    font-weight: bold;
}}
.cta {{
    display: block;
    background: #ff4d6d;
    color: white;
    padding: 20px;
    text-decoration: none;
    font-weight: bold;
    margin-top: 20px;
    border-radius: 6px;
}}
</style>
</head>

<body>
<div class="card">
    <div class="banner">FREE DELIVERY AVAILABLE IN {city.upper()}</div>

    <h1>{title_hook}</h1>
    <p>Mother's Day 2026 Premium Floral Collection</p>

    <div class="price">$34.99</div>

    <a href="{MANYCHAT_LINK}" class="cta">
        ORDER FOR {city.upper()}
    </a>

    <p style="margin-top:20px;font-size:0.85rem;">
        Affiliate ID: {AFFILIATE_ID}
    </p>
</div>
</body>
</html>"""

    path = os.path.join(PROJECT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html_content)

    return filename

# --- SITEMAP ---
def update_sitemap(files):
    today = datetime.date.today().isoformat()

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for f in files:
        xml += f"  <url><loc>{BASE_URL}/{PROJECT_DIR}/{f}</loc><lastmod>{today}</lastmod></url>\n"

    xml += '</urlset>'

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml)

# --- INDEXNOW ---
def ping_index_now(files):
    url_list = [f"{BASE_URL}/{PROJECT_DIR}/{f}" for f in files]

    data = {
        "host": BASE_URL.replace("https://", ""),
        "key": INDEX_NOW_KEY,
        "urlList": url_list
    }

    req = urllib.request.Request(
        "https://www.bing.com/indexnow",
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req) as r:
            print("✅ IndexNow success")
    except Exception as e:
        print("❌ IndexNow failed:", e)

# --- MAIN ---
if __name__ == "__main__":

    os.makedirs(PROJECT_DIR, exist_ok=True)

    with open("cities.json", "r", encoding="utf-8") as f:
        cities = json.load(f)

    # SAFE RANGE HANDLING
    block = cities[4000:6000] if len(cities) > 4000 else cities

    print(f"🚀 Generating {len(block)} retail pages...")

    generated = []
    for c in block:
        if "city" in c and "state" in c:
            generated.append(generate_page_html(c["city"], c["state"]))

    update_sitemap(generated)
    ping_index_now(generated)

    print("✅ DONE: Retail network deployed successfully")
