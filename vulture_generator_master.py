import json
import os
import random

def generate_pages():
    # 1. Setup paths
    # We use a relative path to ensure GitHub Actions sees the folder
    base_path = os.path.dirname(os.path.abspath(__file__))
    blog_dir = os.path.join(base_path, "blog")
    
    if not os.path.exists(blog_dir):
        os.makedirs(blog_dir)
        print(f"📁 Created directory: {blog_dir}")

    # 2. Load Cities
    try:
        with open('cities.json', 'r') as f:
            cities = json.load(f)
            # Targeting the 2001-4000 block
            target_block = cities[2000:4000]
    except Exception as e:
        print(f"❌ Failed to load cities.json: {e}")
        return

    print(f"🚀 Starting generation for {len(target_block)} cities...")

    # 3. Generation Loop
    for c in target_block:
        city_name = c['city']
        state_name = c['state']
        filename = f"flowers-{city_name.lower().replace(' ', '-')}-{state_name.lower()}.html"
        filepath = os.path.join(blog_dir, filename)

        html = f"""<!DOCTYPE html>
<html>
<head><title>Same Day Flowers {city_name}</title></head>
<body><h1>Flowers in {city_name}, {state_name}</h1>
<p>Order by 1PM for same day delivery.</p>
<a href="https://www.floristone.com/main.cfm?AffiliateID=2013017799">Order Now</a>
</body></html>"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

    print(f"✅ Success! Generated {len(target_block)} pages in /blog")

if __name__ == "__main__":
    generate_pages()
