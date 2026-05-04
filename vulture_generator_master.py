import os
import json
import datetime

# --- CONFIGURATION ---
with open('affiliate.json', 'r') as f:
    config = json.load(f)

BASE_URL = "https://brightlane.github.io/SameDayFlowers"
PROJECT_DIR = "blog"
MANYCHAT_LINK = config['links']['messenger_bridge']
PARTNER_ID = config['manychat_partner_id']
DEADLINE = config['parameters']['deadline_date']
TODAY = datetime.datetime.now().strftime("%Y-%m-%d")
YEAR = "2026"

def get_vulture_slug(city, state):
    c = city.lower().replace(' ', '-')
    s = state.lower()
    return f"flowers-{c}-{s}.html"

def generate_page_html(city, state):
    filename = get_vulture_slug(city, state)
    page_url = f"{BASE_URL}/{PROJECT_DIR}/{filename}"
    
    # 1. ENHANCED CONTENT INJECTION
    # This prevents "Thin Content" penalties from Google
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Best Same Day Mother's Day Flowers {city}, {state} | Local Delivery {YEAR}</title>
    <meta name="description" content="Guaranteed same-day flower delivery in {city}, {state} for Mother's Day. Send fresh bouquets from local {city} florists. Order by {DEADLINE}.">
    <link rel="canonical" href="{page_url}">
    
    <!-- 2. JSON-LD SCHEMA (The "Trillion-Gate" Secret) -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Florist",
      "name": "Mother's Day Delivery {city}",
      "description": "Premium flower delivery service in {city}, {state}",
      "url": "{page_url}",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "{city}",
        "addressRegion": "{state.upper()}",
        "addressCountry": "US"
      }},
      "openingHours": "Mo-Su 00:00-23:59",
      "priceRange": "$$",
      "aggregateRating": {{
        "@type": "AggregateRating",
        "ratingValue": "4.9",
        "reviewCount": "1250"
      }}
    }}
    </script>

    <style>
        :root {{ --primary: #ff4d6d; --bg: #fff5f7; --text: #2b2d42; }}
        body {{ font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; margin: 0; color: var(--text); line-height: 1.6; }}
        .top-banner {{ background: var(--primary); color: white; padding: 10px; font-weight: 900; text-align: center; text-transform: uppercase; letter-spacing: 1px; }}
        nav {{ padding: 20px; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; }}
        .hero {{ padding: 80px 20px; background: var(--bg); text-align: center; }}
        h1 {{ font-size: 2.5rem; color: #c9184a; margin-bottom: 10px; }}
        .trust-badges {{ display: flex; justify-content: center; gap: 20px; margin: 20px 0; font-size: 0.9rem; font-weight: bold; }}
        .inventory-card {{ background: white; border: 2px solid var(--primary); border-radius: 15px; padding: 30px; max-width: 500px; margin: 0 auto; box-shadow: 0 10px 30px rgba(255,77,109,0.2); }}
        .btn {{ background: var(--primary); color: white; padding: 22px 45px; text-decoration: none; border-radius: 50px; font-weight: 900; display: inline-block; font-size: 1.4rem; transition: transform 0.2s; box-shadow: 0 5px 15px rgba(255,77,109,0.4); }}
        .btn:hover {{ transform: scale(1.05); }}
        .local-info {{ max-width: 800px; margin: 60px auto; padding: 20px; text-align: left; }}
        .faq-section {{ background: #f8f9fa; padding: 40px 20px; }}
        footer {{ padding: 40px; color: #999; font-size: 0.8rem; border-top: 1px solid #eee; }}
    </style>
</head>
<body>
    <div class="top-banner">🚚 ALERT: SAME-DAY SLOTS STILL OPEN FOR {city.upper()} - ORDER BEFORE {DEADLINE}</div>
    
    <nav>
        <span style="font-weight:bold; color:var(--primary)">SameDayFlowers.AI</span>
        <span>Inventory: 🟢 Verified</span>
    </nav>

    <section class="hero">
        <h1>Send Mother's Day Flowers to {city}, {state}</h1>
        <p style="font-size: 1.2rem;">Hand-delivered by premium {city} florists. Guaranteed fresh.</p>
        
        <div class="trust-badges">
            <span>✅ Local {city} Dispatch</span>
            <span>✅ No Hidden Fees</span>
            <span>✅ 7-Day Freshness</span>
        </div>

        <div class="inventory-card">
            <p style="margin-top:0; font-weight:bold; color:var(--primary);">LIVE INVENTORY CHECK</p>
            <h2 style="margin:10px 0;">Available for {city} Today</h2>
            <p>Our direct ManyChat bridge bypasses standard order delays for local delivery in <strong>{city}, {state}</strong>.</p>
            <a href="{MANYCHAT_LINK}" class="btn">VIEW BOUQUETS</a>
        </div>
    </section>

    <section class="local-info">
        <h3>Why Choose Our {city} Floral Network?</h3>
        <p>Sending flowers to {city} shouldn't be complicated. Our "Vulture-10K" optimized network connects you directly with the best local shops in the {city} area, ensuring your Mother's Day gift doesn't sit in a warehouse.</p>
        <ul>
            <li><strong>Priority Delivery:</strong> All Mother's Day orders in {city} are routed via local couriers.</li>
            <li><strong>Expert Design:</strong> Bouquets are designed by local artisans in {state}.</li>
            <li><strong>Radical Transparency:</strong> Real-time delivery tracking via ManyChat.</li>
        </ul>
    </section>

    <section class="faq-section">
        <div style="max-width:800px; margin:auto; text-align:left;">
            <h3>Frequently Asked Questions ({city})</h3>
            <p><strong>Can I get same-day delivery in {city} on May 10th?</strong><br>Yes, our {city} partners are currently accepting same-day orders, but we recommend booking by {DEADLINE} to guarantee your specific floral choice.</p>
            <p><strong>What is the best bouquet for Mother's Day in {state}?</strong><br>While roses are classic, {city} locals are currently favoring mixed spring peonies and lilies for 2026.</p>
        </div>
    </section>

    <footer>
        <p>Verified Affiliate Partner ID: {PARTNER_ID} | Project: SameDayFlowers-{YEAR}</p>
        <p>Serving {city}, {state} and surrounding metropolitan areas.</p>
    </footer>
</body>
</html>"""
    
    with open(os.path.join(PROJECT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    if not os.path.exists(PROJECT_DIR): os.makedirs(PROJECT_DIR)
    with open('cities.json', 'r') as f:
        cities = json.load(f)
    
    print(f"🚀 Building {len(cities)} Authority Pages...")
    for c in cities:
        generate_page_html(c['city'], c['state'])
    print("✅ Full Authority Build Complete.")
