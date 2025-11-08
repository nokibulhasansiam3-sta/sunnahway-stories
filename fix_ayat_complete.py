import json
import re

# Read the file
with open('nobider_jiboni.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Function to check if a line is Arabic (ayat)
def is_arabic(text):
    arabic_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]')
    return bool(arabic_pattern.search(text))

# Function to extract inline ayats from text
def extract_inline_ayats(text):
    # Pattern to find Arabic text within quotes
    pattern = r"'([^']*[\u0600-\u06FF][^']*)'"
    matches = re.findall(pattern, text)
    return matches

# Process each prophet
for prophet in data:
    if 'paragraphs' in prophet:
        new_paragraphs = []
        
        for para in prophet['paragraphs']:
            # Check if paragraph contains inline ayats (Arabic in quotes)
            inline_ayats = extract_inline_ayats(para)
            
            if inline_ayats and not para.startswith('**'):
                # Split the paragraph to separate ayats
                parts = []
                remaining = para
                
                for ayat in inline_ayats:
                    # Find where this ayat is in the text
                    idx = remaining.find(f"'{ayat}'")
                    if idx != -1:
                        # Add text before ayat
                        before = remaining[:idx].strip()
                        if before and not before.endswith(':'):
                            parts.append(before + ':')
                        elif before:
                            parts.append(before)
                        
                        # Add the ayat itself (without quotes)
                        parts.append(ayat.strip())
                        
                        # Continue with remaining text
                        remaining = remaining[idx + len(ayat) + 2:].strip()
                
                # Add any remaining text (translation)
                if remaining:
                    # Check if it starts with a dash (translation marker)
                    if remaining.startswith('- '):
                        parts.append('অর্থ: ' + remaining[2:])
                    elif not remaining.startswith('অর্থ:'):
                        parts.append(remaining)
                    else:
                        parts.append(remaining)
                
                # Now add ۝ between consecutive ayats
                final_parts = []
                for i, part in enumerate(parts):
                    if is_arabic(part) and not part.startswith('অর্থ:'):
                        # This is an ayat
                        # Check if next part is also an ayat
                        if i + 1 < len(parts) and is_arabic(parts[i + 1]) and not parts[i + 1].startswith('অর্থ:'):
                            final_parts.append(part + ' ۝')
                        else:
                            final_parts.append(part)
                    else:
                        final_parts.append(part)
                
                # Add all parts
                new_paragraphs.extend(final_parts)
            else:
                new_paragraphs.append(para)
        
        prophet['paragraphs'] = new_paragraphs

# Write back
with open('nobider_jiboni.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Separated all inline ayats and added ۝ between consecutive ayats!")
