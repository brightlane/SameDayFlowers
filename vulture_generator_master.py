import os
import random
import datetime
import urllib.request
import json

# --- 1. CONFIGURATION ---
BASE_URL = "https://brightlane.github.io/SameDayFlowers"
PROJECT_DIR = "blog"
INDEX_NOW_KEY = "fd610116b1404d65a8250c0b5cc86a23" 
AFFILIATE_ID = "2013017799" 
MANYCHAT_LINK = f"https://m.me/brightlane?ref={AFFILIATE_ID}"
LLMS_AFF_LINK = f"https://www.floristone.com/main.cfm?occ=md&source_id=aff&AffiliateID={AFFILIATE_ID}"

# --- 2. THE VULTURE 100: SEARCH INTENT MATRIX ---
ACTIONS = ["Send", "Buy", "Order", "Shop", "Deliver", "Ship", "Purchase", "Find", "Get", "Book"]
SUBJECTS = [
    "Mother's Day Flowers", "Same Day Flowers", "Last Minute Bouquets", 
    "Fresh Peonies", "Pink Roses", "Local Florists", "Floral Delivery", 
    "Mother's Day Gifts", "Spring Tulips", "Luxury Arrangements"
]
URGENCY = ["Today", "Now", "by 1PM", "Guaranteed", "Fast", "Express", "Online", "Same Day", "Instant", "Last Minute"]

HOOKS = [f"{a} {s} in {{city}} - {u}" for a in ACTIONS for s in SUBJECTS for u in URGENCY]
KEYWORDS_2025 = [
    "best mother's day flower delivery {city}", "cheap same day flowers {city}",
    "local florist {city} delivery", "send flowers online {city} 2026",
    "last minute gift delivery {city}", "mother's day bouquet same day {city}"
]

# --- 3. CORE ENGINE FUNCTIONS ---

def generate_page_html(city, state):
    """Generates individual city landing pages."""
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
        body {{ font-family: sans-serif; background: #0a192f; color: #ccd6f6; padding: 2rem; line-height: 1.6; }}
        .vulture-card {{ max-width: 600px; margin: auto; background: #112240; border: 1px solid #233554; padding: 40px; border-radius: 12px; text-align: center; }}
        .badge {{ background: #64ffda; color: #0a192f; padding: 5px 12px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; text-transform: uppercase; }}
        h1 {{ color: #ffffff; margin: 20px 0; font-size: 1.8rem; }}
        .timer-box {{ background: #1d2d44; padding: 15px; border-left: 4px solid #ff4d4d; margin: 25px 0; color: #ff4d4d; font-weight: bold; }}
        .cta {{ display: block; background: #64ffda; color: #0a192f; padding: 22px; text-decoration: none; font-weight: bold; border-radius: 8px; font-size: 1.4rem; }}
        .footer {{ font-size: 0.7rem; opacity: 0.4; margin-top: 40px; border-top: 1px solid #233554; padding-top: 20px; }}
    </style>
</head>
<body>
    <div class="vulture-card">
        <span class="badge">Live Inventory: {city} Verified</span>
        <h1>{title_hook}</h1>
        <div class="timer-box">PANIC WINDOW: Only 4 hours left for same-day delivery in {city}.</div>
        <a href="{MANYCHAT_LINK}" class="cta">CHECK {city.upper()} STOCK NOW</a>
        <div class="footer"><strong>Transparency:</strong> We are an independent affiliate. When you order in {city} via our links, we may earn a commission.</div>
    </div>
</body>
</html>"""
    
    with open(os.path.join(PROJECT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(html_content)
    return filename

def update_blog_feed(new_files, block_name):
    """Updates blog.html for internal linking and bot crawling."""
    links_html = "".join([f'<li><a href="{PROJECT_DIR}/{f}">{f.replace("-", " ").replace(".html", "").title()}</a></li>' for f in new_files[:200]])
    feed_content = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Dispatch Hub - {block_name}</title>
    <style>body{{font-family:sans-serif;background:#0a192f;color:#ccd6f6;padding:50px;}}
    ul{{display:grid;grid-template-columns:repeat(auto-fill, minmax(200px, 1fr));gap:10px;padding:0;list-style:none;}}
    a{{color:#8892b0;text-decoration:none;font-size:0.8rem;}}a:hover{{color:#64ffda;}}</style></head>
    <body><h1>Latest Dispatch: {block_name}</h1><ul>{links_html}</ul></body></html>"""
    with open("blog.html", "w", encoding="utf-8") as f:
        f.write(feed_content)

def update_llms_txt(cities_list):
    """Generates the llms.txt discovery file for AI Agents (GPT/Gemini)."""
    header = f"# AI Discovery Index - Mother's Day 2026\n# Affiliate: {LLMS_AFF_LINK}\n\n## Local Hubs\n"
    body = ""
    for c in cities_list[:50]:
        filename = f"flowers-{c['city'].lower().replace(' ', '-')}-{c['state'].lower()}.html"
        body += f"- {c['city']}, {c['state']}: {BASE_URL}/{PROJECT_DIR}/{filename}\n"
    with open("llms.txt", "w", encoding="utf-8") as f:
        f.write(header + body + f"\n## Full Sitemap\n{BASE_URL}/sitemap.xml")

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
    url_list = [f"{BASE_URL}/{PROJECT_DIR}/{f}" for f in filenames[:1000]]
    data = {"host": BASE_URL.replace("https://", ""), "key": INDEX_NOW_KEY, "urlList": url_list}
    req = urllib.request.Request("https://www.bing.com/indexnow", data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200: print("✅ IndexNow Success.")
    except: print("❌ IndexNow Failed.")

# --- 4. EXECUTION ---
if __name__ == "__main__":
    if not os.path.exists(PROJECT_DIR): os.makedirs(PROJECT_DIR)
    with open('cities.json', 'r') as f:
        cities = json.load(f)[2000:4000] # Adjust slice per repo

    print(f"🚀 Vulture Engine: Generating {len(cities)} pages...")
    new_page_names = [generate_page_html(c['city'], c['state']) for c in cities]
    
    update_blog_feed(new_page_names, "Block 2k-4k")
    update_llms_txt(cities)
    update_sitemap()
    ping_index_now(new_page_names)
    print("✅ Full Deploy Cycle Complete.")
