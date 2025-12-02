import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

# 读取Excel数据
df = pd.read_excel('D:/数据可视化实验/实验一/covid19_data.xls', sheet_name='data_history')
df['日期'] = pd.to_datetime(df['date'])  


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)  

# 折线图 -
ax1.plot(df['日期'], df['confirm'], label='确诊', color='red', linestyle='-', marker='o', markersize=3)
ax1.plot(df['日期'], df['dead'], label='死亡', color='black', linestyle='-', marker='s', markersize=3)
ax1.plot(df['日期'], df['heal'], label='治愈', color='green', linestyle='-', marker='^', markersize=3)

ax1.set_title('新冠疫情趋势折线图')
ax1.set_ylabel('人数')
ax1.legend()
ax1.grid(alpha=0.3)
ax1.yaxis.set_ticks(range(0, int(df[['confirm', 'dead', 'heal']].max().max()) + 10000, 10000))

# 散点图 
ax2.scatter(df['日期'], df['confirm'], label='确诊', color='red', marker='o', s=10)
ax2.scatter(df['日期'], df['dead'], label='死亡', color='black', marker='s', s=10)
ax2.scatter(df['日期'], df['heal'], label='治愈', color='green', marker='^', s=10)

ax2.set_title('新冠疫情数据散点图')
ax2.set_xlabel('日期')
ax2.set_ylabel('人数')
ax2.legend()
ax2.grid(alpha=0.3)
ax2.yaxis.set_ticks(range(0, int(df[['confirm', 'dead', 'heal']].max().max()) + 10000, 10000))

# 统一设置x轴格式
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax2.xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)  # 旋转x轴标签避免重叠

# 调整子图间距
plt.tight_layout()
plt.show()