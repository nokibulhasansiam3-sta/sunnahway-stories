import json

with open('sahabider_jibon.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# সব stories এর জন্য highlight করা
for story_idx, story in enumerate(data):
    for para_idx, para in enumerate(story["paragraphs"]):
        # প্রথম paragraph skip (intro)
        if para_idx == 0:
            continue
        
        # যদি already bold না থাকে এবং colon থাকে
        if not para.startswith("**") and ":" in para:
            # প্রথম colon এর আগের অংশ bold করা
            parts = para.split(":", 1)
            # Check if it's not a Quran verse or Arabic text
            if not parts[0].strip().startswith(("قُ", "يَ", "وَ", "إِ", "لَ", "فَ", "مَ", "أَ", "تَ", "بِ", "عَ", "ثُ", "حَ", "خَ", "دَ", "ذَ", "رَ", "زَ", "سَ", "شَ", "صَ", "ضَ", "طَ", "ظَ", "غَ", "نَ", "هَ")):
                data[story_idx]["paragraphs"][para_idx] = f"**{parts[0]}:** {parts[1].strip()}"

with open('sahabider_jibon.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ {len(data)} টি story এর step গুলো highlight করা হয়েছে!")
