import os

BASE_URL = "https://brightlane.github.io/SameDayFlowers"

FOLDERS = ["blog", "shop", "guide", "dispatch", "now", "trending"]

OUTPUT_FILE = "sitemap.html"

def collect():
    pages = []

    for folder in FOLDERS:
        if not os.path.exists(folder):
            continue

        for f in os.listdir(folder):
            if f.endswith(".html"):
                pages.append(f"{BASE_URL}/{folder}/{f}")

    return sorted(pages)


def build(pages):
    html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Sitemap</title>
<style>
body { font-family: Arial; background:#0a0b10; color:#fff; padding:40px; }
a { color:#70a1ff; display:block; margin:6px 0; }
h1 { color:#ff4757; }
</style>
</head>
<body>

<h1>Auto Sitemap</h1>
"""

    html += f"<p>Total pages: {len(pages)}</p>\n"

    for url in pages:
        html += f'<a href="{url}">{url}</a>\n'

    html += """
</body>
</html>
"""

    return html


def main():
    pages = collect()

    if not pages:
        print("❌ No pages found")
        return

    html = build(pages)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ sitemap.html generated with {len(pages)} pages")


if __name__ == "__main__":
    main()
