import math
import os
import json
from datetime import datetime

def generate_vulture_index(all_data):
    # FORCE TEST MODE: We set this to 5. 
    # If you have more than 5 cities, this MUST create 2+ parts.
    CHUNK_SIZE = 5 
    
    BASE_URL = "https://brightlane.github.io/SameDayFlowers"
    SITEMAP_DIR = "sitemaps"
    TODAY = datetime.now().strftime("%Y-%m-%d")

    # 1. KILL AND REBUILD: Clear the old sitemaps folder
    if os.path.exists(SITEMAP_DIR):
        import shutil
        shutil.rmtree(SITEMAP_DIR)
    os.makedirs(SITEMAP_DIR)

    # 2. DATA CHECK: How many cities are we actually working with?
    total = len(all_data)
    num_parts = math.ceil(total / CHUNK_SIZE)
    
    print(f"DEBUG: Processing {total} cities into {num_parts} parts.")

    child_files = []

    # 3. GENERATE PARTS
    for i in range(num_parts):
        filename = f"part-{i+1}.xml"
        child_files.append(filename)
        
        chunk = all_data[i*CHUNK_SIZE : (i+1)*CHUNK_SIZE]
        
        with open(f"{SITEMAP_DIR}/{filename}", "w") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
            for item in chunk:
                slug = f"flowers-{item['city'].lower().replace(' ', '-')}-{item['state'].lower()}.html"
                f.write(f'  <url><loc>{BASE_URL}/blog/{slug}</loc><lastmod>{TODAY}</lastmod></url>\n')
            f.write('</urlset>')

    # 4. GENERATE MASTER INDEX (The file that was "Stuck")
    # We use 'w+' to force a complete overwrite
    with open("sitemap.xml", "w+", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for child in child_files:
            f.write(f'  <sitemap>\n    <loc>{BASE_URL}/{SITEMAP_DIR}/{child}</loc>\n    <lastmod>{TODAY}</lastmod>\n  </sitemap>\n')
        f.write('</sitemapindex>')
    
    print(f"✅ DONE: sitemap.xml now contains {len(child_files)} entries.")

if __name__ == "__main__":
    # Test with 15 fake cities to GUARANTEE 3 parts in the index
    test_data = [{"city": f"City{i}", "state": "ST"} for i in range(15)]
    generate_vulture_index(test_data)
