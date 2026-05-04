AFFILIATE_URL = "https://www.floristone.com/main.cfm?AffiliateID=2013017799&source_id=brightlane"

def build_page(city, state, body_content, blog_content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Same-Day Flowers in {city}, {state}</title>

  <style>
    body {{
      font-family: Arial, sans-serif;
      background: #0a0b10;
      color: white;
      margin: 0;
      padding: 0;
    }}

    .hero {{
      padding: 80px 20px;
      text-align: center;
    }}

    .cta {{
      display: inline-block;
      margin-top: 20px;
      padding: 18px 40px;
      background: #ff4757;
      color: white;
      text-decoration: none;
      border-radius: 50px;
      font-weight: bold;
    }}

    .section {{
      max-width: 900px;
      margin: auto;
      padding: 40px 20px;
      color: #a4b0be;
    }}

    h1, h2 {{
      color: white;
    }}

    footer {{
      text-align: center;
      padding: 40px;
      font-size: 0.8rem;
      color: #57606f;
      border-top: 1px solid #1a1c23;
      margin-top: 60px;
    }}
  </style>
</head>

<body>

  <!-- HERO (shared) -->
  <div class="hero">
    <h1>Same-Day Flower Delivery in {city}</h1>
    <p>Fresh bouquets delivered locally in {city}, {state}</p>

    <a class="cta" href="{AFFILIATE_URL}">
      Order Flowers Now
    </a>
  </div>

  <!-- CITY CONTENT -->
  <div class="section">
    {body_content}
  </div>

  <!-- BLOG CONTENT (ALWAYS APPENDED) -->
  <div class="section">
    <h2>Flower Delivery Guide</h2>
    {blog_content}
  </div>

  <!-- FOOTER -->
  <footer>
    © 2026 SameDayFlowers · Affiliate ID 2013017799
  </footer>

</body>
</html>"""
