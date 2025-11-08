import json
import os
import re

# List of JSON files to process
json_files = [
    'itihasher_golpo.json',
    'ummahatul_mumineen.json',
    'sahabider_jibon_theke.json',
    'nobider_jibon_theke.json',
    'hadiser_golpo.json',
    'quraner_golpo.json',
    'fereshta_golpo.json',
    'tawba_golpo.json',
    'khulafa_jibon.json',
    'mohiyoshi_nari.json',
    'jannat_jahannam.json',
    'dua_zikir.json',
    'prachin_arob.json'
]

# Arabic characters to detect
arabic_pattern = re.compile(r'^[أإآاٱبتثجحخدذرزسشصضطظعغفقكلمنهويىئءؤةٰٓۖۗۚۛۜ۝ۣۢۤۥۦۧۨ۩۪ۭ۫۬\s]+')

def fix_bold_issue(data):
    """Fix bold issue in paragraphs where 'বললেন:' is followed by Arabic text"""
    fixed_count = 0
    
    if isinstance(data, list):
        for item in data:
            if 'paragraphs' in item and isinstance(item['paragraphs'], list):
                paragraphs = item['paragraphs']
                for i in range(len(paragraphs) - 1):
                    # Check if current paragraph ends with 'বললেন:' or similar patterns
                    current = paragraphs[i].strip()
                    next_para = paragraphs[i + 1].strip()
                    
                    # Check if next paragraph is Arabic text
                    if arabic_pattern.match(next_para):
                        # Check various patterns that might cause bold
                        patterns_to_fix = [
                            (r'বললেন:$', 'বললেন,'),
                            (r'বললেন:\s*$', 'বললেন,'),
                            (r'করলেন:$', 'করলেন,'),
                            (r'করলেন:\s*$', 'করলেন,'),
                            (r'দিলেন:$', 'দিলেন,'),
                            (r'দিলেন:\s*$', 'দিলেন,'),
                            (r'নিলেন:$', 'নিলেন,'),
                            (r'নিলেন:\s*$', 'নিলেন,'),
                            (r'হলেন:$', 'হলেন,'),
                            (r'হলেন:\s*$', 'হলেন,'),
                            (r'গেলেন:$', 'গেলেন,'),
                            (r'গেলেন:\s*$', 'গেলেন,'),
                            (r'এলেন:$', 'এলেন,'),
                            (r'এলেন:\s*$', 'এলেন,'),
                        ]
                        
                        for pattern, replacement in patterns_to_fix:
                            if re.search(pattern, current):
                                new_para = re.sub(pattern, replacement, current)
                                if new_para != current:
                                    paragraphs[i] = new_para
                                    fixed_count += 1
                                    break
    
    return fixed_count

# Process each file
total_fixed = 0
for filename in json_files:
    filepath = f'/Users/nasimulhasan/apps/sunnahway-golpo-jiboni/{filename}'
    
    if not os.path.exists(filepath):
        continue
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        fixed = fix_bold_issue(data)
        
        if fixed > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f'✅ {filename}: {fixed} টি ঠিক করা হয়েছে')
            total_fixed += fixed
        else:
            print(f'⚪ {filename}: কোনো সমস্যা নেই')
    
    except Exception as e:
        print(f'❌ {filename}: Error - {str(e)}')

print(f'\n🎉 মোট {total_fixed} টি bold issue ঠিক করা হয়েছে!')
