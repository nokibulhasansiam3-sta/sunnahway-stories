import json
import re

with open('itihasher_golpo.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Fix Musa and Khidir story - add quotes to translations
for item in data:
    if item['id'] == 'musa-o-khidir':
        new_paragraphs = []
        for para in item['paragraphs']:
            # Check if it's a translation line (starts with "অর্থ:")
            if para.startswith('অর্থ:'):
                # Add quotes around the translation part
                # Extract the translation and reference
                if '(সূরা' in para:
                    parts = para.split('(সূরা')
                    translation = parts[0].replace('অর্থ:', '').strip()
                    reference = '(সূরা' + parts[1]
                    new_para = f'অর্থ: \"{translation}\" {reference}'
                else:
                    translation = para.replace('অর্থ:', '').strip()
                    new_para = f'অর্থ: \"{translation}\"'
                new_paragraphs.append(new_para)
            else:
                new_paragraphs.append(para)
        
        item['paragraphs'] = new_paragraphs
        break

with open('itihasher_golpo.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('✅ Conversation line এ quotes যোগ করা হয়েছে!')
