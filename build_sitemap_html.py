import os
from datetime import date

BASE_URL = "https://brightlane.github.io/SameDayFlowers"

FOLDERS = ["blog", "guide", "shop", "dispatch"]

def collect_pages():
    pages = {}

    for folder in FOLDERS:
        if os.path.exists(folder):
            pages[folder] = [
                f for f in os.listdir(folder)
                if f.endswith(".html")
            ]
        else:
            pages[folder] = []

    return pages


def build_html():
    data = collect_pages()

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>SameDayFlowers Sitemap</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #0a0b10;
            color: #eaeaea;
            padding: 40px;
        }}
        h1 {{
            color: #ffffff;
        }}
        h2 {{
            color: #ff4757;
            margin-top: 40px;
        }}
        a {{
            color: #70a1ff;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .box {{
            margin-bottom: 30px;
            padding: 20px;
            background: #11141d;
            border-radius: 10px;
        }}
        .meta {{
            color: #888;
            font-size: 12px;
        }}
    </style>
</head>
<body>

<h1>📍 SameDayFlowers Sitemap</h1>
<div class="meta">Updated: {date.today()}</div>
"""

    total = 0

    for folder, files in data.items():
        html += f"<div class='box'>"
        html += f"<h2>/{folder}/</h2>"

        if not files:
            html += "<p>No pages found.</p>"
        else:
            for f in sorted(files):
                url = f"{BASE_URL}/{folder}/{f}"
                html += f'<div><a href="{url}">{f}</a></div>'
                total += 1

        html += "</div>"

    html += f"""
<p class="meta">Total Pages: {total}</p>

</body>
</html>
"""

    with open("sitemap.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("✅ sitemap.html generated with", total, "pages")


if __name__ == "__main__":
    build_html() 
