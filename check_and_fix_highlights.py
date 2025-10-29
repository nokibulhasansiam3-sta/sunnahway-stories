import json
import re

def should_highlight(text):
    """Check if a paragraph should have highlighting"""
    # Don't highlight if it's already highlighted
    if text.startswith("**"):
        return False
    
    # Don't highlight Arabic text
    if re.search(r'[\u0600-\u06FF]', text.split(':')[0] if ':' in text else ''):
        return False
    
    # Don't highlight if it's just a regular sentence without a clear section marker
    if ':' not in text:
        return False
    
    # Check if it looks like a section header (short text before colon)
    parts = text.split(':', 1)
    if len(parts) == 2:
        header = parts[0].strip()
        # Only highlight if header is reasonably short (likely a section title)
        if len(header) < 100 and not header.startswith(('অর্থাৎ', 'অর্থ', 'মানে')):
            return True
    
    return False

def fix_highlights(filename):
    """Fix highlights in a JSON file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        changes = 0
        
        for story in data:
            if 'paragraphs' not in story:
                continue
                
            for i, para in enumerate(story['paragraphs']):
                # Skip first paragraph (usually intro)
                if i == 0:
                    continue
                
                if should_highlight(para):
                    parts = para.split(':', 1)
                    new_para = f"**{parts[0]}:** {parts[1].strip()}"
                    if new_para != para:
                        story['paragraphs'][i] = new_para
                        changes += 1
        
        if changes > 0:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"✅ {filename}: {changes} টি paragraph highlight করা হয়েছে")
        else:
            print(f"✓ {filename}: কোনো পরিবর্তন প্রয়োজন নেই")
        
        return changes
        
    except Exception as e:
        print(f"❌ {filename}: Error - {e}")
        return 0

# Check all files
files = [
    'sahabider_jibon.json',
    'nobider_jibon_theke.json',
    'jannat_jahannam.json',
    'dua_zikir.json',
    'fereshta_golpo.json',
    'tawba_golpo.json',
    'khulafa_jibon.json',
    'mujahid_jibon.json'
]

total_changes = 0
for filename in files:
    changes = fix_highlights(filename)
    total_changes += changes

print(f"\n🎉 মোট {total_changes} টি paragraph highlight করা হয়েছে!")
