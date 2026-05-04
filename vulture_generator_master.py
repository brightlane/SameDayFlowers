import os
import json
import datetime

# --- 1. LOAD AFFILIATE CONFIG ---
with open('affiliate.json', 'r') as f:
    config = json.load(f)

BASE_URL = "https://brightlane.github.io/SameDayFlowers"
PROJECT_DIR = "blog"
# Pulling the ManyChat Bridge link from your affiliate.json
MANYCHAT_LINK = config['links']['messenger_bridge']
DEADLINE = config['parameters']['deadline_date']

def generate_page_html(city, state):
    filename = f"flowers-{city.lower().replace(' ', '-')}-{state.lower()}.html"
    page_url = f"{BASE_URL}/{PROJECT_DIR}/{filename}"
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Same Day Mother's Day Flowers {city}, {state} | Fast Delivery</title>
    <meta name="description" content="Send Mother's Day flowers in {city}, {state}. Guaranteed delivery by May 10, 2026. $0 service fees.">
    <link rel="canonical" href="{page_url}">
    <meta name="geo.region" content="US-{state.upper()}">
    <meta name="geo.placename" content="{city}">
    
    <style>
        :root {{ --primary: #ff4d6d; --dark: #1a1a1a; --light: #f9f9f9; }}
        body {{ font-family: -apple-system, sans-serif; margin: 0; color: var(--dark); line-height: 1.6; }}
        .panic-bar {{ background: var(--primary); color: white; text-align: center; padding: 12px; font-weight: bold; position: sticky; top: 0; }}
        nav {{ display: flex; justify-content: space-between; padding: 15px 5%; border-bottom: 1px solid #eee; }}
        .hero {{ background: var(--light); padding: 80px 5%; text-align: center; }}
        .btn {{ background: var(--primary); color: white; padding: 20px 45px; text-decoration: none; border-radius: 50px; font-weight: 800; display: inline-block; font-size: 1.2rem; }}
        footer {{ background: #eee; padding: 40px 5%; text-align: center; font-size: 0.8rem; }}
    </style>
</head>
<body>
    <div class="panic-bar">🌷 MOTHER'S DAY DEADLINE: {DEADLINE} — ORDER FOR {city.upper()}</div>
    <nav><a href="../index.html" style="color:var(--primary); text-decoration:none; font-weight:800;">SameDayFlowers</a></nav>
    <header class="hero">
        <h1>Send Mother's Day Flowers in {city}</h1>
        <p>Hand-delivered by local {city} florists. Guaranteed fresh.</p>
        <!-- NEW AFFILIATE LINK INJECTED HERE -->
        <a href="{MANYCHAT_LINK}" class="btn">VIEW {city.upper()} BOUQUETS</a>
    </header>
    <main style="padding: 40px 5%; max-width: 800px; margin: auto;">
        <h2>Local {city} Delivery Information</h2>
        <p>Order by the deadline for guaranteed same-day delivery in the {city} area. We partner with local florists across {state} to ensure your Mother's Day gift arrives fresh and on time.</p>
    </main>
    <footer>
        <a href="../index.html">Home</a> | <a href="../llms.txt">AI Index</a>
        <p>© 2026 SameDayFlowers · Affiliate: {config['manychat_partner_id']}</p>
    </footer>
</body>
</html>"""
    
    file_path = os.path.join(PROJECT_DIR, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    return filename

if __name__ == "__main__":
    if not os.path.exists(PROJECT_DIR): os.makedirs(PROJECT_DIR)
    with open('cities.json', 'r') as f:
        cities = json.load(f)[0:1000] 

    print(f"🚀 Deploying Pages with Partner ID: {config['manychat_partner_id']}...")
    for c in cities:
        generate_page_html(c['city'], c['state'])
    print("✅ All pages updated with ManyChat Affiliate Bridge.")
