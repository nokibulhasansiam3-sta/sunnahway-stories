import json
import re

# যে files গুলো update করতে হবে
files = [
    'jannat_jahannam.json',
    'dua_zikir.json',
    'fereshta_golpo.json',
    'tawba_golpo.json',
    'khulafa_jibon.json',
    'mujahid_jibon.json'
]

def highlight_dialogues(text):
    """Highlight dialogues and important statements"""
    
    # Pattern 1: 'কথা বলল:' বা 'বললেন:' এর পরের অংশ
    patterns = [
        (r"বললেন:\s*'([^']+)'", r"বললেন: **'\1'**"),
        (r"বলল:\s*'([^']+)'", r"বলল: **'\1'**"),
        (r"বলেছেন:\s*'([^']+)'", r"বলেছেন: **'\1'**"),
        (r"বলেছিলেন:\s*'([^']+)'", r"বলেছিলেন: **'\1'**"),
        (r"জিজ্ঞাসা করলেন:\s*'([^']+)'", r"জিজ্ঞাসা করলেন: **'\1'**"),
        (r"জিজ্ঞাসা করল:\s*'([^']+)'", r"জিজ্ঞাসা করল: **'\1'**"),
        (r"উত্তর দিলেন:\s*'([^']+)'", r"উত্তর দিলেন: **'\1'**"),
        (r"উত্তর দেন:\s*'([^']+)'", r"উত্তর দেন: **'\1'**"),
        (r"ঘোষণা করলেন:\s*'([^']+)'", r"ঘোষণা করলেন: **'\1'**"),
    ]
    
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)
    
    return text

total_changes = 0

for filename in files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        file_changes = 0
        
        for story in data:
            for idx, para in enumerate(story['paragraphs']):
                new_para = highlight_dialogues(para)
                if new_para != para:
                    story['paragraphs'][idx] = new_para
                    file_changes += 1
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ {filename}: {file_changes} টি dialogue highlight করা হয়েছে")
        total_changes += file_changes
        
    except Exception as e:
        print(f"❌ {filename}: Error - {e}")

print(f"\n🎉 মোট {total_changes} টি dialogue highlight করা হয়েছে!")
