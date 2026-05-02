import datetime, hashlib, os

AFF_BASE = "https://www.floristone.com/main.cfm?source_id=aff&AffiliateID=21885"
BASE_URL = "https://brightlane.github.io/SameDayFlowers"
today = datetime.date.today()
date_str = str(today)
year = today.year
seed = int(hashlib.md5(date_str.encode()).hexdigest()[:8], 16)

cities = [
    "New York","Los Angeles","Chicago","Houston","Phoenix","Philadelphia",
    "San Antonio","San Diego","Dallas","San Jose","Austin","Seattle",
    "Denver","Nashville","Miami","Atlanta","Tampa","Minneapolis",
    "Toronto","Montreal","Vancouver","Calgary","Edmonton","Ottawa",
    "Winnipeg","Boston","Portland","Las Vegas","Baltimore","Washington DC",
]

occasions = [
    {"name":"Same Day Mother's Day Flowers","slug":"same-day-mothers-day","tag":"md"},
    {"name":"Same Day Birthday Flowers",    "slug":"same-day-birthday",   "tag":"bd"},
    {"name":"Same Day Sympathy Flowers",    "slug":"same-day-sympathy",   "tag":"sy"},
    {"name":"Same Day Anniversary Flowers", "slug":"same-day-anniversary","tag":"an"},
    {"name":"Same Day Get Well Flowers",    "slug":"same-day-get-well",   "tag":"gw"},
    {"name":"Same Day Romance Flowers",     "slug":"same-day-romance",    "tag":"ro"},
    {"name":"Same Day Thank You Flowers",   "slug":"same-day-thank-you",  "tag":"ty"},
    {"name":"Same Day New Baby Flowers",    "slug":"same-day-new-baby",   "tag":"nb"},
]

titles = [
    "Order {occ} in {city} — Delivered Free Today {year}",
    "Best {occ} in {city} — Free Same-Day Delivery",
    "{occ} in {city} — No Hidden Fees, Free Delivery",
    "Last Minute {occ} in {city} — Still Delivered Today",
]

intros = [
    "Need {occ} delivered in {city} today? Floristone's local florist network guarantees same-day delivery across {city} — free delivery, $0 service fees, from $29.99.",
    "Send {occ} to {city} in 2 minutes. Floristone delivers same-day with free delivery and $0 hidden fees. 4.8 stars from 18,742 customers.",
    "Looking for {occ} in {city}? Floristone makes it simple — order now, same-day delivery, free, $0 fees, farm-fresh flowers guaranteed.",
    "The easiest way to get {occ} in {city} today — Floristone delivers same-day with free delivery and $0 service fees.",
]

city     = cities[seed % len(cities)]
occasion = occasions[(seed // 7) % len(occasions)]
title    = titles[(seed // 13) % len(titles)].format(occ=occasion["name"], city=city, year=year)
intro    = intros[(seed // 17) % len(intros)].format(occ=occasion["name"].lower(), city=city)
aff_link = f"{AFF_BASE}&occ={occasion['tag']}"
city_slug = city.lower().replace(" ", "-")
filename = f"blog/blog-{city_slug}-{occasion['slug']}-{date_str}.html"

os.makedirs("blog", exist_ok=True)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | SameDayFlowers</title>
    <meta name="description" content="Order {occasion['name'].lower()} in {city}. Free same-day delivery, $0 fees, from $29.99. 4.8 stars from 18,742 customers.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{BASE_URL}/{filename}">
    <script type="application/ld+json">
    {{"@context":"https://schema.org","@graph":[
      {{"@type":"Article","headline":"{title}","datePublished":"{date_str}","dateModified":"{date_str}","author":{{"@type":"Organization","name":"SameDayFlowers"}}}},
      {{"@type":"Product","name":"Floristone {occasion['name']} — {city}","offers":{{"@type":"Offer","priceCurrency":"USD","price":"29.99","availability":"https://schema.org/InStock","url":"{aff_link}","deliveryLeadTime":{{"@type":"QuantitativeValue","value":"0","unitCode":"DAY"}}}},"aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.8","reviewCount":"18742"}}}}
    ]}}
    </script>
    <style>
        :root{{--blue:#004b98;--blue-dk:#003c78;--bg:#f9f9ff;--border:#e6e6f0;--mid:#666;--gradient:linear-gradient(135deg,#004b98 0%,#e20613 100%);}}
        *{{box-sizing:border-box;margin:0;padding:0;}}
        body{{font-family:system-ui,sans-serif;background:var(--bg);color:#333;line-height:1.7;}}
        .nav{{background:#fff;padding:14px 5%;border-bottom:1px solid var(--border);font-weight:700;color:var(--blue-dk);display:flex;justify-content:space-between;align-items:center;}}
        .nav a{{font-size:0.85rem;color:var(--blue);text-decoration:none;}}
        .article{{max-width:760px;margin:0 auto;padding:50px 24px 80px;}}
        .eyebrow{{font-size:0.75rem;font-weight:700;color:var(--blue);letter-spacing:0.1em;text-transform:uppercase;margin-bottom:12px;display:block;}}
        h1{{font-size:clamp(1.8rem,4vw,2.5rem);color:#1a1a1a;margin-bottom:16px;line-height:1.2;}}
        .byline{{font-size:0.85rem;color:#999;margin-bottom:32px;border-bottom:1px solid var(--border);padding-bottom:16px;}}
        h2{{font-size:1.3rem;color:#1a1a1a;margin:32px 0 10px;}}
        p{{margin-bottom:16px;font-size:1rem;color:#444;}}
        .cta-box{{background:var(--gradient);color:#fff;text-align:center;padding:40px 24px;border-radius:16px;margin:40px 0;}}
        .cta-box h2{{color:#fff;margin:0 0 10px;font-size:1.5rem;}}
        .cta-box p{{color:rgba(255,255,255,0.88);margin-bottom:20px;}}
        .cta-btn{{background:#fff;color:var(--blue-dk);padding:14px 32px;border-radius:99px;font-weight:900;text-decoration:none;display:inline-block;font-size:1rem;}}
        .trust-row{{display:flex;justify-content:center;gap:16px;flex-wrap:wrap;margin-top:12px;}}
        .trust-row span{{font-size:0.75rem;color:rgba(255,255,255,0.8);font-weight:700;}}
        .faq-box{{background:#fff;border:1px solid var(--border);border-radius:12px;padding:24px;margin:32px 0;}}
        .faq-box strong{{display:block;color:#1a1a1a;margin-bottom:8px;}}
        .faq-box p{{margin:0;font-size:0.92rem;}}
        .back{{display:block;text-align:center;margin-top:32px;font-size:0.85rem;color:var(--blue);text-decoration:none;}}
        footer{{background:#111;color:#888;text-align:center;padding:24px;font-size:0.78rem;}}
    </style>
</head>
<body>
<nav class="nav">SameDayFlowers <a href="{BASE_URL}/">← Back to home</a></nav>
<article class="article">
    <span class="eyebrow">{occasion['name']} · {city} · {date_str}</span>
    <h1>{title}</h1>
    <p class="byline">SameDayFlowers · Same-day delivery in {city} · {date_str}</p>
    <p>{intro}</p>
    <h2>How to order {occasion['name'].lower()} in {city}</h2>
    <p>Order in 2 minutes. Choose your arrangement, add a card message, enter the delivery address in {city}, and checkout. Floristone's local florists in {city} cut flowers fresh and deliver same-day. Free delivery, $0 fees, live tracking included.</p>
    <h2>Why Floristone is the best same day flower delivery in {city}</h2>
    <p>4.8/5 stars from 18,742 verified customers. Free same-day delivery. $0 service fees. Local florists in {city} — no warehouse transit, no wilted stems. From $29.99 all-inclusive.</p>
    <div class="cta-box">
        <h2>Order {occasion['name']} in {city} Now</h2>
        <p>From $29.99 · Free delivery · $0 fees · 4.8★ from 18,742 customers</p>
        <a href="{aff_link}" class="cta-btn">🌷 Order Now</a>
        <div class="trust-row">
            <span>✓ FREE DELIVERY</span><span>✓ $0 FEES</span><span>✓ FARM FRESH</span><span>✓ LIVE TRACKING</span>
        </div>
    </div>
    <div class="faq-box">
        <strong>Q: Can I get {occasion['name'].lower()} delivered same-day in {city}?</strong>
        <p>Yes. Floristone guarantees same-day delivery across {city} with free delivery and $0 service fees. Order before the daily cutoff for guaranteed same-day arrival.</p>
    </div>
    <a href="{BASE_URL}/" class="back">← Browse all same day flowers</a>
</article>
<footer>This page contains affiliate links. We may earn a commission at no cost to you. © {year} SameDayFlowers</footer>
</body>
</html>"""

with open(filename, "w", encoding="utf-8") as f:
    f.write(html)

if os.path.exists("sitemap.xml"):
    with open("sitemap.xml", "r") as f:
        sm = f.read()
    entry = f'  <url><loc>{BASE_URL}/{filename}</loc><lastmod>{date_str}</lastmod><changefreq>never</changefreq><priority>0.7</priority></url>'
    if filename not in sm:
        sm = sm.replace("</urlset>", f"{entry}\n</urlset>")
        with open("sitemap.xml", "w") as f:
            f.write(sm)

print(f"Generated: {filename}")
print(f"City: {city} | Occasion: {occasion['name']}")
print(f"Affiliate ID: 21885 ✓")
