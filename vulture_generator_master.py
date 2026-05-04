import math
import os
import json
import shutil
from datetime import datetime
from urllib.parse import quote

# =========================
# LOAD CONFIG SAFELY
# =========================
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# =========================
# SAFE LINK LOADING (FIXED)
# =========================
MANYCHAT_LINK = (
    config.get("links", {}).get("messenger_bridge")
    or config.get("links", {}).get("manychat_entry")
)

AFFILIATE_ID = (
    config.get("tracking", {}).get("AffiliateID")
    or config.get("affiliate_id")
)

FALLBACK_URL = config.get("links", {}).get("fallback")

# HARD FALLBACKS (prevents crashes)
if not MANYCHAT_LINK:
    MANYCHAT_LINK = "https://m.me/brightlane?ref=nwkkk7vkps17"

if not AFFILIATE_ID:
    raise ValueError("Missing AffiliateID in config.json")

# =========================
# CORE SETTINGS
# =========================
CHUNK_SIZE = 45000
BASE_URL = "https://brightlane.github.io/SameDayFlowers"
SITEMAP_DIR = "sitemaps"
PAGE_DIR = "blog"
TODAY = datetime.now().strftime("%Y-%m-%d")

AFFILIATE_LINK = (
    f"http://www.floristone.com/main.cfm?"
    f"source_id=aff&AffiliateID={AFFILIATE_ID}&occ=mothersday"
)

# =========================
# RESET OUTPUT DIRS
# =========================
for d in [SITEMAP_DIR, PAGE_DIR]:
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d)

# =========================
# LOAD CITY DATA
# =========================
with open("cities.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Deduplicate cities
seen = set()
clean = []

for item in data:
    city = item.get("city", "").strip()
    state = item.get("state", "").strip()

    if not city or not state:
        continue

    key = f"{city.lower()}-{state.lower()}"
    if key in seen:
        continue

    seen.add(key)
    clean.append({"city": city, "state": state})

total = len(clean)
parts = math.ceil(total / CHUNK_SIZE)
child_files = []

# =========================
# PAGE BUILDER
# =========================
def build_page(city, state, slug):
    return f"""<!DOCTYPE html>
<html>
<head>
  <title>Same Day Flowers in {city}, {state}</title>
  <meta name="description" content="Order same day flowers in {city}, {state}. Fast delivery available.">
</head>
<body>

<h1>Same Day Flowers in {city}, {state}</h1>

<button onclick="routeUser()">Order Flowers 🌸</button>

<script>
const MANYCHAT = "{MANYCHAT_LINK}";
const AFFILIATE = "{AFFILIATE_LINK}";

function routeUser() {{
  const now = new Date();
  const panicStart = new Date("2026-05-07");
  const panicEnd = new Date("2026-05-10");

  let url = AFFILIATE;

  // Panic window → ManyChat first
  if (now >= panicStart && now <= panicEnd) {{
    url = MANYCHAT;
  }}

  // Traffic split (40% ManyChat)
  if (Math.random() < 0.4) {{
    url = MANYCHAT;
  }}

  window.location.href = url;
}}
</script>

</body>
</html>"""

# =========================
# GENERATE SITEMAPS + PAGES
# =========================
for i in range(parts):
    filename = f"part-{i+1}.xml"
    child_files.append(filename)

    start = i * CHUNK_SIZE
    end = (i + 1) * CHUNK_SIZE
    chunk = clean[start:end]

    with open(os.path.join(SITEMAP_DIR, filename), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

        for item in chunk:
            city_slug = quote(item["city"].lower().replace(" ", "-"))
            state_slug = quote(item["state"].lower())

            slug = f"flowers-{city_slug}-{state_slug}.html"
            loc = f"{BASE_URL}/{PAGE_DIR}/{slug}"

            # sitemap entry
            f.write(f"<url><loc>{loc}</loc><lastmod>{TODAY}</lastmod></url>\n")

            # page generation
            page_html = build_page(item["city"], item["state"], slug)

            with open(os.path.join(PAGE_DIR, slug), "w", encoding="utf-8") as p:
                p.write(page_html)

        f.write("</urlset>")

    print(f"Created {filename}")

# =========================
# MASTER SITEMAP
# =========================
with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

    for child in child_files:
        f.write(f"<sitemap><loc>{BASE_URL}/{SITEMAP_DIR}/{child}</loc></sitemap>\n")

    f.write("</sitemapindex>")

print("\n--- VULTURE SYSTEM COMPLETE ---")
print(f"Pages: {total}")
print(f"Sitemaps: {parts}")
print("Status: SAFE BUILD (no KeyErrors)")
print("--------------------------------")
