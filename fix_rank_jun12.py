# -*- coding: utf-8 -*-
"""Fix duplicate 'rank' class in today card hot items (rank rank rank-1 -> rank rank-1)"""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

fixes = [
    ('class="rank rank rank-1"',     'class="rank rank-1"'),
    ('class="rank rank rank-2"',     'class="rank rank-2"'),
    ('class="rank rank rank-3"',     'class="rank rank-3"'),
    ('class="rank rank rank-other"', 'class="rank rank-other"'),
]

total = 0
for old, new in fixes:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f'Fixed {count}x: {old} -> {new}')
        total += count

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print(f'Total fixes: {total}')
