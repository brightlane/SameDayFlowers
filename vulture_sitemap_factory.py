import math
import os
import json
import shutil
from datetime import datetime
from urllib.parse import quote

def generate_vulture_production_sitemaps():
    """
    Vulture 10K Protocol: Production Sitemap Engine (Repaired)
    """

    # --- CONFIGURATION ---
    CHUNK_SIZE = 45000
    BASE_URL = "https://brightlane.github.io/SameDayFlowers"
    SITEMAP_DIR = "sitemaps"
    TODAY = datetime.now().strftime("%Y-%m-%d")

    # OPTIONAL: keep affiliate tracking (DO NOT use in sitemap unless intentional)
    AFFILIATE_PARAMS = "?atid=ProfessorOwlTaxGuide&campaign=vulture_10k_mothers_day"

    # 1. HARD RESET
    if os.path.exists(SITEMAP_DIR):
        shutil.rmtree(SITEMAP_DIR)
    os.makedirs(SITEMAP_DIR)

    # 2. LOAD DATA
    if not os.path.exists('cities.json'):
        print("❌ ERROR: 'cities.json' not found!")
        return

    with open('cities.json', 'r', encoding='utf-8') as f:
        all_data = json.load(f)

    # 3. CLEAN + DEDUPE
    seen = set()
    clean_data = []

    for item in all_data:
        city = item.get('city', '').strip()
        state = item.get('state', '').strip()

        if not city or not state:
            continue

        key = f"{city.lower()}-{state.lower()}"
        if key in seen:
            continue

        seen.add(key)
        clean_data.append({"city": city, "state": state})

    total_records = len(clean_data)
    num_parts = math.ceil(total_records / CHUNK_SIZE)

    child_files = []

    # 4. GENERATE CHILD SITEMAPS
    for i in range(num_parts):
        filename = f"part-{i+1}.xml"
        child_files.append(filename)

        start = i * CHUNK_SIZE
        end = (i + 1) * CHUNK_SIZE
        chunk = clean_data[start:end]

        file_path = os.path.join(SITEMAP_DIR, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

            for item in chunk:
                # slug safe
                city_slug = quote(item['city'].lower().replace(' ', '-'))
                state_slug = quote(item['state'].lower())

                # IMPORTANT: canonical URL (no tracking params)
                loc = f"{BASE_URL}/blog/flowers-{city_slug}-{state_slug}.html"

                f.write("  <url>\n")
                f.write(f"    <loc>{loc}</loc>\n")
                f.write(f"    <lastmod>{TODAY}</lastmod>\n")
                f.write("  </url>\n")

            f.write('</urlset>')

        print(f"  ∟ Created {filename} ({len(chunk)} URLs)")

    # 5. GENERATE INDEX
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

        for child in child_files:
            f.write("  <sitemap>\n")
            f.write(f"    <loc>{BASE_URL}/{SITEMAP_DIR}/{child}</loc>\n")
            f.write(f"    <lastmod>{TODAY}</lastmod>\n")
            f.write("  </sitemap>\n")

        f.write('</sitemapindex>')

    print("\n--- VULTURE FINAL REPORT ---")
    print(f"● Clean URLs: {total_records:,}")
    print(f"● Sitemap parts: {num_parts}")
    print("● Affiliate tracking: PRESERVED (not in sitemap for SEO safety)")
    print("● Status: READY FOR INDEXING")
    print("-----------------------------\n")


if __name__ == "__main__":
    generate_vulture_production_sitemaps()
