#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add bold formatting to headings in nobider_jiboni.json
Pattern: "Heading: content" -> "**Heading:** content"
"""

import json
import re

with open('nobider_jiboni.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for nabi in data:
    new_paragraphs = []
    
    for para in nabi['paragraphs']:
        # Skip if already bold or if it's Arabic or translation
        if para.startswith('**') or re.search(r'^[ا-ي]', para) or para.startswith("'") or para.startswith('"'):
            new_paragraphs.append(para)
            continue
        
        # Check if paragraph starts with a heading pattern
        # Pattern: "Word word word: Content..."
        match = re.match(r'^([^:]+):\s+(.+)$', para, re.DOTALL)
        
        if match:
            heading = match.group(1).strip()
            content = match.group(2).strip()
            
            # Check if heading is short (likely a real heading, not a quote)
            # And doesn't contain certain words that indicate it's a quote
            if (len(heading) < 80 and 
                not any(word in heading for word in ['বললেন', 'বলল', 'বলেছেন', 'জিজ্ঞাসা করলেন', 'বললাম'])):
                # Make it bold
                new_paragraphs.append(f'**{heading}:** {content}')
            else:
                new_paragraphs.append(para)
        else:
            new_paragraphs.append(para)
    
    nabi['paragraphs'] = new_paragraphs

with open('nobider_jiboni.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('✅ Added bold formatting to headings!')
