import os
import json
import shutil
from datetime import datetime
from urllib.parse import quote

# =========================
# SETTINGS
# =========================
BASE_URL = "https://brightlane.github.io/SameDayFlowers"
PAGE_DIR = "blog"
TODAY = datetime.now().strftime("%Y-%m-%d")

# Affiliate (hard safe)
AFFILIATE_LINK = "http://www.floristone.com/main.cfm?source_id=aff&AffiliateID=2013017799&occ=mothersday"
MANYCHAT_LINK = "https://m.me/brightlane?ref=nwkkk7vkps17"

# =========================
# FORCE CLEAN BUILD FOLDER
# =========================
if os.path.exists(PAGE_DIR):
    shutil.rmtree(PAGE_DIR)

os.makedirs(PAGE_DIR, exist_ok=True)

# =========================
# LOAD DATA (IMPORTANT)
# =========================
if not os.path.exists("cities.json"):
    raise FileNotFoundError("cities.json is missing")

with open("cities.json", "r", encoding="utf-8") as f:
    cities = json.load(f)

# =========================
# PAGE TEMPLATE
# =========================
def build_page(city, state, slug):
    return f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Flowers in {city}, {state}</title>
</head>
<body>

<h1>Same Day Flowers in {city}, {state}</h1>

<button onclick="go()">Order Flowers</button>

<script>
const affiliate = "{AFFILIATE_LINK}";
const manychat = "{MANYCHAT_LINK}";

function go() {{
  window.location.href = affiliate;
}}
</script>

</body>
</html>"""

# =========================
# GENERATE PAGES
# =========================
count = 0

for item in cities:
    city = item.get("city", "").strip()
    state = item.get("state", "").strip()

    if not city or not state:
        continue

    city_slug = quote(city.lower().replace(" ", "-"))
    state_slug = quote(state.lower())

    filename = f"flowers-{city_slug}-{state_slug}.html"
    path = os.path.join(PAGE_DIR, filename)

    html = build_page(city, state, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    count += 1
    print(f"Created: {path}")

# =========================
# FINAL DEBUG OUTPUT
# =========================
print("\n--- BUILD SUMMARY ---")
print("Pages created:", count)
print("Folder exists:", os.path.exists(PAGE_DIR))
print("Files in blog:", len(os.listdir(PAGE_DIR)))
