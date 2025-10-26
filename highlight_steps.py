import json

with open('sahabider_jibon.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# আবু বকর - highlight করা
for i, para in enumerate(data[0]["paragraphs"]):
    if i == 0:
        continue  # প্রথম intro skip
    if not para.startswith("**"):
        # প্রথম শব্দগুলো bold করা
        if ":" in para:
            parts = para.split(":", 1)
            data[0]["paragraphs"][i] = f"**{parts[0]}:** {parts[1].strip()}"

# উমর - highlight করা  
for i, para in enumerate(data[1]["paragraphs"]):
    if i == 0:
        continue
    if not para.startswith("**"):
        if ":" in para:
            parts = para.split(":", 1)
            data[1]["paragraphs"][i] = f"**{parts[0]}:** {parts[1].strip()}"

with open('sahabider_jibon.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Step গুলো highlight করা হয়েছে!")
