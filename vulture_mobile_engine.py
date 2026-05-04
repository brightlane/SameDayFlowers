import os
import json
import random

# --- CONFIGURATION ---
BASE_URL = "https://brightlane.github.io/FastFlowers"
AFFILIATE_ID = "2013017799"
MANYCHAT_LINK = f"https://m.me/brightlane?ref={AFFILIATE_ID}"

def generate_mobile_bridge(city, state):
    filename = f"get-{city.lower().replace(' ', '-')}.html"
    
    # Random "Social Proof" numbers for the Panic Window
    viewers = random.randint(45, 120)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Priority Dispatch: {city}</title>
    <style>
        body {{ font-family: -apple-system, sans-serif; background: #fff; margin: 0; display: flex; align-items: center; justify-content: center; height: 100vh; overflow: hidden; }}
        .bridge-container {{ width: 90%; text-align: center; border: 2px solid #000; padding: 30px 15px; border-radius: 20px; }}
        .status-dot {{ height: 10px; width: 10px; background: #22c55e; border-radius: 50%; display: inline-block; animation: pulse 1s infinite; }}
        @keyframes pulse {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.4; }} 100% {{ opacity: 1; }} }}
        h1 {{ font-size: 1.4rem; margin: 15px 0; }}
        .live-counter {{ font-size: 0.8rem; color: #ef4444; font-weight: bold; margin-bottom: 20px; }}
        .cta-mobile {{ background: #000; color: #fff; text-decoration: none; padding: 20px; display: block; border-radius: 12px; font-weight: bold; font-size: 1.1rem; text-transform: uppercase; }}
        .secure-lock {{ margin-top: 15px; font-size: 0.7rem; color: #9ca3af; }}
    </style>
</head>
<body>
    <div class="bridge-container">
        <div class="status-dot"></div> <span style="font-size: 0.8rem; font-weight: bold;">LIVE DISPATCH: {city.upper()}</span>
        <h1>Mother's Day Inventory Found</h1>
        <div class="live-counter">🔥 {viewers} others are looking at {city} florists right now.</div>
        
        <a href="{MANYCHAT_LINK}" class="cta-mobile">Claim Delivery Slot</a>
        
        <div class="secure-lock">🔒 Secured by ManyChat & FloristOne</div>
    </div>
</body>
</html>"""

    with open(f"now/{filename}", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    if not os.path.exists('now'): os.makedirs('now')
    with open('cities.json', 'r') as f:
        cities = json.load(f)[:2000] # Target Top 2000 Cities
    
    for c in cities:
        generate_mobile_bridge(c['city'], c['state'])
    print("🚀 Mobile Bridge Pages Generated in /now/")
