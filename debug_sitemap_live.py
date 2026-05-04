import os

path = "sitemap.xml"

print("🔍 Checking local sitemap...\n")

if not os.path.exists(path):
    print("❌ sitemap.xml does not exist locally")
else:
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()

    print("FIRST 200 CHARACTERS:\n")
    print(data[:200])

    print("\n--- ANALYSIS ---")

    if "<urlset" in data and "<loc>" in data:
        print("✅ Valid sitemap structure (local file is good)")
    elif data.strip().startswith("<!DOCTYPE html>"):
        print("❌ Local file is HTML, NOT XML (broken generator)")
    else:
        print("⚠️ Unknown format - likely corrupted or overwritten")
