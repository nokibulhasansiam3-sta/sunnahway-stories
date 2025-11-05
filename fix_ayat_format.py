#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Quranic ayat formatting in nobider_jiboni.json:
1. Add line breaks before and after Arabic ayats
2. Keep conversation style intact
"""

import json
import re

def fix_ayat_formatting(text):
    """Add line breaks before Arabic text and after translation"""
    
    # Pattern to match: text + Arabic + translation
    # Arabic text starts with common Arabic letters
    arabic_pattern = r'([:\n])([ا-ي۝ۖۚ\s]+)\n([^:\n][^\n]+\[সূরা[^\]]+\])'
    
    def replacer(match):
        prefix = match.group(1)
        arabic = match.group(2).strip()
        translation = match.group(3).strip()
        
        # Add line breaks
        return f'{prefix}\n\n{arabic}\n\n{translation}'
    
    result = re.sub(arabic_pattern, replacer, text)
    return result

# Read the JSON file
with open('nobider_jiboni.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Process each prophet's biography
for nabi in data:
    for i, para in enumerate(nabi['paragraphs']):
        # Fix ayat formatting
        nabi['paragraphs'][i] = fix_ayat_formatting(para)

# Write back
with open('nobider_jiboni.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Ayat formatting fixed!")
