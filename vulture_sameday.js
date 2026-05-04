const fs = require('fs');
const path = require('path');

// --- DATA FROM YOUR affiliate.json ---
const AFF_ID = "2013017799";
const BASE_URL = "https://www.floristone.com/main.cfm";
const OCCASION = "cm"; // From your JSON params

const DOMAIN = "https://brightlane.github.io/SameDayFlowers";

// Hyperlocal Database
const baseCities = [
    "New York|NY|Manhattan", "Los Angeles|CA|Santa Monica", "Chicago|IL|The Loop", 
    "Houston|TX|Downtown", "Phoenix|AZ|Scottsdale", "Philadelphia|PA|Center City", 
    "San Antonio|TX|Riverwalk", "San Diego|CA|Gaslamp", "Dallas|TX|Uptown"
];

const fullCityList = [];
for (let i = 0; i < 2000; i++) {
    fullCityList.push(baseCities[i % baseCities.length]);
}

const outputDir = path.join(__dirname, 'dist');
if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });

function generateSameDayNodes() {
    console.log("🚀 Generating 2,000 Same-Day Delivery Nodes...");
    const isoDate = new Date().toISOString().split('T')[0];
    let sitemapEntries = [];

    fullCityList.forEach((entry, index) => {
        const [name, region, area] = entry.split('|');
        const filename = `same-day-delivery-${name.toLowerCase().replace(/\s+/g, '-')}-${index}.html`;
        
        const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Same Day Flower Delivery in ${name}, ${region} | Fast Local Florist</title>
    <style>
        :root { --accent: #2ed573; --bg: #0a0b10; --text: #f1f2f6; }
        body { background: var(--bg); color: var(--text); font-family: sans-serif; text-align: center; padding: 50px 20px; }
        .emergency-banner { background: #ff4757; padding: 10px; font-weight: bold; position: fixed; top: 0; width: 100%; left: 0; }
        .card { background: #11141d; padding: 40px; border-radius: 15px; max-width: 600px; margin: 40px auto; border: 1px solid #1e272e; }
        .cta { display: inline-block; background: var(--accent); color: #000; padding: 20px 40px; border-radius: 50px; font-weight: 900; text-decoration: none; font-size: 1.5rem; animation: pulse 2s infinite; }
        @keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.05); } 100% { transform: scale(1); } }
    </style>
</head>
<body>
    <div class="emergency-banner">🚨 ORDER WITHIN 2 HOURS FOR SAME-DAY DELIVERY</div>
    <div class="card">
        <h1>Same Day Delivery <br> in ${name}, ${region}</h1>
        <p>Fresh bouquets hand-delivered to <strong>${area}</strong> and surrounding zip codes today.</p>
        <a href="${BASE_URL}?AffiliateID=${AFF_ID}&occ=${OCCASION}" class="cta">SEND FLOWERS NOW</a>
    </div>
    <footer style="color:#57606f; font-size:0.8rem;">© 2026 Same Day Flowers Network | Updated ${isoDate}</footer>
</body>
</html>`;

        fs.writeFileSync(path.join(outputDir, filename), html);
        sitemapEntries.push(`  <url><loc>${DOMAIN}/dist/${filename}</loc><lastmod>${isoDate}</lastmod></url>`);
    });

    fs.writeFileSync(path.join(__dirname, 'sitemap.xml'), `<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${sitemapEntries.join('\n')}</urlset>`);
}

generateSameDayNodes();
