name: Vulture 10K Daily Blast
on:
  schedule:
    - cron: '0 0 * * *' # Runs every night at midnight
  workflow_dispatch:      # Allows you to run it manually for testing

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Run Generator
        run: python daily_blast.py
      - name: Commit & Push Pages
        run: |
          git config --global user.name 'brightlane-bot'
          git config --global user.email 'bot@brightlane.dev'
          git add blog/*.html
          git commit -m "Vulture Blast: 2000 Cities [${{ github.event.head_commit.timestamp }}]"
          git push
