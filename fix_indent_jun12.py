# -*- coding: utf-8 -*-
"""Fix siyueerwuqi block indent (16 spaces -> 8 spaces for the block opener and 12 spaces for items should already be 12)"""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the siyueerwuqi block (starts with 16 spaces)
# The block opener should be 8 spaces, items 12 spaces, closer 8 spaces
# But the opener ended up at 16 spaces

# Find: "\n                siyueerwuqi:{" and replace with "\n        siyueerwuqi:{"
old_block_start = '\n                siyueerwuqi:{'
new_block_start = '\n        siyueerwuqi:{'
count = content.count(old_block_start)
print(f'Found {count} occurrences of 16-space siyueerwuqi: opener')
if count > 0:
    content = content.replace(old_block_start, new_block_start, 1)
    print('Fixed: siyueerwuqi: opener 16 spaces -> 8 spaces')

# Check if item indents are 16 spaces (they should be 12)
# items start with: "\n            N:{title:" (12 spaces) - but might be "\n                N:{title:" (16 spaces)
# Find the start of the block
pos = content.find('siyueerwuqi:{')
if pos > 0:
    # Find the closing
    depth = 0
    i = pos
    while i < len(content):
        c = content[i]
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                end = i + 1
                while end < len(content) and content[end] in ' \t\n':
                    end += 1
                if end < len(content) and content[end] == ',':
                    end += 1
                break
        i += 1
    block = content[pos:end]
    print(f'Block length: {len(block)}')
    # Find first item
    item_start_pat = re.compile(r'^\s+(\d):\{title:')
    matches = item_start_pat.findall(block, re.MULTILINE)
    print(f'Items found: {matches}')
    # Get indent of first item
    lines = block.split('\n')
    for ln in lines[:5]:
        if re.match(r'^\s+\d:\{title:', ln):
            n = len(ln) - len(ln.lstrip(' '))
            print(f'  Item line indent: {n} spaces: {ln[:50]!r}')
            break

# Save
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Saved')
