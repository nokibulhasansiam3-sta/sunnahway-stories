#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix ayat formatting to match sahabider_jibon.json exactly:
- Context ending with colon should be separate paragraph
- Arabic ayat should be separate paragraph
- Translation should be separate paragraph
"""

import json
import re

def fix_ayat_format(paragraphs):
    """Separate ayats properly like in sahabider_jibon"""
    new_paragraphs = []
    
    for para in paragraphs:
        # Check if paragraph has pattern: text:\nArabic
        if ':\n' in para and re.search(r'[ا-ي]', para):
            # Split at :\n
            parts = para.split(':\n', 1)
            if len(parts) == 2:
                context = parts[0] + ':'
                rest = parts[1]
                
                # Add context
                new_paragraphs.append(context)
                
                # Now split rest by lines
                lines = rest.split('\n')
                for line in lines:
                    line = line.strip()
                    if line:
                        new_paragraphs.append(line)
            else:
                new_paragraphs.append(para)
        else:
            new_paragraphs.append(para)
    
    return new_paragraphs

# Read the JSON file
with open('nobider_jiboni.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Process each prophet's biography
for nabi in data:
    nabi['paragraphs'] = fix_ayat_format(nabi['paragraphs'])

# Write back
with open('nobider_jiboni.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Ayat formatting fixed to match sahabider_jibon!")
