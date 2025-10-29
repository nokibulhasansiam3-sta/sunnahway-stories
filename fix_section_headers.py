import json
import re

def fix_section_headers(filename):
    """Fix section headers that should be highlighted"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        changes = 0
        
        for story in data:
            if 'paragraphs' not in story:
                continue
                
            for i, para in enumerate(story['paragraphs']):
                # Skip if already highlighted
                if para.startswith('**'):
                    continue
                
                # Check if paragraph contains standalone section headers (not part of sentence)
                # Pattern: Text followed by \n\nSection Header\n\n
                if '\n\n' in para:
                    parts = para.split('\n\n')
                    new_parts = []
                    modified = False
                    
                    for part in parts:
                        part = part.strip()
                        if not part:
                            continue
                        
                        # Check if this looks like a section header
                        # Criteria: Short text (< 100 chars), no punctuation at end, not starting with number
                        if (len(part) < 100 and 
                            not part.endswith(('.', '।', '!', '?', '"', "'")) and
                            not part[0].isdigit() and
                            not part.startswith(('অর্থাৎ', 'অর্থ', 'মানে', 'তিনি', 'রাসূল', 'হযরত', 'আল্লাহ')) and
                            not re.search(r'[\u0600-\u06FF]', part)):  # Not Arabic
                            
                            # This looks like a section header
                            new_parts.append(f'**{part}**')
                            modified = True
                        else:
                            new_parts.append(part)
                    
                    if modified:
                        story['paragraphs'][i] = '\n\n'.join(new_parts)
                        changes += 1
        
        if changes > 0:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"✅ {filename}: {changes} টি paragraph এ section headers highlight করা হয়েছে")
        else:
            print(f"✓ {filename}: কোনো পরিবর্তন প্রয়োজন নেই")
        
        return changes
        
    except Exception as e:
        print(f"❌ {filename}: Error - {e}")
        return 0

# Fix sahabider_jibon.json
changes = fix_section_headers('sahabider_jibon.json')
print(f"\n🎉 মোট {changes} টি paragraph ঠিক করা হয়েছে!")
