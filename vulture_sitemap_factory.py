import math
import os
import json
import shutil
from datetime import datetime
from urllib.parse import quote

BASE_URL = "https://brightlane.github.io/SameDayFlowers"
SITEMAP_DIR = "sitemaps"
BLOG_DIR = "blog"
CHUNK_SIZE = 45000
TODAY = datetime.now().strftime("%Y-%m-%d")

# -----------------------------
# FULL PIPELINE ENTRY
# -----------------------------
def generate_vulture_production_sitemaps():

    # 1. RESET OUTPUTS
    for d in [SITEMAP_DIR, BLOG_DIR]:
        if os.path.exists(d):
            shutil.rmtree(d)
        os.makedirs(d)

    # 2. LOAD DATA
    if not os.path.exists("cities.json"):
        print("❌ Missing cities.json")
        return

    with open("cities.json", "r", encoding="utf-8") as f:
        all_data = json.load(f)

    # 3. CLEAN DATA
    seen = set()
    clean = []

    for item in all_data:
        city = item.get("city", "").strip()
        state = item.get("state", "").strip()

        if not city or not state:
            continue

        key = f"{city.lower()}-{state.lower()}"
        if key in seen:
            continue

        seen.add(key)
        clean.append({"city": city, "state": state})

    print(f"Total clean cities: {len(clean)}")

    # -----------------------------
    # 4. GENERATE PAGES (FIX YOU WERE MISSING THIS)
    # -----------------------------
    def build_page(city, state):
        slug = f"flowers-{city.lower().replace(' ','-')}-{state.lower()}.html"
        url = f"{BASE_URL}/blog/{slug}"

        html = f"""<!DOCTYPE html>
<html>
<head>
<title>Flowers in {city}, {state}</title>
</head>
<body>
<h1>Same Day Flowers in {city}, {state}</h1>

<a href="https://www.floristone.com/main.cfm?AffiliateID=2013017799&source_id=aff&occ=mothersday">
Order Flowers
</a>

</body>
</html>"""

        with open(os.path.join(BLOG_DIR, slug), "w", encoding="utf-8") as f:
            f.write(html)

        return url

    urls = []

    for item in clean:
        urls.append(build_page(item["city"], item["state"]))

    # -----------------------------
    # 5. SITEMAP CHUNKING
    # -----------------------------
    parts = math.ceil(len(urls) / CHUNK_SIZE)
    child_files = []

    for i in range(parts):
        chunk = urls[i * CHUNK_SIZE:(i + 1) * CHUNK_SIZE]
        filename = f"part-{i+1}.xml"
        child_files.append(filename)

        with open(os.path.join(SITEMAP_DIR, filename), "w", encoding="utf-8") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

            for url in chunk:
                f.write("  <url>\n")
                f.write(f"    <loc>{url}</loc>\n")
                f.write(f"    <lastmod>{TODAY}</lastmod>\n")
                f.write("  </url>\n")

            f.write("</urlset>")

    # -----------------------------
    # 6. INDEX SITEMAP
    # -----------------------------
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

        for file in child_files:
            f.write("  <sitemap>\n")
            f.write(f"    <loc>{BASE_URL}/{SITEMAP_DIR}/{file}</loc>\n")
            f.write(f"    <lastmod>{TODAY}</lastmod>\n")
            f.write("  </sitemap>\n")

        f.write("</sitemapindex>")

    print("✅ DONE: Pages + sitemap generated")
    print(f"Pages created: {len(urls)}")
    print(f"Sitemaps: {len(child_files)}")


if __name__ == "__main__":
    generate_vulture_production_sitemaps()
