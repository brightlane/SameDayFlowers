import os
import json
from datetime import date

# --------------------
# LOAD CONFIG
# --------------------
with open("config.json", "r") as f:
    cfg = json.load(f)

BASE_URL = cfg["site_base"]
AFFILIATE_URL = cfg["affiliate_url"]

# --------------------
# SIMPLE TEMPLATE RENDERER
# --------------------
def render(template, data):
    for k, v in data.items():
        template = template.replace("{{" + k + "}}", str(v))
    return template

# --------------------
# LOAD TEMPLATE
# --------------------
def load_template():
    with open("templates/page.html", "r", encoding="utf-8") as f:
        return f.read()

# --------------------
# PAGE GENERATOR
# --------------------
def generate_page(city, state, folder="blog"):
    template = load_template()

    slug = f"{city.lower().replace(' ', '-')}-{state.lower()}"
    filename = f"{slug}.html"

    html = render(template, {
        "title": f"Flowers in {city}, {state}",
        "heading": f"Same-Day Flowers in {city}",
        "content": f"Order fresh flowers delivered today in {city}, {state}.",
        "affiliate_url": AFFILIATE_URL
    })

    out_dir = os.path.join("build", folder)
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    return f"{folder}/{filename}"

# --------------------
# SITEMAP BUILDER (SAFE + CHUNKED)
# --------------------
def build_sitemap(urls, chunk_size=5000):
    os.makedirs("sitemaps", exist_ok=True)

    chunks = [urls[i:i + chunk_size] for i in range(0, len(urls), chunk_size)]

    index_xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    index_xml.append('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for i, chunk in enumerate(chunks):
        file_name = f"part-{i+1}.xml"
        file_path = os.path.join("sitemaps", file_name)

        xml = ['<?xml version="1.0" encoding="UTF-8"?>']
        xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

        for u in chunk:
            xml.append(f"<url><loc>{BASE_URL}/{u}</loc><lastmod>{date.today()}</lastmod></url>")

        xml.append("</urlset>")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(xml))

        index_xml.append(f"""
        <sitemap>
            <loc>{BASE_URL}/sitemaps/{file_name}</loc>
            <lastmod>{date.today()}</lastmod>
        </sitemap>
        """)

    index_xml.append("</sitemapindex>")

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write("\n".join(index_xml))

    print("✅ Sitemap built:", len(urls), "URLs")

# --------------------
# MAIN RUNNER
# --------------------
if __name__ == "__main__":

    # load cities
    with open("cities.json", "r") as f:
        cities = json.load(f)

    urls = []

    print("🚀 Generating pages...")

    for c in cities[:50000]:   # safe first batch
        url = generate_page(c["city"], c["state"], folder="blog")
        urls.append(url)

    print("📦 Building sitemap...")
    build_sitemap(urls)

    print("✅ DONE: Single Engine Build Complete")
