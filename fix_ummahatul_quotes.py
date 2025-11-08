import json
import re

with open('ummahatul_mumineen.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Function to add quotes to conversation-style text
def fix_paragraph(para):
    # Skip if it's already an Arabic text or starts with certain patterns
    if para.strip().startswith(('أ', 'إ', 'و', 'ك', 'ل', 'ف', 'ت', 'م', 'ب', 'ع', 'ن', 'ق', 'ي', 'ه', 'ج', 'خ', 'ح', 'ش', 'ص', 'ض', 'ط', 'ظ', 'غ', 'ذ', 'د', 'ر', 'ز', 'س', 'ث')):
        return para
    
    # Check if it starts with "অর্থ:" or "অর্থাৎ,"
    if para.startswith('অর্থ:') or para.startswith('অর্থাৎ,'):
        # Check if already has quotes
        if '\"' in para:
            return para
        
        # Add quotes
        if '(সূরা' in para or '[সূরা' in para or '[সহীহ' in para:
            # Split at reference
            match = re.search(r'(\[সূরা|\(সূরা|\[সহীহ)', para)
            if match:
                pos = match.start()
                text_part = para[:pos].strip()
                ref_part = para[pos:].strip()
                
                # Extract the prefix (অর্থ: or অর্থাৎ,)
                if text_part.startswith('অর্থ:'):
                    prefix = 'অর্থ:'
                    translation = text_part[5:].strip()
                elif text_part.startswith('অর্থাৎ,'):
                    prefix = 'অর্থাৎ,'
                    translation = text_part[6:].strip()
                else:
                    return para
                
                return f'{prefix} \"{translation}\" {ref_part}'
        else:
            # No reference, just add quotes
            if para.startswith('অর্থ:'):
                translation = para[5:].strip()
                return f'অর্থ: \"{translation}\"'
            elif para.startswith('অর্থাৎ,'):
                translation = para[6:].strip()
                return f'অর্থাৎ, \"{translation}\"'
    
    return para

# Fix all items
for item in data:
    new_paragraphs = []
    for para in item['paragraphs']:
        new_paragraphs.append(fix_paragraph(para))
    item['paragraphs'] = new_paragraphs

with open('ummahatul_mumineen.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('✅ Ummahatul Mumineen এ conversation style এ quotes যোগ করা হয়েছে!')
