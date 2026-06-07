# -*- coding: utf-8 -*-
"""
Update spring-festival-guide/index.html for 四月廿三 (2026-06-08, 芒种第4天)
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

changes = []

# 1. Update header from 四月廿二 to 四月廿三
old_header = '<div class="header"><h1>🧧 四月廿二 · 芒种第三天 · 龙舟下水</h1>'
new_header = '<div class="header"><h1>🧧 四月廿三 · 芒种第四天 · 端午倒数</h1>'
if old_header in content:
    content = content.replace(old_header, new_header, 1)
    changes.append('Updated header: 四月廿二 -> 四月廿三 (芒种第四天)')
else:
    changes.append('WARNING: header 四月廿二 not found')

# 2. Update year subline
old_year = '<div class="year">2026 丙午马年 · 仲夏麦黄 · 端午临近</div>'
new_year = '<div class="year">2026 丙午马年 · 仲夏梅雨 · 端午倒数11天</div>'
if old_year in content:
    content = content.replace(old_year, new_year, 1)
    changes.append('Updated year: 端午临近 -> 端午倒数11天')
else:
    changes.append('WARNING: year subline not found')

# 3. Update "今日 · 四月廿二" -> "今日 · 四月廿三"
old_today = '<div class="card-title"><span class="icon">🧧</span>今日 · 四月廿二</div>'
new_today = '<div class="card-title"><span class="icon">🧧</span>今日 · 四月廿三</div>'
if old_today in content:
    content = content.replace(old_today, new_today, 1)
    changes.append('Updated today card title: 四月廿二 -> 四月廿三')
else:
    changes.append('WARNING: today card 四月廿二 not found')

# 4. Update update time stamp
m = re.search(r'最后更新[：:]\s*\d{1,2}[:：]\d{2}\s*·\s*\d{4}年\d{1,2}月\d{1,2}日', content)
new_time = '最后更新：06:31 · 2026年6月8日'
if m:
    content = content.replace(m.group(0), new_time, 1)
    changes.append(f'Updated time stamp (was: {m.group(0)})')
else:
    changes.append('WARNING: time stamp not found')

# 5. Update 今日 hot items to point to siyueershisan (4/23)
# Find the today card section by locating the new "今日 · 四月廿三" text
today_idx = content.find('今日 · 四月廿三')
if today_idx > 0:
    end_idx = content.find('<div class="card">', today_idx + 50)
    if end_idx > 0:
        today_section = content[today_idx:end_idx]
        new_today_section = today_section.replace("showDetail('siyueerer',", "showDetail('siyueershisan',")
        if new_today_section != today_section:
            content = content[:today_idx] + new_today_section + content[end_idx:]
            count = today_section.count("showDetail('siyueerer',")
            changes.append(f'Updated {count} hot items in today card: siyueerer -> siyueershisan')
        else:
            changes.append('WARNING: siyueerer not found in today card')
    else:
        changes.append('WARNING: end of today card not found')
else:
    changes.append('WARNING: today marker not found after replacement')

# 6. Add siyueershisan (四月廿三 / 芒种第四天) data to detailData - only if not already there
detail_has_siyueershisan = bool(re.search(r'^\s{8}siyueershisan:\{', content, re.MULTILINE))

# Find weibo position (insertion point - insert siyueershisan BEFORE weibo)
weibo_pos = content.find("weibo:{")
if weibo_pos < 0:
    changes.append('WARNING: could not find weibo position')
else:
    # Find the line start - look for the preceding newline + indent
    weibo_line_start = content.rfind('\n        weibo:{', 0, weibo_pos + 20)
    if weibo_line_start < 0:
        weibo_line_start = content.rfind('        weibo:{', 0, weibo_pos + 20)
    
    siyueershisan_data = '''siyueershisan:{
            1:{title:'🐛 收蚕结茧',tags:['四月廿三','芒种','蚕桑'],content:'<h3>🌍 地域</h3><p>江南蚕区（湖州、苏州、嘉兴）</p><h3>📍 地图</h3><div style="background:#f5f5f5;padding:15px;border-radius:8px;text-align:center;margin:10px 0;"><p style="color:#666;">🐛 江南蚕房·方格簇</p><p style="font-size:12px;color:#999;">采茧丰收蚕农忙</p></div><h3>📖 习俗介绍</h3><p>四月廿三芒种第四天，江南蚕区进入收茧高峰期。"春蚕到死丝方尽"，蚕农们将方格簇上结好的洁白蚕茧小心采下，按品级分装。湖州"辑里湖丝"、苏州"苏缎"原料皆出于此。新鲜蚕茧立即送往缫丝厂，民间有"芒种三天蚕，白茧堆成山"之说。</p><h3>🐛 收茧</h3><p>① 采方格簇<br>② 分级挑选<br>③ 通风晾干<br>④ 送缫丝厂</p>',comments:[{user:'湖州蚕农',text:'今年茧子又大又白',likes:'4.2万'},{user:'丝绸匠人',text:'辑里湖丝甲天下',likes:'3.5万'},{user:'文化学者',text:'丝绸之路源头在江南',likes:'2.9万'}]},
            2:{title:'🍶 浸梅煮酒',tags:['四月廿三','芒种','江南饮食'],content:'<h3>🌍 地域</h3><p>江南地区（江浙、皖南）</p><h3>📍 地图</h3><div style="background:#f5f5f5;padding:15px;border-radius:8px;text-align:center;margin:10px 0;"><p style="color:#666;">🍶 江南庭院·酒坛</p><p style="font-size:12px;color:#999;">青梅入酒初夏香</p></div><h3>📖 习俗介绍</h3><p>四月廿三芒种，正值江南梅雨季节前，青梅已黄熟，民间开始"浸梅煮酒"。选黄熟鲜梅洗净晾干，与冰糖一同浸入高度烧酒中，密封坛口，置于阴凉处三个月即成"梅子酒"。曹操"青梅煮酒论英雄"传为千古佳话。这一习俗延续千年，至今江南人家仍保留此风。</p><h3>🍶 制法</h3><p>① 选黄熟鲜梅<br>② 洗净晾干<br>③ 加冰糖浸酒<br>④ 密封三月</p>',comments:[{user:'江南人家',text:'梅子酒是夏天灵魂',likes:'4.4万'},{user:'酒文化研究者',text:'青梅煮酒论英雄',likes:'3.7万'},{user:'美食家',text:'自酿梅酒最香醇',likes:'3.0万'}]},
            3:{title:'🐟 晒鱼鲞',tags:['四月廿三','芒种','沿海'],content:'<h3>🌍 地域</h3><p>沿海地区（山东、福建、浙江、广东）</p><h3>📍 地图</h3><div style="background:#f5f5f5;padding:15px;border-radius:8px;text-align:center;margin:10px 0;"><p style="color:#666;">🐟 沿海渔村·晒场</p><p style="font-size:12px;color:#999;">烈日晒鱼鲞飘香</p></div><h3>📖 习俗介绍</h3><p>四月廿三芒种，沿海渔民进入晒鱼鲞旺季。此时黄鱼、带鱼丰收，渔民将鲜鱼开膛去脏，用盐略腌后铺在竹席上暴晒成鱼鲞，便于长期保存。浙江"黄鱼鲞"、福建"鳗鱼鲞"、山东"鮁鱼鲞"都享有盛名。芒种阳光猛烈，晒出的鱼鲞色泽金黄、肉质紧实，是沿海人家夏日的美味。</p><h3>🐟 晒法</h3><p>① 鲜鱼开膛<br>② 盐腌半日<br>③ 竹席暴晒<br>④ 翻晒三日</p>',comments:[{user:'沿海渔民',text:'鱼鲞配粥最香',likes:'3.9万'},{user:'浙江老饕',text:'黄鱼鲞蒸肉绝配',likes:'3.3万'},{user:'主妇',text:'夏天离不开鱼鲞',likes:'2.7万'}]},
            4:{title:'🌾 蒸新麦',tags:['四月廿三','芒种','北方'],content:'<h3>🌍 地域</h3><p>北方地区（河南、山东、陕西）</p><h3>📍 地图</h3><div style="background:#f5f5f5;padding:15px;border-radius:8px;text-align:center;margin:10px 0;"><p style="color:#666;">🌾 北方农家·灶台</p><p style="font-size:12px;color:#999;">新麦蒸糕谢丰年</p></div><h3>📖 习俗介绍</h3><p>四月廿三芒种，北方新麦登场，民间有"蒸新麦"习俗。农户将刚收割的麦子脱壳磨粉，蒸成麦糕或馒头，全家共食，称为"尝新"。新麦糕软糯香甜，散发着新麦特有的清香。这一习俗源于古代"荐新"礼：丰收后用新谷祭祖，再合家分享，感念天地恩德，祈愿五谷丰登。</p><h3>🌾 食俗</h3><p>① 新麦脱壳<br>② 磨粉成面<br>③ 上屉蒸糕<br>④ 全家尝新</p>',comments:[{user:'北方老人',text:'新麦糕最香甜',likes:'4.0万'},{user:'农妇',text:'蒸一锅全家分',likes:'3.4万'},{user:'文化传承者',text:'荐新礼仪不能丢',likes:'2.8万'}]},
            5:{title:'☂️ 修屋备漏',tags:['四月廿三','芒种','江南'],content:'<h3>🌍 地域</h3><p>江南地区（江浙、皖南、沪）</p><h3>📍 地图</h3><div style="background:#f5f5f5;padding:15px;border-radius:8px;text-align:center;margin:10px 0;"><p style="color:#666;">☂️ 江南老宅·屋檐</p><p style="font-size:12px;color:#999;">梅雨前修屋防漏</p></div><h3>📖 习俗介绍</h3><p>四月廿三芒种第四天，江南即将进入梅雨季节，民间有"修屋备漏"习俗。屋主在梅雨来临前抓紧检修房屋：检查瓦片是否破损、疏通屋檐天沟、修补漏雨墙面、更换朽木梁柱。江南老宅多为木质结构，潮湿天气易生霉腐朽，民间俗语"芒种修屋，三年不漏"。这一习俗体现了江南人未雨绸缪的生活智慧。</p><h3>☂️ 修缮</h3><p>① 检查瓦片<br>② 疏通天沟<br>③ 修补墙面<br>④ 更换朽木</p>',comments:[{user:'江南屋主',text:'梅雨前必查屋顶',likes:'3.6万'},{user:'老工匠',text:'修屋是老传统',likes:'3.0万'},{user:'江南主妇',text:'未雨绸缪最安心',likes:'2.4万'}]}
        },
        '''
    if weibo_line_start > 0:
        content = content[:weibo_line_start] + siyueershisan_data + content[weibo_line_start:]
        changes.append('Added siyueershisan (四月廿三 / 芒种第四天) to detailData')
    else:
        content = content[:weibo_pos] + siyueershisan_data + content[weibo_pos:]
        changes.append('Added siyueershisan (四月廿三 / 芒种第四天) to detailData (fallback insertion)')

# Report
print('Changes made:')
for c in changes:
    print(f'  - {c}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print()
print('Updated index.html for 四月廿三 / 芒种第四天 (2026-06-08)')
