import math
import os
import json
import shutil
from datetime import datetime

def generate_vulture_production_sitemaps():
    """
    Vulture 10K Protocol: Production Sitemap Engine
    Scales from 50k to 1 Trillion URLs.
    """
    
    # --- CONFIGURATION ---
    CHUNK_SIZE = 45000  # Standard safety limit for search engine bots
    BASE_URL = "https://brightlane.github.io/SameDayFlowers"
    SITEMAP_DIR = "sitemaps"
    TODAY = datetime.now().strftime("%Y-%m-%d")

    # 1. HARD RESET: Wipe old sitemaps to prevent 'ghost' files
    if os.path.exists(SITEMAP_DIR):
        shutil.rmtree(SITEMAP_DIR)
    os.makedirs(SITEMAP_DIR)

    # 2. LOAD REAL DATA: Reading your cities.json
    if not os.path.exists('cities.json'):
        print("❌ ERROR: 'cities.json' not found in this folder!")
        return

    with open('cities.json', 'r', encoding='utf-8') as f:
        all_data = json.load(f)

    total_records = len(all_data)
    num_parts = math.ceil(total_records / CHUNK_SIZE)
    
    child_files = []

    # 3. GENERATE CHILD PARTS (The Inventory)
    for i in range(num_parts):
        filename = f"part-{i+1}.xml"
        child_files.append(filename)
        
        start = i * CHUNK_SIZE
        end = (i + 1) * CHUNK_SIZE
        chunk = all_data[start:end]

        file_path = os.path.join(SITEMAP_DIR, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
            
            for item in chunk:
                # Format: flowers-city-st.html
                city_slug = item['city'].lower().replace(' ', '-')
                state_slug = item['state'].lower()
                loc = f"{BASE_URL}/blog/flowers-{city_slug}-{state_slug}.html"
                f.write(f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{TODAY}</lastmod>\n  </url>\n')
            
            f.write('</urlset>')
        print(f"  ∟ Created {filename} ({len(chunk)} URLs)")

    # 4. GENERATE MASTER INDEX (The Gateway)
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        
        for child in child_files:
            f.write(f'  <sitemap>\n')
            f.write(f'    <loc>{BASE_URL}/{SITEMAP_DIR}/{child}</loc>\n')
            f.write(f'    <lastmod>{TODAY}</lastmod>\n')
            f.write(f'  </sitemap>\n')
            
        f.write('</sitemapindex>')

    print(f"\n--- VULTURE FINAL REPORT ---")
    print(f"● Processed: {total_records:,} cities")
    print(f"● Created: {num_parts} sitemap parts")
    print(f"● Status: Ready for Mother's Day 2026 deployment")
    print(f"-----------------------------\n")

if __name__ == "__main__":
    generate_vulture_production_sitemaps()
