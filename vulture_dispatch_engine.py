import os
import random
import datetime
import json

# --- CONFIG ---
BASE_URL = "https://brightlane.github.io/Flower-Dispatch-Network"
PROJECT_DIR = "dispatch"

AFFILIATE_ID = "2013017799"
MANYCHAT_LINK = f"https://m.me/brightlane?ref={AFFILIATE_ID}"

# --- DATA ---
ACTIONS = ["Dispatch", "Track", "Locate", "Send", "Rush", "Express"]
SUBJECTS = [
    "Flower Courier",
    "Local Delivery",
    "Mother's Day Flowers",
    "Floral Dispatch",
    "Gift Delivery"
]
URGENCY = ["Priority", "ASAP", "Immediate", "Scheduled", "Confirmed"]

HOOKS = [f"{a} {s} in {{city}} - {u}" for a in ACTIONS for s in SUBJECTS for u in URGENCY]

# --- SAFE FOLDER CREATION ---
os.makedirs(PROJECT_DIR, exist_ok=True)

def generate_page_html(city, state):
    title_hook = random.choice(HOOKS).format(city=city)
    filename = f"dispatch-{city.lower().replace(' ', '-')}-{state.lower()}.html"

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{title_hook}</title>
</head>
<body>

<h1>{city}, {state} Dispatch Center</h1>

<p>{title_hook}</p>

<a href="{MANYCHAT_LINK}">
INITIATE DISPATCH
</a>

</body>
</html>"""

    file_path = os.path.join(PROJECT_DIR, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

    return filename


def update_sitemap(files):
    today = datetime.date.today().isoformat()

    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    # Root
    sitemap += f"""
  <url>
    <loc>{BASE_URL}/</loc>
    <lastmod>{today}</lastmod>
  </url>
"""

    # Pages
    for f in files:
        sitemap += f"""
  <url>
    <loc>{BASE_URL}/{PROJECT_DIR}/{f}</loc>
    <lastmod>{today}</lastmod>
  </url>
"""

    sitemap += "</urlset>"

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)


# --- MAIN ---
if __name__ == "__main__":

    if not os.path.exists("cities.json"):
        print("❌ cities.json missing")
        exit()

    with open("cities.json", "r") as f:
        cities = json.load(f)[8000:10000]

    print(f"🚀 Generating {len(cities)} dispatch pages...")

    created_files = []

    for c in cities:
        try:
            file = generate_page_html(c["city"], c["state"])
            created_files.append(file)
        except Exception as e:
            print(f"❌ Error: {c} -> {e}")

    update_sitemap(created_files)

    print("✅ DONE: Pages + Sitemap generated")
