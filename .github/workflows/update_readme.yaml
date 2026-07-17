name: Daily README Update

on:
  schedule:
    - cron: "0 0 * * *"  # Every day at midnight UTC
  workflow_dispatch:      # Allow manual trigger too

permissions:
  contents: write   # allow pushing commits with GITHUB_TOKEN

jobs:
  update-readme:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"

      - name: Run update script
        run: python .github/scripts/update_readme.py

      - name: Commit and push if changed
        run: |
          git config user.name "VickySekhon"
          git config user.email "sekh4498@mylaurier.ca"
          git add README.md
          if git diff --staged --quiet; then
            echo "No changes to commit"
          else
            git commit -m "🔄 Daily increment of days off"
            git push
          fi
