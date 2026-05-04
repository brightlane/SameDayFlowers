import os

PROJECT_DIR = "blog"  # change if your output folder is different


def check_build():
    print("\n🔍 Running Build Check...\n")

    # 1. Check directory
    if not os.path.exists(PROJECT_DIR):
        print(f"❌ Folder not found: {PROJECT_DIR}")
        print("👉 Your pages were NOT generated or saved elsewhere.")
        return

    # 2. Read files
    files = os.listdir(PROJECT_DIR)
    html_files = [f for f in files if f.endswith(".html")]

    # 3. Report
    print("📊 BUILD REPORT")
    print("----------------------")
    print("Total files:", len(files))
    print("HTML pages:", len(html_files))

    # 4. Status check
    if len(html_files) == 0:
        print("⚠️ No HTML pages found — generator likely failed.")
        return

    # 5. Sample output
    print("\n📄 Sample pages:")
    for f in html_files[:10]:
        print(" -", f)

    print("\n✅ Build check complete.")


if __name__ == "__main__":
    check_build()
