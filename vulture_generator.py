import os
import math
import json
import datetime

# =========================
# CONFIG
# =========================
BASE_URL = "https://brightlane.github.io/SameDayFlowers"
AFFILIATE_ID = "2013017799"

FLORISTONE_URL = f"http://www.floristone.com/main.cfm?source_id=aff&AffiliateID={AFFILIATE_ID}&occ=mothersday"
MANYCHAT_URL = f"https://m.me/brightlane?ref={AFFILIATE_ID}"

OUTPUT_DIR = "sitemaps"
CHUNK_SIZE = 50000  # SAFE LIMIT FOR GOOGLE

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================
# DATA (EXPANDABLE)
# =========================
cities = [
    "New York","Los Angeles","Chicago","Houston","Phoenix","Philadelphia",
    "San Antonio","San Diego","Dallas","San Jose","Austin","Seattle",
    "Denver","Boston","Miami","Atlanta","Toronto","Montreal","Vancouver"
]

states = [
    "NY","CA","IL","TX","AZ","PA","FL","GA","ON","QC","BC"
]

occasions = [
    "mothers-day",
    "birthday",
    "sympathy",
    "anniversary",
    "romance",
    "get-well"
]

# =========================
# URL GENERATOR (NO FILES)
# =========================
def generate_url(city, state, occ):
    slug = f"{city.lower().replace(' ','-')}-{state.lower()}-{occ}"
    return f"{BASE_URL}/blog/{slug}.html"

# =========================
# BUILD ALL URLS (VIRTUAL)
# =========================
urls = []

for city in cities:
    for state in states:
        for occ in occasions:
            urls.append(generate_url(city, state, occ))

total = len(urls)
print(f"Total virtual URLs: {total}")

# =========================
# CHUNKED SITEMAP GENERATION
# =========================
def write_sitemap_chunk(chunk, index):
    filename = f"sitemap-{index}.xml"
    path = os.path.join(OUTPUT_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

        for url in chunk:
            f.write("  <url>\n")
            f.write(f"    <loc>{url}</loc>\n")
            f.write("    <changefreq>daily</changefreq>\n")
            f.write("    <priority>0.7</priority>\n")
            f.write("  </url>\n")

        f.write("</urlset>")

    return filename

# =========================
# SPLIT INTO SAFE CHUNKS
# =========================
sitemap_files = []

num_chunks = math.ceil(total / CHUNK_SIZE)

for i in range(num_chunks):
    start = i * CHUNK_SIZE
    end = start + CHUNK_SIZE
    chunk = urls[start:end]

    fname = write_sitemap_chunk(chunk, i + 1)
    sitemap_files.append(fname)

# =========================
# SITEMAP INDEX
# =========================
index_file = "sitemap.xml"
index_path = os.path.join(OUTPUT_DIR, index_file)

with open(index_path, "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

    for file in sitemap_files:
        f.write("  <sitemap>\n")
        f.write(f"    <loc>{BASE_URL}/sitemaps/{file}</loc>\n")
        f.write(f"    <lastmod>{datetime.date.today()}</lastmod>\n")
        f.write("  </sitemap>\n")

    f.write("</sitemapindex>")

# =========================
# LLMS.TXT (AI INDEXING)
# =========================
llms = f"""llms.txt
AI Flower Delivery Index

Affiliate: {FLORISTONE_URL}

Top Intent Pages:
- Same day flower delivery USA
- Mother's Day flowers {datetime.date.today().year}
- birthday flowers same day delivery

Routing Logic:
- High intent → FloristOne affiliate
- Chat intent → ManyChat ({MANYCHAT_URL})
"""

with open("llms.txt", "w", encoding="utf-8") as f:
    f.write(llms)

# =========================
# REPORT
# =========================
print("\n--- TRILLION SAFE REPORT ---")
print(f"Total virtual URLs: {total}")
print(f"Sitemaps generated: {len(sitemap_files)}")
print("Affiliate ID:", AFFILIATE_ID)
print("Mode: TRILLION-SAFE (no file explosion)")
