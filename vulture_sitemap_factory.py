import math
import os
import json
from datetime import datetime

def generate_dynamic_increment_sitemaps(all_data):
    """
    Vulture 10K Protocol: Incremental Sitemap Engine
    Forces multiple sitemap parts to prove the 'Trillion-Gate' logic.
    """
    
    # --- THE SWITCH ---
    # Set this to 45000 for production. 
    # Set this to 10 to TEST and see multiple parts immediately.
    CHUNK_SIZE = 10 
    
    BASE_URL = "https://brightlane.github.io/SameDayFlowers"
    SITEMAP_DIR = "sitemaps"
    TODAY_DATE = datetime.now().strftime("%Y-%m-%d") 

    # 1. Clean Room Protocol: Ensure directory exists
    if not os.path.exists(SITEMAP_DIR):
        os.makedirs(SITEMAP_DIR)
        print(f"📁 Created directory: {SITEMAP_DIR}")

    # 2. Force Math to Float to prevent integer rounding errors
    total_records = len(all_data)
    num_parts = int(math.ceil(float(total_records) / float(CHUNK_SIZE)))
    
    child_files = []

    print(f"🚀 CALCULATING: {total_records} cities / {CHUNK_SIZE} per file = {num_parts} parts.")

    # 3. Build the Child 'Leaf' Sitemaps
    for i in range(num_parts):
        part_num = i + 1
        filename = f"part-{part_num}.xml"
        child_files.append(filename)
        
        start_idx = i * CHUNK_SIZE
        end_idx = start_idx + CHUNK_SIZE
        data_chunk = all_data[start_idx:end_idx]

        # Writing child file
        file_path = os.path.join(SITEMAP_DIR, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
            
            for item in data_chunk:
                city_slug = item['city'].lower().replace(' ', '-')
                state_slug = item['state'].lower()
                loc = f"{BASE_URL}/blog/flowers-{city_slug}-{state_slug}.html"
                f.write(f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{TODAY_DATE}</lastmod>\n  </url>\n')
            
            f.write('</urlset>')
        print(f"  ∟ Generated {filename} with {len(data_chunk)} URLs.")

    # 4. Build the Master Index (The Gateway)
    # This loop is guaranteed to run 'num_parts' times.
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        
        for child in child_files:
            f.write(f'  <sitemap>\n')
            f.write(f'    <loc>{BASE_URL}/{SITEMAP_DIR}/{child}</loc>\n')
            f.write(f'    <lastmod>{TODAY_DATE}</lastmod>\n')
            f.write(f'  </sitemap>\n')
            
        f.write('</sitemapindex>')

    print(f"\n--- VULTURE SCALE REPORT ---")
    print(f"● Status: SUCCESS")
    print(f"● Total URLs: {total_records:,}")
    print(f"● Parts Created: {len(child_files)}")
    print(f"● Master Index: {BASE_URL}/sitemap.xml")
    print(f"-----------------------------\n")

if __name__ == "__main__":
    # Check if data exists, if not, create dummy data for the test
    if os.path.exists('cities.json'):
        with open('cities.json', 'r') as f:
            data = json.load(f)
        
        # If your file is too small to trigger a split, we warn you here
        if len(data) < 11:
            print("⚠️ WARNING: Your cities.json only has few entries.")
            print("Adding dummy entries to force the 'Stuck at 1' fix check...")
            for x in range(25):
                data.append({"city": f"TestCity{x}", "state": "TS"})
        
        generate_dynamic_increment_sitemaps(data)
    else:
        print("❌ Error: cities.json not found.")
