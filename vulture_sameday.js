const fs = require('fs');
const path = require('path');

/**
 * VULTURE SAMEDAY FIXED PIPELINE
 * GitHub Pages Compatible
 */

const AFF_ID = "2013017799";
const BASE_URL = "https://www.floristone.com/main.cfm";
const OCCASION = "cm";
const DOMAIN = "https://brightlane.github.io/SameDayFlowers";

const OUTPUT_DIR = path.join(__dirname, 'blog'); // ✅ FIXED (was dist)
if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

const baseCities = [
    "New York|NY|Manhattan",
    "Los Angeles|CA|Santa Monica",
    "Chicago|IL|The Loop",
    "Houston|TX|Downtown",
    "Phoenix|AZ|Scottsdale"
];

const fullCityList = [];
for (let i = 0; i < 200; i++) {
    fullCityList.push(baseCities[i % baseCities.length]);
}

function generate() {
    console.log("🚀 Generating Pages (FIXED PIPELINE)");

    const date = new Date().toISOString().split('T')[0];
    let sitemap = [];

    fullCityList.forEach((entry, i) => {
        const [city, state, area] = entry.split('|');

        const filename = `flowers-${city.toLowerCase().replace(/\s+/g,'-')}-${state.toLowerCase()}.html`;

        const affLink =
            `${BASE_URL}?AffiliateID=${AFF_ID}&source_id=aff&occ=${OCCASION}`;

        const html = `
<!DOCTYPE html>
<html>
<head>
<title>Same Day Flowers in ${city}, ${state}</title>
</head>
<body style="font-family:sans-serif;text-align:center;padding:40px;">
<h1>Flowers in ${city}, ${state}</h1>

<p>Delivered same day to ${area}</p>

<a href="${affLink}"
style="background:#2ed573;color:#000;padding:20px 40px;
display:inline-block;text-decoration:none;font-weight:bold;">
ORDER FLOWERS NOW
</a>

</body>
</html>`;

        fs.writeFileSync(path.join(OUTPUT_DIR, filename), html);

        sitemap.push(`
  <url>
    <loc>${DOMAIN}/blog/${filename}</loc>
    <lastmod>${date}</lastmod>
  </url>`);
    });

    const sitemapXML =
`<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${sitemap.join('\n')}
</urlset>`;

    fs.writeFileSync(path.join(__dirname, 'sitemap.xml'), sitemapXML);

    console.log("✅ DONE: Pages + Sitemap fixed and GitHub-ready");
}

generate();
