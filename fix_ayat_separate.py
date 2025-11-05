#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Separate Arabic ayats and translations into separate paragraphs
like in sahabider_jibon.json
"""

import json
import re

def separate_ayat_paragraphs(paragraphs):
    """Separate ayats into individual paragraphs"""
    new_paragraphs = []
    
    for para in paragraphs:
        # Check if paragraph contains Arabic text
        if re.search(r'[ا-ي]', para):
            # Split by newlines
            lines = para.split('\n')
            current_text = []
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                    
                # Check if line is Arabic
                is_arabic = bool(re.search(r'^[ا-ي۝ۖۚ\s،؛]+$', line))
                
                # Check if line is translation (starts with Bengali and has [সূরা])
                is_translation = '[সূরা' in line and not is_arabic
                
                if is_arabic or is_translation:
                    # Save accumulated text first
                    if current_text:
                        new_paragraphs.append('\n'.join(current_text))
                        current_text = []
                    # Add Arabic/translation as separate paragraph
                    new_paragraphs.append(line)
                else:
                    # Accumulate regular text
                    current_text.append(line)
            
            # Add remaining text
            if current_text:
                new_paragraphs.append('\n'.join(current_text))
        else:
            # No Arabic, keep as is
            new_paragraphs.append(para)
    
    return new_paragraphs

# Read the JSON file
with open('nobider_jiboni.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Process each prophet's biography
for nabi in data:
    nabi['paragraphs'] = separate_ayat_paragraphs(nabi['paragraphs'])

# Write back
with open('nobider_jiboni.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Ayats separated into individual paragraphs!")
