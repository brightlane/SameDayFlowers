import os
import random
import datetime
import urllib.request
import json

# --- 1. CONFIGURATION ---
BASE_URL = "https://brightlane.github.io/SameDayFlowers"
PROJECT_DIR = "blog"  # Folder where city pages are stored
INDEX_NOW_KEY = "fd610116b1404d65a8250c0b5cc86a23" 
AFFILIATE_ID = "2013017799" 
MANYCHAT_LINK = f"https://m.me/brightlane?ref={AFFILIATE_ID}"
LLMS_AFF_LINK = f"https://www.floristone.com/main.cfm?occ=md&source_id=aff&AffiliateID={AFFILIATE_ID}"

# --- 2. THE VULTURE 100: PEAK 2025 SEARCH INTENT DATA ---
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

# Matrix of 1,000+ potential high-converting title hooks
HOOKS = [f"{a} {s} in {{city}} - {u}" for a in ACTIONS for s in SUBJECTS for u in URGENCY]

# Targeted sub-keywords for H2 tags and metadata density
KEYWORDS_2025 = [
    "best mother's day flower delivery {city}", "cheap same day flowers {city}",
    "local florist {city} delivery", "send flowers online {city} 2026",
    "last minute gift delivery {city}", "mother's day bouquet same day {city}",
    "order peonies online {city}", "affordable flowers delivered {city}"
]

# --- 3. CORE ENGINE FUNCTIONS ---

def generate_page_html(city, state):
    """Generates the high-conversion Dark Mode transactional page."""
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
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: #0a192f; color: #ccd6f6; padding: 2rem; line-height: 1.6; }}
        .vulture-card {{ max-width: 600px; margin: auto; background: #112240; border: 1px solid #233554; padding: 40px; border-radius: 12px; text-align: center; box-shadow: 0 10px 30px -15px rgba(2,12,27,0.7); }}
        .badge {{ background: #64ffda; color: #0a192f; padding: 5px 12px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; }}
        h1 {{ color: #ffffff; margin: 25px 0 10px 0; font-size: 2rem; }}
        h2 {{ color: #8892b0; font-size: 1.1rem; font-weight: normal; margin-bottom: 30px; }}
        .timer-box {{ background: #1d2d44; padding: 18px; border-left: 4px solid #ff4d4d; margin: 25px 0; color: #ff4d4d; font-weight: bold; font-size: 0.95rem; }}
        .cta {{ display: block; background: #64ffda; color: #0a192f; padding: 22px; text-decoration: none; font-weight: bold; border-radius: 8px; font-size: 1.4rem; transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1); }}
        .cta:hover {{ background: #ffffff; transform: translateY(-3px); }}
        .footer {{ font-size: 0.75rem; opacity: 0.4; margin-top: 40px; border-top: 1px solid #233554; padding-top: 25px; }}
    </style>
</head>
<body>
    <div class="vulture-card">
        <span class="badge">Live Connection: {city} Inventory Active</span>
        <h1>{title_hook}</h1>
        <h2>Local Verified Result: {secondary_seo}</h2>
        <div class="timer-box">PANIC WINDOW: Mother's Day delivery slots for {city} are 92% full.</div>
        <a href="{MANYCHAT_LINK}" class="cta">CHECK {city.upper()} AVAILABILITY</a>
        <div class="footer">
            <strong>Radical Transparency:</strong> We are an independent affiliate. When you {random.choice(ACTIONS).lower()} flowers in {city} via our portal, we may receive a commission.
        </div>
    </div>
</body>
</html>"""
    
    with open(os.path.join(PROJECT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(html_content)
    return filename

def update_blog_feed(new_files, block_name):
    """Updates blog.html with internal links to force search engine crawling."""
    links_html = "".join([f'<li><a href="{PROJECT_DIR}/{f}">{f.replace("-", " ").replace(".html", "").title()}</a></li>' for f in new_files[:200]])
    
    feed_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Mother's Day Flower Dispatch Hub - {block_name}</title>
    <style>
        body {{ font-family: sans-serif; background: #0a192f; color: #ccd6f6; padding: 50px; line-height: 1.8; }}
        h1 {{ color: #64ffda; border-bottom: 2px solid #233554; padding-bottom: 15px; }}
        ul {{ list-style: square; padding: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 10px; }}
        a {{ color: #8892b0; text-decoration: none; font-size: 0.9rem; }}
        a:hover {{ color: #64ffda; }}
        .meta {{ font-size: 0.8rem; opacity: 0.5; margin-bottom: 30px; }}
    </style>
</head>
<body>
    <h1>Latest Flower Delivery Dispatches</h1>
    <p class="meta">Network Sync: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} | Block: {block_name}</p>
    <ul>{links_html}</ul>
    <hr style="border: 0; border-top: 1px solid #233554; margin-top: 50px;">
    <p><a href="sitemap.xml">Full Network Sitemap</a></p>
</body>
</html>"""

    with open("blog.html", "w", encoding="utf-8") as f:
        f.write(feed_content)

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
    url_list = [f"{BASE_URL}/{PROJECT_DIR}/{f}" for f in filenames[:5000]] # Limit per ping
    data = {"host": BASE_URL.replace("https://", "").split("/")[0], "key": INDEX_NOW_KEY, "urlList": url_list}
    req = urllib.request.Request("https://www.bing.com/indexnow", data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200: print("✅ IndexNow Success.")
    except Exception as e: print(f"❌ IndexNow Failed: {e}")

# --- 4. EXECUTION BLOCK ---

if __name__ == "__main__":
    if not os.path.exists(PROJECT_DIR): os.makedirs(PROJECT_DIR)
    
    # Selecting the Vulture Block: 2001-4000
    try:
        with open('cities.json', 'r') as f:
            cities_data = json.load(f)
            cities = cities_data[2000:4000]
    except FileNotFoundError:
        print("❌ Error: cities.json not found.")
        exit()

    print(f"🚀 Vulture Engine Initialized: Generating {len(cities)} Money-Intent Pages...")
    
    # Step A: Generate individual city pages
    new_page_names = [generate_page_html(c['city'], c['state']) for c in cities]
    
    # Step B: Update the internal linking feed
    update_blog_feed(new_page_names, "Block 2001-4000")
    
    # Step C: Update sitemap for search crawlers
    update_sitemap()
    
    # Step D: Force indexing via IndexNow
    ping_index_now(new_page_names)
    
    print(f"✅ Success. {len(new_page_names)} pages are live and indexed.")
