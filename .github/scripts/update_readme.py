import re

readme_path = "README.md"

with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find "Days off!: X months Y days" and increment days
match = re.search(r"Days off!:\s*(\d+)\s+months\s+(\d+)\s+days", content)
if match:
    months = int(match.group(1))
    days = int(match.group(2)) + 1

    # Handle rollover if days reach 30
    if days >= 30:
        days = 0
        months += 1

    new_line = f"Days off!: {months} months {days} days"
    content = re.sub(r"Days off!:\s*\d+\s+months\s+\d+\s+days", new_line, content)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("README updated!")
else:
    print("No 'Days off!' line found to update.")
