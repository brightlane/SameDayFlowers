import os
import json
import random
import re

# --- CONFIGURATION ---
BASE_URL = "https://brightlane.github.io/FastFlowers"
AFFILIATE_ID = "2013017799"
MANYCHAT_LINK = f"https://m.me/brightlane?ref={AFFILIATE_ID}"

OUTPUT_DIR = "now"

# --- SAFE SLUG ---
def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")

# --- PAGE GENERATOR ---
def generate_mobile_bridge(city, state):
    safe_city = slugify(city)
    filename = f"get-{safe_city}.html"

    viewers = random.randint(45, 120)

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Priority Dispatch: {city}</title>

<style>
body {{
    font-family: -apple-system, sans-serif;
    background: #fff;
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}}
.card {{
    width: 90%;
    text-align: center;
    border: 2px solid #000;
    padding: 30px 15px;
    border-radius: 20px;
}}
.cta {{
    background: #000;
    color: #fff;
    padding: 20px;
    display: block;
    text-decoration: none;
    border-radius: 12px;
    font-weight: bold;
}}
.live {{
    color: red;
    font-weight: bold;
    font-size: 0.8rem;
}}
</style>
</head>

<body>
<div class="card">

<div style="font-weight:bold;">
🟢 LIVE DISPATCH: {city.upper()}
</div>

<h2>Mother's Day Inventory Found</h2>

<p class="live">{viewers} people viewing {city} florists</p>

<a href="{MANYCHAT_LINK}" class="cta">
Claim Delivery Slot
</a>

<p style="font-size:0.7rem;color:#999;margin-top:15px;">
Affiliate ID: {AFFILIATE_ID}
</p>

</div>
</body>
</html>"""

    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    return filename

# --- SITEMAP ---
def generate_sitemap(files):
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for f in files:
        xml += f"  <url><loc>{BASE_URL}/now/{f}</loc></url>\n"

    xml += '</urlset>'

    with open("sitemap.xml", "w") as f:
        f.write(xml)

# --- MAIN ---
if __name__ == "__main__":

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open("cities.json", "r", encoding="utf-8") as f:
        cities = json.load(f)

    seen = set()
    generated = []

    for c in cities[:2000]:
        key = c["city"].lower()

        if key in seen:
            continue

        seen.add(key)

        generated.append(generate_mobile_bridge(c["city"], c["state"]))

    generate_sitemap(generated)

    print(f"🚀 Generated {len(generated)} Mobile Bridge Pages + Sitemap")
