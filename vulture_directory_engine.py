import os
import random
import datetime
import json
from urllib.parse import quote

BASE_URL = "https://brightlane.github.io/Local-Flower-Directory"
PROJECT_DIR = "guide"

AFFILIATE_ID = "2013017799"
MANYCHAT_LINK = f"https://m.me/brightlane?ref={AFFILIATE_ID}"

ACTIONS = ["Best", "Top Rated", "Find", "Compare", "Local", "Reviews for"]
SUBJECTS = ["Flower Delivery", "Florists", "Mother's Day Flowers", "Same Day Service", "Gift Shops"]
URGENCY = ["2026 Guide", "Today", "Now", "Verified", "Ranked"]

HOOKS = [f"{a} {s} in {{city}} - {u}" for a in ACTIONS for s in SUBJECTS for u in URGENCY]

os.makedirs(PROJECT_DIR, exist_ok=True)


def safe_slug(text):
    return quote(text.lower().replace(" ", "-"))


def generate_page_html(city, state):
    if not city or not state:
        return None

    title_hook = random.choice(HOOKS).format(city=city)

    filename = f"best-flowers-{safe_slug(city)}-{state.lower()}.html"
    path = os.path.join(PROJECT_DIR, filename)

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{title_hook}</title>
</head>
<body>

<h1>{city}, {state}</h1>
<p>{title_hook}</p>

<a href="{MANYCHAT_LINK}">
View Florists
</a>

</body>
</html>"""

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    return filename


def update_sitemap(files):
    today = datetime.date.today().isoformat()

    sitemap = '<?xml version="1.0"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for f in files:
        if not f:
            continue

        sitemap += f"""
  <url>
    <loc>{BASE_URL}/{PROJECT_DIR}/{f}</loc>
    <lastmod>{today}</lastmod>
  </url>
"""

    sitemap += "</urlset>"

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)


if __name__ == "__main__":

    with open("cities.json", "r", encoding="utf-8") as f:
        cities = json.load(f)[6000:8000]

    print(f"🚀 Generating {len(cities)} directory pages...")

    created = []

    for c in cities:
        try:
            file = generate_page_html(c.get("city"), c.get("state"))
            if file:
                created.append(file)
        except Exception as e:
            print(f"❌ Error: {e}")

    update_sitemap(created)

    print(f"✅ DONE: {len(created)} pages generated")
