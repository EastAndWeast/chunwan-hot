# -*- coding: utf-8 -*-
"""
Fix the today card section to use clean (non-corrupted) text labels
for 2026-06-08 (四月廿三 / 芒种第四天)
Robust version: doesn't rely on icon char (which may be PUA/corrupted)
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the today card section by matching the date pattern 今日 · 四月廿二 (which is still old)
# The today card is between this title and the next <div class="card">
pattern = r'(<div class="card-title"><span class="icon">[^<]+</span>今日 · 四月廿二</div>)(.*?)(<div class="card">)'
m = re.search(pattern, content, re.DOTALL)

if not m:
    print('ERROR: today card (with 四月廿二) not found', file=sys.stderr)
    sys.exit(1)

print(f'Found today card (old title 四月廿二) at offset {m.start()}-{m.end()}', file=sys.stderr)

# Build clean today card body with proper text labels
new_today_body = '''
            <div class="hot-item" onclick="showDetail('siyueershisan',1)"><div class="rank rank-1">1</div><div class="hot-content"><div class="hot-title">🐛 收蚕结茧</div><div class="hot-desc">江南蚕区采茧忙，辑里湖丝甲天下</div></div><span class="click-hint">›</span></div>
            <div class="hot-item" onclick="showDetail('siyueershisan',2)"><div class="rank rank-2">2</div><div class="hot-content"><div class="hot-title">🍶 浸梅煮酒</div><div class="hot-desc">青梅入酒三伏香，江南人家夏日魂</div></div><span class="click-hint">›</span></div>
            <div class="hot-item" onclick="showDetail('siyueershisan',3)"><div class="rank rank-3">3</div><div class="hot-content"><div class="hot-title">🐟 晒鱼鲞</div><div class="hot-desc">沿海晒鱼鲞飘香，烈日竹席色金黄</div></div><span class="click-hint">›</span></div>
            <div class="hot-item" onclick="showDetail('siyueershisan',4)"><div class="rank rank-other">4</div><div class="hot-content"><div class="hot-title">🌾 蒸新麦</div><div class="hot-desc">新麦登场蒸麦糕，荐新尝谢丰收年</div></div><span class="click-hint">›</span></div>
            <div class="hot-item" onclick="showDetail('siyueershisan',5)"><div class="rank rank-other">5</div><div class="hot-content"><div class="hot-title">☂️ 修屋备漏</div><div class="hot-desc">梅雨前修屋防漏，未雨绸缪江南智</div></div><span class="click-hint">›</span></div>
        </div>
        '''

# Replace
new_section = m.group(1).replace('四月廿二', '四月廿三') + new_today_body + m.group(3)
content = content[:m.start()] + new_section + content[m.end():]

# Verify no PUA chars in the new section
pua_count = len(re.findall(r'[\uE000-\uF8FF]', new_section))
print(f'PUA chars in new today card: {pua_count}', file=sys.stderr)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Today card section rebuilt with clean text for 四月廿三 / 芒种第四天')
