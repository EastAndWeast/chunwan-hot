# -*- coding: utf-8 -*-
"""Update spring-festival-guide/index.html for 四月廿七 (2026-06-12, 芒种第八天, 端午倒数7天)"""
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

changes = []

# 1. Header
m = re.search(r'<div class="header"><h1>[^<]*四月廿五 · 芒种第六天 · 端午倒数</h1>', content)
new_header = '<div class="header"><h1>🧧 四月廿七 · 芒种第八天 · 端午倒数</h1>'
if m:
    content = content[:m.start()] + new_header + content[m.end():]
    changes.append('Header: 四月廿五 芒种第六天 -> 四月廿七 芒种第八天')
else:
    changes.append('WARNING: header not found')

# 2. Year subline
old_year = '<div class="year">2026 丙午马年 · 仲夏梅雨 · 端午倒数9天</div>'
new_year = '<div class="year">2026 丙午马年 · 仲夏梅雨 · 端午倒数7天</div>'
if old_year in content:
    content = content.replace(old_year, new_year, 1)
    changes.append('Year: 端午倒数9天 -> 端午倒数7天')
else:
    changes.append('WARNING: year subline not found')

# 3. Today card title
old_today_pattern = r'(<div class="card-title"><span class="icon">[^<]+</span>今日 · )四月廿五(</div>)'
m = re.search(old_today_pattern, content)
if m:
    content = content[:m.start()] + m.group(1) + '四月廿七' + m.group(2) + content[m.end():]
    changes.append('Today card: 四月廿五 -> 四月廿七')
else:
    changes.append('WARNING: today card not found')

# 4. Time stamp
m = re.search(r'最后更新：\s*\d{1,2}[:：]\d{2}\s*·\s*\d{4}年\d{1,2}月\d{1,2}日', content)
new_time = '最后更新：06:31 · 2026年6月12日'
if m:
    content = content.replace(m.group(0), new_time, 1)
    changes.append(f'Time stamp: {m.group(0)} -> 06:31 6/12')
else:
    changes.append('WARNING: time stamp not found')

# 5. Update today card 5 hot items
new_hot_items = [
    (1, 'rank rank-1',     '🪡 缝制香囊',     '艾叶雄黄入囊中，端午倒数7天忙备节'),
    (2, 'rank rank-2',     '🌾 北方麦收扫尾', '黄淮海平原麦场晾晒，归仓一夏心安'),
    (3, 'rank rank-3',     '🪷 西湖曲院风荷', '六月西湖赏荷盛，十景之首映日红'),
    (4, 'rank rank-other', '🪢 劈竹编篮',     '劈篾编篮备盛粽，端午倒计时七天'),
    (5, 'rank rank-other', '🐚 采海带',       '芒种旺汛海带丰，山东福建沿海忙'),
]

today_idx = content.find('今日 · 四月廿七')
if today_idx < 0:
    changes.append('ERROR: today marker not found')
else:
    end_idx = content.find('<div class="card-title"><span class="icon">', today_idx + 50)
    if end_idx < 0:
        changes.append('ERROR: end of today card not found')
    else:
        today_section = content[today_idx:end_idx]
        new_today_section = today_section
        for n, rank_cls, title, desc in new_hot_items:
            old_pat = r'<div class="hot-item" onclick="showDetail\(\'siyueerwuwu\',' + str(n) + r'\)"><div class="rank [^"]+">\d+</div><div class="hot-content"><div class="hot-title">[^<]+</div><div class="hot-desc">[^<]+</div></div><span class="click-hint">›</span></div>'
            new_str = f'<div class="hot-item" onclick="showDetail(\'siyueerwuqi\',{n})"><div class="rank {rank_cls}">{n}</div><div class="hot-content"><div class="hot-title">{title}</div><div class="hot-desc">{desc}</div></div><span class="click-hint">›</span></div>'
            new_today_section2 = re.sub(old_pat, new_str, new_today_section, count=1)
            if new_today_section2 == new_today_section:
                changes.append(f'WARNING: hot item {n} not found')
            else:
                new_today_section = new_today_section2
        if new_today_section != today_section:
            content = content[:today_idx] + new_today_section + content[end_idx:]
            changes.append('Hot items: titles+onclick siyueerwuwu->siyueerwuqi')

# Save
print('Changes:')
for c in changes:
    print(f'  - {c}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Saved (header/year/today/time/hot items only; siyueerwuqi data will be added in step 2)')
