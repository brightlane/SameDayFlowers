import os
import json
import shutil
from urllib.parse import quote

BASE_URL = "https://brightlane.github.io/SameDayFlowers"
PAGE_DIR = "blog"
SITEMAP_DIR = "sitemaps"

AFFILIATE_LINK = "http://www.floristone.com/main.cfm?source_id=aff&AffiliateID=2013017799&occ=mothersday"
MANYCHAT_LINK = "https://m.me/brightlane?ref=nwkkk7vkps17"

# =========================
# CLEAN OUTPUT
# =========================
for folder in [PAGE_DIR, SITEMAP_DIR]:
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)

# =========================
# LOAD DATA (FAIL FAST IF MISSING)
# =========================
if not os.path.exists("cities.json"):
    raise FileNotFoundError("cities.json missing in repo")

with open("cities.json", "r", encoding="utf-8") as f:
    cities = json.load(f)

print("Cities loaded:", len(cities))

# =========================
# PAGE TEMPLATE
# =========================
def build_page(city, state):
    return f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Flowers in {city}, {state}</title>
</head>
<body>

<h1>Same Day Flowers in {city}, {state}</h1>

<a href="{AFFILIATE_LINK}">Order Flowers</a>
<br>
<a href="{MANYCHAT_LINK}">Order via Chat</a>

</body>
</html>"""

# =========================
# GENERATE FILES
# =========================
child_sitemaps = []
count = 0

for i, item in enumerate(cities):
    city = item.get("city", "").strip()
    state = item.get("state", "").strip()

    if not city or not state:
        continue

    slug = f"flowers-{quote(city.lower().replace(' ', '-'))}-{quote(state.lower())}.html"
    path = os.path.join(PAGE_DIR, slug)

    with open(path, "w", encoding="utf-8") as f:
        f.write(build_page(city, state))

    count += 1

# =========================
# SITEMAP (SINGLE FILE = SIMPLER + RELIABLE)
# =========================
sitemap_path = os.path.join(SITEMAP_DIR, "sitemap.xml")

with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

    for file in os.listdir(PAGE_DIR):
        url = f"{BASE_URL}/{PAGE_DIR}/{file}"
        f.write(f"<url><loc>{url}</loc></url>\n")

    f.write("</urlset>")

print("Pages created:", count)
print("Sitemap generated")
