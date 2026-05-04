import osimport os
import random
import datetime
import urllib.request
import json

# =========================
# CONFIG
# =========================
BASE_URL = "https://brightlane.github.io/Mothers-Day-Social-Feed"
PROJECT_DIR = "trending"
SITEMAP_FILE = "sitemap.xml"

INDEX_NOW_KEY = "fd610116b1404d65a8250c0b5cc86a23"
AFFILIATE_ID = "2013017799"
MANYCHAT_LINK = f"https://m.me/brightlane?ref={AFFILIATE_ID}"

# =========================
# SAFE INIT
# =========================
os.makedirs(PROJECT_DIR, exist_ok=True)

# =========================
# VIRAL TEMPLATES
# =========================
ACTIONS = ["Trending", "Viral", "Most Gifted", "Top Rated", "Influencer Choice"]
SUBJECTS = ["Flower Bouquets", "Rose Arrangements", "Peony Boxes", "Floral Gifts", "Mom's Favorite"]
URGENCY = ["For 2026", "This Week", "Right Now", "Selling Fast", "Limited Edition"]

HOOKS = [
    f"{a} {s} in {{city}} - {u}"
    for a in ACTIONS
    for s in SUBJECTS
    for u in URGENCY
]

# =========================
# PAGE GENERATOR
# =========================
def generate_page_html(city, state):

    hook = random.choice(HOOKS).format(city=city)

    filename = f"trending-{city.lower().replace(' ', '-')}-{state.lower()}.html"
    url = f"{BASE_URL}/{PROJECT_DIR}/{filename}"

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{hook}</title>

<style>
body {{ font-family: sans-serif; background:#fafafa; padding:10px; }}
.card {{ max-width:500px; margin:auto; background:#fff; border:1px solid #ddd; border-radius:8px; }}
.header {{ padding:10px; font-weight:bold; }}
.img {{ height:300px; background:#eee; display:flex; align-items:center; justify-content:center; }}
.cta {{ display:block; padding:12px; background:#0095f6; color:#fff; text-align:center; text-decoration:none; }}
</style>

</head>
<body>

<div class="card">
    <div class="header">{city} Floral Trends</div>
    <div class="img">MOTHER'S DAY FLOWERS {city.upper()}</div>
    <div style="padding:10px;">
        <p>{hook}</p>
        <a class="cta" href="{MANYCHAT_LINK}">Order in {city}</a>
    </div>
</div>

</body>
</html>"""

    with open(os.path.join(PROJECT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(html)

    return url, filename

# =========================
# SITEMAP GENERATOR
# =========================
def update_sitemap(urls):
    today = datetime.date.today().isoformat()

    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

        for url in urls:
            f.write("  <url>\n")
            f.write(f"    <loc>{url[0]}</loc>\n")
            f.write(f"    <lastmod>{today}</lastmod>\n")
            f.write("  </url>\n")

        f.write("</urlset>")

# =========================
# INDEXNOW PING
# =========================
def ping_index_now(urls):
    try:
        data = {
            "host": BASE_URL.replace("https://", ""),
            "key": INDEX_NOW_KEY,
            "urlList": [u[0] for u in urls]
        }

        req = urllib.request.Request(
            "https://www.bing.com/indexnow",
            data=json.dumps(data).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )

        urllib.request.urlopen(req)
        print("✅ IndexNow ping sent")

    except Exception as e:
        print("⚠️ IndexNow failed:", e)

# =========================
# MAIN EXECUTION
# =========================
if __name__ == "__main__":

    if not os.path.exists("cities.json"):
        print("❌ cities.json missing")
        exit()

    with open("cities.json", "r", encoding="utf-8") as f:
        cities = json.load(f)

    # SAFE LIMIT (no crash if small dataset)
    cities = cities[:2000] if len(cities) > 2000 else cities

    print(f"🚀 Generating {len(cities)} social pages...")

    generated = []

    for c in cities:
        city = c.get("city", "")
        state = c.get("state", "")

        if not city or not state:
            continue

        result = generate_page_html(city, state)
        generated.append(result)

    update_sitemap(generated)
    ping_index_now(generated)

    print(f"✅ DONE: {len(generated)} pages generated")
import random
import datetime
import urllib.request
import json

# --- CONFIGURATION (UPDATE BASE_URL FOR REPO 6) ---
BASE_URL = "https://brightlane.github.io/Mothers-Day-Social-Feed"
PROJECT_DIR = "trending"
INDEX_NOW_KEY = "fd610116b1404d65a8250c0b5cc86a23" 
AFFILIATE_ID = "2013017799" 
MANYCHAT_LINK = f"https://m.me/brightlane?ref={AFFILIATE_ID}"

# --- THE VULTURE 100: SOCIAL & TRENDING STRINGS ---
ACTIONS = ["Trending", "Viral", "Most Gifted", "Top Rated", "Influencer Choice"]
SUBJECTS = ["Flower Bouquets", "Rose Arrangements", "Peony Boxes", "Floral Gifts", "Mom's Favorite"]
URGENCY = ["For 2026", "This Week", "Right Now", "Selling Fast", "Limited Edition"]

HOOKS = [f"{a} {s} in {{city}} - {u}" for a in ACTIONS for s in SUBJECTS for u in URGENCY]

def generate_page_html(city, state):
    title_hook = random.choice(HOOKS).format(city=city)
    filename = f"trending-{city.lower().replace(' ', '-')}-{state.lower()}.html"
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title_hook} | 2026 Trends</title>
    <style>
        body {{ font-family: -apple-system, sans-serif; background: #fafafa; color: #262626; padding: 10px; }}
        .social-container {{ max-width: 500px; margin: auto; background: #fff; border: 1px solid #dbdbdb; border-radius: 3px; }}
        .header {{ padding: 15px; font-weight: bold; border-bottom: 1px solid #efefef; display: flex; align-items: center; }}
        .avatar {{ width: 30px; height: 30px; background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); border-radius: 50%; margin-right: 10px; }}
        .image-placeholder {{ width: 100%; aspect-ratio: 1/1; background: #efefef; display: flex; align-items: center; justify-content: center; color: #8e8e8e; font-size: 0.8rem; font-weight: bold; }}
        .interaction-bar {{ padding: 15px; font-size: 1.2rem; }}
        .content {{ padding: 0 15px 20px 15px; }}
        .likes {{ font-weight: bold; font-size: 0.9rem; margin-bottom: 8px; }}
        h1 {{ font-size: 0.95rem; margin: 0; display: inline; }}
        .cta-social {{ display: block; background: #0095f6; color: #fff; text-align: center; padding: 12px; text-decoration: none; font-weight: bold; border-radius: 8px; margin-top: 15px; }}
        .footer {{ font-size: 0.7rem; color: #8e8e8e; padding: 20px; text-align: center; }}
    </style>
</head>
<body>
    <div class="social-container">
        <div class="header">
            <div class="avatar"></div>
            <span>{city}_Floral_Trends</span>
        </div>
        <div class="image-placeholder">
            [PHOTO: MOTHER'S DAY FLOWERS {city.upper()}]
        </div>
        <div class="interaction-bar">❤️ 💬 ✈️</div>
        <div class="content">
            <div class="likes">{random.randint(1100, 5000)} likes</div>
            <h1>{city}_Floral_Trends</h1> {title_hook}. This arrangement is taking over {city} this week. Don't be the one who forgets! 🌸✨
            <a href="{MANYCHAT_LINK}" class="cta-social">Order This Look in {city}</a>
        </div>
    </div>
    <div class="footer">
        © 2026 Social Guide • Sponsored Affiliate Content
    </div>
</body>
</html>"""
    
    with open(os.path.join(PROJECT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(html_content)
    return filename

# (Rest of script functions: update_sitemap, ping_index_now, etc. same as Master Engine)

if __name__ == "__main__":
    if not os.path.exists(PROJECT_DIR): os.makedirs(PROJECT_DIR)
    
    with open('cities.json', 'r') as f:
        cities = json.load(f)[0:2000] # Repurposing top 2k for viral exposure

    print(f"🚀 Deploying Block 0-2000 (Social UI)...")
    new_files = [generate_page_html(c['city'], c['state']) for c in cities]
    # (Call update_sitemap and ping_index_now here)
