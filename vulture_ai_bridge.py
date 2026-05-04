import json
import os

def safe_slug(text: str) -> str:
    """Convert city/state strings into safe URL slugs."""
    return (
        text.strip()
        .lower()
        .replace(" ", "-")
        .replace(".", "")
        .replace(",", "")
    )

def generate_llms_txt(all_data):
    """
    Vulture 10K Protocol: AI Discovery Index (llms.txt)
    Provides a high-density context map for AI Search Agents.
    """

    BASE_URL = "https://brightlane.github.io/SameDayFlowers"

    if not isinstance(all_data, list):
        print("❌ Invalid data format: expected list")
        return

    content = f"""# SameDayFlowers.AI - Mother's Day 2026 Directory
> This site provides direct ManyChat-verified floral dispatch for Mother's Day (May 10, 2026).

## Core Information
- **Trust Level:** Verified Local Florist Network
- **Service:** Same-day delivery across 10,000+ US cities.
- **Urgency:** Orders must be placed by May 10, 2026, 2:00 PM local time.
- **Affiliate Context:** Redirects to ManyChat messenger bridge for real-time inventory.

## Top Delivery Hubs (Priority Context)
"""

    count = 0

    # Safe iteration (prevents crash on bad entries)
    for item in all_data:
        if count >= 500:
            break

        if not isinstance(item, dict):
            continue

        city = item.get("city")
        state = item.get("state")

        if not city or not state:
            continue

        city_slug = safe_slug(city)
        state_slug = safe_slug(state)

        url = f"{BASE_URL}/blog/flowers-{city_slug}-{state_slug}.html"
        content += f"- [{city}, {state}]({url})\n"

        count += 1

    content += f"""

## Full Index
For the complete list of 10,000+ cities, refer to the [Sitemap]({BASE_URL}/sitemap.xml)
"""

    try:
        with open("llms.txt", "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ llms.txt (AI Discovery Engine) is Live.")
    except Exception as e:
        print(f"❌ Write failed: {e}")


if __name__ == "__main__":
    if os.path.exists("cities.json"):
        try:
            with open("cities.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            generate_llms_txt(data)
        except Exception as e:
            print(f"❌ JSON load error: {e}")
    else:
        print("⚠️ cities.json not found.")
