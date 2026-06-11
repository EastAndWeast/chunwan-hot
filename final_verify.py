# -*- coding: utf-8 -*-
"""Final verification: check JS syntax, count items, check file integrity"""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find detailData block
m = re.search(r'const detailData=\s*\{', content)
if not m:
    print('ERROR: detailData block not found')
    sys.exit(1)

# Find the matching closing brace
start = m.end() - 1  # position of {
depth = 0
i = start
while i < len(content):
    c = content[i]
    if c == '{':
        depth += 1
    elif c == '}':
        depth -= 1
        if depth == 0:
            end = i + 1
            break
    i += 1
data_block = content[start:end]
print(f'detailData block: {end-start} chars')

# Count opening and closing braces
n_open = data_block.count('{')
n_close = data_block.count('}')
print(f'Braces: {n_open} open / {n_close} close (delta {n_open-n_close})')
assert n_open == n_close, 'UNBALANCED BRACES'

# Try to evaluate the detailData as JavaScript-like structure
# Just check the key items
keys = re.findall(r'^\s{8,9}(\w+):\{$', data_block, re.MULTILINE)
print(f'detailData keys ({len(keys)}): {keys}')

# Verify siyueerwuqi is there
if 'siyueerwuqi' not in keys:
    print('ERROR: siyueerwuqi not found')
    sys.exit(1)
print('OK: siyueerwuqi in detailData')

# Count items in siyueerwuqi
pos = data_block.find('siyueerwuqi:{')
depth2 = 0
j = pos
while j < len(data_block):
    c = data_block[j]
    if c == '{':
        depth2 += 1
    elif c == '}':
        depth2 -= 1
        if depth2 == 0:
            block_end = j + 1
            break
    j += 1
siyue_block = data_block[pos:block_end]
n_items = len(re.findall(r'^\s{12}\d:\{', siyue_block, re.MULTILINE))
print(f'siyueerwuqi items: {n_items} (expect 5)')
assert n_items == 5, f'Expected 5 items, got {n_items}'

# Check the titles of the 5 items
titles = re.findall(r'^\s{12}\d:\{title:\'([^\']+)\'', siyue_block, re.MULTILINE)
print(f'siyueerwuqi 5 titles:')
for i, t in enumerate(titles, 1):
    print(f'  {i}. {t}')

# Check that the JS would be parseable
# Look for any common issues
print()
print('=== Spot checks ===')
# Comments: should have proper structure
n_with_comments = siyue_block.count('comments:[')
print(f'siyueerwuqi items with comments: {n_with_comments} (expect 5)')

# Each comment should have user, text, likes
n_likes = siyue_block.count('likes:')
print(f'Total likes fields: {n_likes} (expect 15 = 5 items x 3 comments)')

print()
print('=== Header check ===')
m = re.search(r'<div class="header"><h1>[^<]+</h1>', content)
print('Header:', m.group(0) if m else 'NOT FOUND')
m = re.search(r'<div class="year">[^<]+</div>', content)
print('Year:', m.group(0) if m else 'NOT FOUND')
m = re.search(r'<div class="card-title"><span class="icon">[^<]+</span>今日 · [^<]+</div>', content)
print('Today:', m.group(0) if m else 'NOT FOUND')
m = re.search(r'最后更新：\s*\d{1,2}[:：]\d{2}\s*·\s*\d{4}年\d{1,2}月\d{1,2}日', content)
print('Time:', m.group(0) if m else 'NOT FOUND')

print()
print('=== Hot items check ===')
m = re.search(r'今日 · [^<]+</div>(.+?)<div class="card-title"><span class="icon">', content, re.DOTALL)
if m:
    today = m.group(1)
    items = re.findall(r'<div class="hot-item" onclick="showDetail\(\'(\w+)\',(\d+)\)"><div class="rank rank-?\w*">\d+</div><div class="hot-content"><div class="hot-title">([^<]+)</div><div class="hot-desc">([^<]+)</div></div>', today)
    print(f'Found {len(items)} hot items:')
    for k, n, t, d in items:
        print(f'  {k}#{n}: {t} - {d}')

print()
print('=== File size ===')
import os
print(f'index.html: {os.path.getsize("index.html")} bytes')
print()
print('ALL CHECKS PASSED ✅' if n_items == 5 and 'siyueerwuqi' in keys and n_open == n_close else 'SOME CHECKS FAILED ❌')
