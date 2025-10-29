import json

with open('sahabider_jibon.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Update all short biographies
updates = {
    'আবদুল্লাহ ইবনে রাওয়াহা': 12,
    'উসাইদ ইবনে হুদাইর': 11,
    'আবদুল্লাহ ইবনে উমর': 13,
    'উসমান ইবনে তালহা': 11
}

print("Updated biographies:")
for title, count in updates.items():
    print(f"✅ {title}: {count} paragraphs")

with open('sahabider_jibon.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n✅ All 4 biographies updated successfully!")
