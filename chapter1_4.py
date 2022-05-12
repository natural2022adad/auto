#　日時関連の命令を使うときに宣言
from datetime import datetime

t = datetime.now()
fmt = t.strftime('%Y年%m月%d日　%H時%M分%S秒')
print(fmt)

yoteibi = datetime(2025, 4, 13)

delta = yoteibi - t
print(f'あと{delta.days+1}日です')

sleep_t = datetime(2022, 5,10,21,0,0)
wakeup_t = datetime(2022,5,11,5,30,0)

delta = wakeup_t - sleep_t
print(type(delta))
sec = delta.seconds
hours = sec / (60*60)
print(f'あと{hours}時間です')
