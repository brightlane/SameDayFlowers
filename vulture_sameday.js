const fs = require('fs');
const path = require('path');

/** * VULTURE SAMEDAY: 10-Site Network Integration
 * Domain: SameDayFlowers
 */

// --- DATA FROM YOUR affiliate.json ---
const AFF_ID = "2013017799";
const BASE_URL = "https://www.floristone.com/main.cfm";
const OCCASION = "cm"; // Christmas/Current Setting
const DOMAIN = "https://brightlane.github.io/SameDayFlowers";

// --- THE NETWORK LINKS (YOUR OTHER 9 SITES) ---
const networkSites = [
    { name: "Mother's Day Flowers", url: "https://brightlane.github.io/MothersDayFlowers/" },
    { name: "Bouquet Flowers", url: "https://brightlane.github.io/BouquetFlowers/" },
    { name: "Valentine's Day Flowers", url: "https://brightlane.github.io/ValentinesDayFlowers/" },
    { name: "Send Flowers Online", url: "https://brightlane.github.io/SendFlowersOnline/" },
    { name: "Easter Flower Gifts", url: "https://brightlane.github.io/EasterFlowerGifts/" },
    { name: "Christmas Flowers", url: "https://brightlane.github.io/ChristmasFlowers/" },
    { name: "Flower Delivery", url: "https://brightlane.github.io/FlowerDelivery/" },
    { name: "Same Day Florist", url: "https://brightlane.github.io/SameDayFlorist/" },
    { name: "FTD Flowers Hub", url: "https://brightlane.github.io/FtdFlowers/" }
];

const baseCities = [
    "New York|NY|Manhattan", "Los Angeles|CA|Santa Monica", "Chicago|IL|The Loop", 
    "Houston|TX|Downtown", "Phoenix|AZ|Scottsdale", "Philadelphia|PA|Center City", 
    "San Antonio|TX|Riverwalk", "San Diego|CA|Gaslamp", "Dallas|TX|Uptown",
    "Toronto|ON|Financial District", "Montreal|QC|Old Port", "Vancouver|BC|Gastown"
];

const fullCityList = [];
for (let i = 0; i < 2000; i++) {
    fullCityList.push(baseCities[i % baseCities.length]);
}

const outputDir = path.join(__dirname, 'dist');
if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });

function generateSameDayNodes() {
    console.log("🚀 Generating 2,000 Linked Same-Day Nodes...");
    const isoDate = new Date().toISOString().split('T')[0];
    let sitemapEntries = [];

    // Pre-generate the backlink footer
    const backlinkHtml = networkSites.map(s => `<a href="${s.url}" style="color:#2ed573; text-decoration:none; margin:0 10px; font-size:0.75rem;">${s.name}</a>`).join(' | ');

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
        body { background: var(--bg); color: var(--text); font-family: sans-serif; text-align: center; margin:0; padding:0; }
        .emergency-banner { background: #ff4757; padding: 10px; font-weight: bold; }
        .hero { padding: 60px 20px; }
        .cta { display: inline-block; background: var(--accent); color: #000; padding: 20px 45px; border-radius: 50px; font-weight: 900; text-decoration: none; font-size: 1.4rem; margin-top:20px; }
        .network-footer { background: #11141d; padding: 30px 10px; margin-top: 60px; border-top: 1px solid #333; }
    </style>
</head>
<body>
    <div class="emergency-banner">🚨 2-HOUR ORDER WINDOW FOR SAME-DAY DELIVERY</div>
    
    <div class="hero">
        <h1>Same Day Flower Delivery <br> in ${name}, ${region}</h1>
        <p>Expert local florists delivering to <strong>${area}</strong> and the greater ${name} area.</p>
        <a href="${BASE_URL}?AffiliateID=${AFF_ID}&occ=${OCCASION}" class="cta">SEND SAME-DAY FLOWERS</a>
    </div>

    <div class="network-footer">
        <p style="font-size:0.8rem; color:#57606f; margin-bottom:10px;">Our Floral Partner Network:</p>
        ${backlinkHtml}
    </div>

    <footer style="padding:20px; color:#57606f; font-size:0.7rem;">Updated ${isoDate}</footer>
</body>
</html>`;

        fs.writeFileSync(path.join(outputDir, filename), html);
        sitemapEntries.push(`  <url><loc>${DOMAIN}/dist/${filename}</loc><lastmod>${isoDate}</lastmod></url>`);
    });

    const sitemapContent = `<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${sitemapEntries.join('\n')}</urlset>`;
    fs.writeFileSync(path.join(__dirname, 'sitemap.xml'), sitemapContent);
    console.log("✅ 2,000 Nodes and Sitemap generated for SameDayFlowers.");
}

generateSameDayNodes();
