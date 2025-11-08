import json
import re

# Read the file
with open('nobider_jiboni.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Function to check if a line is Arabic (ayat)
def is_arabic(text):
    # Check if text contains Arabic characters
    arabic_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]')
    return bool(arabic_pattern.search(text))

# Process each prophet
for prophet in data:
    if 'paragraphs' in prophet:
        new_paragraphs = []
        i = 0
        while i < len(prophet['paragraphs']):
            para = prophet['paragraphs'][i]
            
            # Check if this is an ayat (Arabic text)
            if is_arabic(para) and not para.startswith('অর্থ:') and not para.startswith('**'):
                # This is an ayat
                # Remove any existing ۝ at the end
                para = para.rstrip(' ۝')
                
                # Check if next paragraph is also an ayat (not translation)
                if i + 1 < len(prophet['paragraphs']):
                    next_para = prophet['paragraphs'][i + 1]
                    # If next is also ayat (not translation), add ۝ between them
                    if is_arabic(next_para) and not next_para.startswith('অর্থ:') and not next_para.startswith('**'):
                        para = para + ' ۝'
                
                new_paragraphs.append(para)
            else:
                new_paragraphs.append(para)
            
            i += 1
        
        prophet['paragraphs'] = new_paragraphs

# Write back
with open('nobider_jiboni.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Fixed all ayat with ۝ between consecutive ayats!")
