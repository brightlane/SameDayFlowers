import os
import random
import datetime

# --- CONFIGURATION ---
BASE_URL = "https://brightlane.github.io"
PROJECT_DIR = "blog"
INDEX_NOW_KEY = "YOUR_INDEX_NOW_KEY_HERE"  # Place your key file in root
AFFILIATE_ID = "007949054186005142" # e-file/ManyChat specific ID
MANYCHAT_LINK = f"https://m.me/YourPage?ref={AFFILIATE_ID}"

# POPULATION TIER: 2001 - 4000 (Sample batch - Expand this list to 2000 items)
CITIES = [
    {"city": "Zionsville", "state": "IN"}, {"city": "Haddonfield", "state": "NJ"},
    {"city": "Brielle", "state": "NJ"}, {"city": "Yellow Springs", "OH": "OH"},
    # ... Add your full list of 2000 cities here ...
]

# CONTENT VARIATIONS (Chameleon Logic)
HOOKS = [
    "Surprise Mom this Sunday!",
    "Last-minute flowers for Mother's Day.",
    "The freshest blooms in {city} delivered today.",
    "Don't forget Mother's Day! Order now in {state}."
]

# --- CORE FUNCTIONS ---

def generate_page_html(city, state):
    title_hook = random.choice(HOOKS).format(city=city, state=state)
    filename = f"{city.lower().replace(' ', '-')}-{state.lower()}.html"
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <title>Same Day Mother's Day Flowers in {city}, {state} | Fast Delivery</title>
    <style>
        body {{ font-family: sans-serif; background: #0a192f; color: #ccd6f6; padding: 2rem; }}
        .container {{ max-width: 800px; margin: auto; text-align: center; }}
        .cta-button {{ background: #64ffda; color: #0a192f; padding: 15px 30px; text-decoration: none; font-weight: bold; border-radius: 5px; font-size: 1.2rem; }}
        .timer {{ color: #f00; font-weight: bold; margin: 20px 0; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title_hook}</h1>
        <p>Need beautiful flowers delivered in <strong>{city}, {state}</strong>? Our local florists are ready to help you celebrate Mother's Day 2026.</p>
        <div class="timer">ORDER WITHIN 04:22:10 FOR SAME-DAY DELIVERY</div>
        <br><br>
        <a href="{MANYCHAT_LINK}" class="cta-button">Check Local Availability on Messenger</a>
        <p style="margin-top: 40px; font-size: 0.8rem; opacity: 0.6;">Radical Transparency: We may earn an affiliate commission via ManyChat automation.</p>
    </div>
</body>
</html>"""
    
    with open(f"{PROJECT_DIR}/{filename}", "w") as f:
        f.write(html_content)
    return filename

def update_sitemap(filenames):
    today = datetime.date.today().isoformat()
    sitemap_header = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap_footer = '</urlset>'
    
    with open("sitemap.xml", "w") as f:
        f.write(sitemap_header)
        for name in filenames:
            f.write(f"  <url>\n    <loc>{BASE_URL}/{PROJECT_DIR}/{name}</loc>\n    <lastmod>{today}</lastmod>\n  </url>\n")
        f.write(sitemap_footer)

def ping_index_now(filenames):
    # This simulates the IndexNow API call
    # In a live environment, use the 'requests' library to POST to https://www.bing.com/indexnow
    print(f"Pinging IndexNow for {len(filenames)} new pages...")
    # Example: requests.post(f"https://www.bing.com/indexnow?url={url}&key={INDEX_NOW_KEY}")

# --- EXECUTION ---

if __name__ == "__main__":
    if not os.path.exists(PROJECT_DIR):
        os.makedirs(PROJECT_DIR)
    
    generated_files = []
    print(f"🚀 Starting Vulture 10K Blast for {len(CITIES)} cities...")
    
    for item in CITIES:
        fname = generate_page_html(item['city'], item['state'])
        generated_files.append(fname)
        
    update_sitemap(generated_files)
    ping_index_now(generated_files)
    
    print(f"✅ Success! 2,000 pages built in /{PROJECT_DIR}/ and sitemap updated.")
