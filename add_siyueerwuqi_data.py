# -*- coding: utf-8 -*-
"""Add siyueerwuqi (四月廿七) data block with 5 customs to detailData"""
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if already added
if re.search(r'^\s{8}siyueerwuqi:\{', content, re.MULTILINE):
    print('siyueerwuqi already exists, skipping')
    sys.exit(0)

weibo_pos = content.find("        weibo:{")
if weibo_pos < 0:
    print('ERROR: weibo position not found')
    sys.exit(1)

# 5 customs for 四月廿七 / 芒种第八天 / 端午倒数7天 (2026-06-12)
data = '''        siyueerwuqi:{
            1:{title:'🪡 缝制香囊',tags:['四月廿七','芒种','端午'],content:'<h3>🌍 地域</h3><p>全国各地（江南、华北、西南尤盛）</p><h3>📍 地图</h3><div style="background:#f5f5f5;padding:15px;border-radius:8px;text-align:center;margin:10px 0;"><p style="color:#666;">🪡 端午香囊·五彩绣</p><p style="font-size:12px;color:#999;">艾叶雄黄绣囊中</p></div><h3>📖 习俗介绍</h3><p>四月廿七芒种第八天，端午倒数7天，民间进入"缝制香囊"高峰期。香囊用五色丝线绣成，内装艾叶、雄黄、苍术、白芷、丁香等中药材，挂于孩童腰间、系于床帐之上，据说能驱虫辟邪、预防暑湿。江南女子巧手绣"老虎头""五毒""粽子"等图案；华北多用"十二生肖"；西南少数民族则绣出图腾花纹。香囊小巧精致，是端午最具人气的节物之一。</p><h3>🪡 缝囊</h3><p>① 选五色丝<br>② 配中药材<br>③ 绣端午图<br>④ 挂于腰间</p>',comments:[{user:'苏州绣娘',text:'香囊手艺传了三代',likes:'4.5万'},{user:'杭州妈妈',text:'每年给孩子缝新香囊',likes:'3.8万'},{user:'民俗学者',text:'香囊是端午的符号',likes:'3.1万'}]},
            2:{title:'🌾 北方麦收扫尾',tags:['四月廿七','芒种','黄淮海'],content:'<h3>🌍 地域</h3><p>北方黄淮海平原（河南、山东、河北、苏北、皖北）</p><h3>📍 地图</h3><div style="background:#f5f5f5;padding:15px;border-radius:8px;text-align:center;margin:10px 0;"><p style="color:#666;">🌾 黄淮麦海·晾晒忙</p><p style="font-size:12px;color:#999;">麦场扫尾归仓储</p></div><h3>📖 习俗介绍</h3><p>四月廿七芒种第八天，北方麦收进入"扫尾"阶段。前期抢收的小麦含水率较高，需要趁晴好天气晾晒脱水。农人将新麦摊在麦场上，厚约寸许，每隔两小时翻动一次，让阳光均匀照射。水分降到13%以下时即可入仓储藏。豫东有"晒三晌"、鲁西南"晒麦不睡午觉"、皖北"麦不晒透不进仓"等说法。晾晒看似简单，实则是麦收最后一道关口，关乎一年口粮的品质。</p><h3>🌾 晾麦</h3><p>① 看天抢晴<br>② 摊薄翻动<br>③ 测水份<br>④ 干麦归仓</p>',comments:[{user:'豫东老农',text:'晒麦是麦收最后一关',likes:'4.3万'},{user:'鲁西农妇',text:'翻麦胳膊酸但心安',likes:'3.6万'},{user:'皖北粮农',text:'麦不晒透不敢进仓',likes:'2.9万'}]},
            3:{title:'🪷 西湖曲院风荷',tags:['四月廿七','芒种','杭州'],content:'<h3>🌍 地域</h3><p>浙江杭州西湖（曲院风荷景区）</p><h3>📍 地图</h3><div style="background:#f5f5f5;padding:15px;border-radius:8px;text-align:center;margin:10px 0;"><p style="color:#666;">🪷 曲院风荷·映日红</p><p style="font-size:12px;color:#999;">西湖十景六月天</p></div><h3>📖 习俗介绍</h3><p>四月廿七芒种后，杭州西湖"曲院风荷"迎来最佳观赏期。曲院原是南宋时酿造官酒的麯院，院内种植荷花，夏季清风徐来荷香与酒香交织，"麯院荷风"列西湖十景之一。清康熙帝南巡时手书"曲院风荷"四字立碑，从此名扬天下。如今景区内共有荷花300余种、30000+ 平米，6月中旬至7月上旬盛放。游人泛舟湖上、漫步九曲桥、品茗赏荷，是杭州夏日最具诗意的风物。</p><h3>🪷 赏荷</h3><p>① 曲院碑亭<br>② 九曲桥畔<br>③ 湖上泛舟<br>④ 荷茶品茗</p>',comments:[{user:'杭州市民',text:'六月必去曲院风荷',likes:'4.7万'},{user:'摄影爱好者',text:'清晨荷露最有意境',likes:'4.0万'},{user:'外地游客',text:'西湖十景之首名不虚传',likes:'3.4万'}]},
            4:{title:'🪢 劈竹编篮',tags:['四月廿七','芒种','端午'],content:'<h3>🌍 地域</h3><p>江南及西南地区（浙江、江西、湖南、四川、福建）</p><h3>📍 地图</h3><div style="background:#f5f5f5;padding:15px;border-radius:8px;text-align:center;margin:10px 0;"><p style="color:#666;">🪢 篾匠作坊·竹篮新</p><p style="font-size:12px;color:#999;">劈篾编篮备端阳</p></div><h3>📖 习俗介绍</h3><p>四月廿七芒种，端午倒数7天，江南篾匠进入一年中最忙时节。家家户户要编新竹篮、备粽篓、换蒸笼、晒匾盖。篾匠将毛竹劈成薄薄竹篾，编出"三眼篮""元宝篮""蒸笼架""粽子提篮"等各式器物。浙江嵊州、江西宜春、湖南益阳、四川道孚、福建武平都有百年篾匠世家。一只上好竹篮可用十年，是端午走亲访友、提粽送粽的必备容器。</p><h3>🪢 编织</h3><p>① 选三年竹<br>② 破竹劈篾<br>③ 起底编织<br>④ 收口提手</p>',comments:[{user:'嵊州篾匠',text:'端午前订单排满',likes:'4.2万'},{user:'宜春老艺人',text:'一根竹子七十二变',likes:'3.5万'},{user:'城市白领',text:'回乡买竹篮过端午',likes:'2.8万'}]},
            5:{title:'🐚 采海带',tags:['四月廿七','芒种','沿海'],content:'<h3>🌍 地域</h3><p>山东、福建、辽宁沿海（荣成、霞浦、长海、连江）</p><h3>📍 地图</h3><div style="background:#f5f5f5;padding:15px;border-radius:8px;text-align:center;margin:10px 0;"><p style="color:#666;">🐚 海上采收·海带丰</p><p style="font-size:12px;color:#999;">芒种旺汛海带黄</p></div><h3>📖 习俗介绍</h3><p>四月廿七芒种第八天，正是北方海域海带收获旺季。海带冬种春收，进入6月藻体厚实、含碘量达到峰值。山东荣成"中国海带之乡" 6月开启"海上麦收"，千艘渔船驶向养殖区，采收、晾晒、收储一气呵成。福建霞浦"紫菜海带之乡"滩涂上铺满新收海带，晒成"海带墙"成网红打卡地。一望无际的金色海带滩，是闽东最壮丽的海上农事景观。海带营养丰富，富含碘和褐藻胶，是沿海人家端午餐桌上的健康食材。</p><h3>🐚 采收</h3><p>① 看潮汛<br>② 海上采割<br>③ 滩涂晾晒<br>④ 打包入库</p>',comments:[{user:'荣成渔民',text:'海上麦收一年最忙',likes:'4.6万'},{user:'霞浦摄影师',text:'海带墙是夏天一景',likes:'3.9万'},{user:'沿海主妇',text:'端午煮海带汤最鲜',likes:'3.2万'}]}
        },
'''

new_content = content[:weibo_pos] + data + content[weibo_pos:]
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Added siyueerwuqi block (5 customs) before weibo')
print('File size: before/after:', len(content), '/', len(new_content), 'delta:', len(new_content) - len(content))
