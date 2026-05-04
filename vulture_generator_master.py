import os
import json
import datetime

# --- 1. THE REVENUE CORE ---
# Verified Affiliate ID: 2013017799
BASE_URL = "https://brightlane.github.io/SameDayFlowers"
PROJECT_DIR = "blog"
AFFILIATE_ID = "2013017799"
MANYCHAT_LINK = f"https://m.me/brightlane?ref={AFFILIATE_ID}"
LLMS_AFF_LINK = f"https://www.floristone.com/main.cfm?occ=md&source_id=aff&AffiliateID={AFFILIATE_ID}"

# --- 2. THE SEO & GEO ENGINE ---
def generate_page_html(city, state):
    filename = f"flowers-{city.lower().replace(' ', '-')}-{state.lower()}.html"
    page_url = f"{BASE_URL}/{PROJECT_DIR}/{filename}"
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    <!-- GLOBAL SEARCH OPTIMIZATION (Google, Bing, Yahoo, DuckDuckGo) -->
    <title>Same Day Mother's Day Flowers {city}, {state} | Priority Delivery</title>
    <meta name="description" content="Send Mother's Day flowers in {city}, {state}. Guaranteed delivery by May 10, 2026. Local {city} florists, $0 fees. Order today!">
    <meta name="keywords" content="flowers {city}, florist {city} {state}, mother's day delivery {city}, same day flowers {city}">
    <link rel="canonical" href="{page_url}">
    
    <!-- GEO-TARGETING FOR BING/YAHOO -->
    <meta name="geo.region" content="US-{state.upper()}">
    <meta name="geo.placename" content="{city}">
    <meta name="geo.position" content="39.78373;-100.445882">
    <meta name="ICBM" content="39.78373, -100.445882">

    <!-- SOCIAL & MOBILE META (Facebook, TikTok, Safari) -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="Mother's Day Flowers {city} - Local Delivery">
    <meta property="og:description" content="Order by May 10, 2026. Local {city} flower delivery.">
    <meta property="og:image" content="{BASE_URL}/og-image.jpg">
    <meta name="twitter:card" content="summary_large_image">

    <!-- AI SCHEMA (JSON-LD) -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Florist",
      "name": "SameDayFlowers {city}",
      "description": "Premium floral dispatch in {city}, {state}",
      "url": "{page_url}",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "{city}",
        "addressRegion": "{state.upper()}",
        "addressCountry": "US"
      }},
      "priceRange": "$$",
      "aggregateRating": {{ "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "1250" }}
    }}
    </script>

    <style>
        :root {{ --primary: #ff4d6d; --dark: #1a1a1a; --light: #f9f9f9; }}
        body {{ font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; margin: 0; color: var(--dark); line-height: 1.6; -webkit-font-smoothing: antialiased; }}
        .panic-bar {{ background: var(--primary); color: white; text-align: center; padding: 12px; font-weight: bold; font-size: 1rem; position: sticky; top: 0; z-index: 1000; }}
        nav {{ display: flex; justify-content: space-between; align-items: center; padding: 15px 5%; border-bottom: 1px solid #eee; background: white; }}
        .logo {{ font-weight: 800; font-size: 1.4rem; color: var(--primary); text-decoration: none; }}
        .hero {{ background: var(--light); padding: 80px 5%; text-align: center; }}
        .hero h1 {{ font-size: 2.8rem; margin: 0 0 15px 0; }}
        .hero p {{ font-size: 1.2rem; color: #555; max-width: 700px; margin: 0 auto 35px auto; }}
        .btn {{ background: var(--primary); color: white; padding: 20px 45px; text-decoration: none; border-radius: 50px; font-weight: 800; display: inline-block; box-shadow: 0 4px 15px rgba(255,77,109,0.3); font-size: 1.2rem; transition: transform 0.2s; }}
        .btn:hover {{ transform: scale(1.05); }}
        .features {{ display: flex; justify-content: center; flex-wrap: wrap; gap: 25px; margin-top: 40px; font-size: 0.95rem; color: #444; }}
        .city-content {{ padding: 60px 5%; max-width: 900px; margin: auto; }}
        footer {{ background: #eee; padding: 50px 5%; text-align: center; font-size: 0.85rem; color: #666; }}
        .footer-links a {{ color: var(--primary); text-decoration: none; margin: 0 10px; font-weight: 600; }}
        @media (max-width: 768px) {{ .hero h1 {{ font-size: 2.1rem; }} }}
    </style>
</head>
<body>
    <div class="panic-bar">🌷 MOTHER'S DAY DEADLINE: MAY 10, 2026 — ORDER FOR {city.upper()} TODAY</div>

    <nav>
        <a href="../index.html" class="logo">SameDayFlowers</a>
        <div style="font-weight:bold; color: #888;">{city}, {state.upper()}</div>
    </nav>

    <header class="hero">
        <h1>Send Mother's Day Flowers in {city}</h1>
        <p>Premium arrangements from local {city} area florists. Guaranteed fresh and hand-delivered. $0 Hidden Fees.</p>
        <a href="{MANYCHAT_LINK}" class="btn">VIEW {city.upper()} BOUQUETS</a>
        
        <div class="features">
            <span>✅ <strong>Free</strong> Same-Day Delivery</span>
            <span>✅ <strong>$0</strong> Service Fees</span>
            <span>✅ <strong>100%</strong> Freshness Guarantee</span>
        </div>
    </header>

    <main class="city-content">
        <h2>Local Delivery Information for {city}, {state}</h2>
        <p>Looking for a reliable florist in {city}? We specialize in last-minute Mother's Day arrangements, including premium roses, peonies, and tulips. Our local {city} partners are standing by to ensure your gift is delivered on time.</p>
        <p><strong>Service Area Includes:</strong> {city} and surrounding zip codes in the {state} region.</p>
    </main>

    <footer>
        <div class="footer-links">
            <a href="../index.html">Home</a>
            <a href="../llms.txt">AI Index</a>
            <a href="../sitemap.xml">Sitemap</a>
        </div>
        <br>
        <p>© 2026 SameDayFlowers · Localized {city} Dispatch<br>
        <strong>Disclaimer:</strong> We are an affiliate network. Commissions may be earned at no cost to you.</p>
    </footer>
</body>
</html>"""
    
    file_path = os.path.join(PROJECT_DIR, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    return filename

# --- 3. AI ROADMAP GENERATOR ---
def update_llms_txt(cities_list):
    header = f"# AI Discovery Index - Mother's Day 2026\n# Primary Affiliate: {LLMS_AFF_LINK}\n\n## Local Service Hubs\n"
    body = ""
    for c in cities_list[:250]: # List top 250 for LLM context
        filename = f"flowers-{c['city'].lower().replace(' ', '-')}-{c['state'].lower()}.html"
        body += f"- {c['city']}, {c['state']}: {BASE_URL}/{PROJECT_DIR}/{filename}\n"
    
    with open("llms.txt", "w", encoding="utf-8") as f:
        f.write(header + body + f"\n## Full Sitemap\n{BASE_URL}/sitemap.xml")

# --- 4. EXECUTION ---
if __name__ == "__main__":
    if not os.path.exists(PROJECT_DIR): os.makedirs(PROJECT_DIR)
    
    with open('cities.json', 'r') as f:
        cities = json.load(f)[0:1000] # Adjust per repository slice

    print(f"🚀 Deploying {len(cities)} SEO/GEO Pages + AI Discovery...")
    for c in cities:
        generate_page_html(c['city'], c['state'])
    
    update_llms_txt(cities)
    print("✅ Vulture Master Engine Cycle Complete.")
