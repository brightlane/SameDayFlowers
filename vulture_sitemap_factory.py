import math
import os
import json
from datetime import datetime

def generate_dynamic_increment_sitemaps(all_data):
    """
    Vulture 10K Protocol: Incremental Sitemap Engine
    Scales from 50k to 1 Trillion URLs using Hierarchical Indexing.
    """
    # The official XML protocol limit is 50,000. 
    # 45,000 is used as a safety buffer for bot processing speed.
    CHUNK_SIZE = 45000 
    
    BASE_URL = "https://brightlane.github.io/SameDayFlowers"
    SITEMAP_DIR = "sitemaps"
    # Dynamic date ensures search engines see 'fresh' content daily
    TODAY_DATE = datetime.now().strftime("%Y-%m-%d") 

    # Ensure the sub-directory exists for the distributed parts
    if not os.path.exists(SITEMAP_DIR):
        os.makedirs(SITEMAP_DIR)
        print(f"📁 Created directory: {SITEMAP_DIR}")

    # 1. Calculate the total footprint
    total_records = len(all_data)
    num_parts = math.ceil(total_records / CHUNK_SIZE)
    
    child_files = []

    # 2. Build the Child 'Leaf' Sitemaps
    for i in range(num_parts):
        part_num = i + 1
        filename = f"part-{part_num}.xml"
        child_files.append(filename)
        
        start_idx = i * CHUNK_SIZE
        end_idx = start_idx + CHUNK_SIZE
        data_chunk = all_data[start_idx:end_idx]

        # Writing child file to the /sitemaps/ directory
        file_path = os.path.join(SITEMAP_DIR, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
            
            for item in data_chunk:
                # Normalizing city/state for the URL slug
                city_slug = item['city'].lower().replace(' ', '-')
                state_slug = item['state'].lower()
                loc = f"{BASE_URL}/blog/flowers-{city_slug}-{state_slug}.html"
                
                f.write(f'  <url>\n    <loc>{loc}</loc>\n    <lastmod>{TODAY_DATE}</lastmod>\n  </url>\n')
            
            f.write('</urlset>')

    # 3. Build the Master Index (The Gateway)
    # Submit THIS file to Google Search Console and Bing Webmaster Tools
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        
        for child in child_files:
            f.write(f'  <sitemap>\n')
            f.write(f'    <loc>{BASE_URL}/{SITEMAP_DIR}/{child}</loc>\n')
            f.write(f'    <lastmod>{TODAY_DATE}</lastmod>\n')
            f.write(f'  </sitemap>\n')
            
        f.write('</sitemapindex>')

    print(f"--- VULTURE SCALE REPORT ---")
    print(f"● Total URLs Mapped: {total_records:,}")
    print(f"● Active Sitemap Parts: {num_parts}")
    print(f"● Master Index: {BASE_URL}/sitemap.xml")
    print(f"-----------------------------")

if __name__ == "__main__":
    # Integration for local testing
    if os.path.exists('cities.json'):
        with open('cities.json', 'r') as f:
            data = json.load(f)
        generate_dynamic_increment_sitemaps(data)
    else:
        print("❌ Error: cities.json not found. Feed the Vulture.")
