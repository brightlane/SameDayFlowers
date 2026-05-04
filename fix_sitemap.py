import os
import datetime

BASE_URL = "https://brightlane.github.io/SameDayFlowers"

# All folders your system actually generates pages into
PROJECT_DIRS = [
    "blog",
    "shop",
    "guide",
    "dispatch",
    "now"
]

OUTPUT_FILE = "sitemap.xml"

def collect_urls():
    urls = []

    for folder in PROJECT_DIRS:
        if not os.path.exists(folder):
            continue

        for file in os.listdir(folder):
            if file.endswith(".html"):
                urls.append(f"{BASE_URL}/{folder}/{file}")

    # also include root pages if they exist
    root_pages = [
        "index.html",
        "blog.html",
        "faq.html"
    ]

    for page in root_pages:
        if os.path.exists(page):
            urls.append(f"{BASE_URL}/{page}")

    return sorted(set(urls))


def build_sitemap(urls):
    today = datetime.date.today().isoformat()

    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for url in urls:
        xml.append("  <url>")
        xml.append(f"    <loc>{url}</loc>")
        xml.append(f"    <lastmod>{today}</lastmod>")
        xml.append("  </url>")

    xml.append("</urlset>")

    return "\n".join(xml)


def main():
    print("🚀 Rebuilding CLEAN sitemap.xml...")

    urls = collect_urls()

    if not urls:
        print("❌ No URLs found — sitemap NOT generated")
        return

    xml_content = build_sitemap(urls)

    # SAFE WRITE (prevents corruption)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(xml_content)

    print(f"✅ sitemap.xml rebuilt with {len(urls)} URLs")


if __name__ == "__main__":
    main()
