import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

# 1. 读取Excel数据（假设data_history是工作表名，日期列名为'日期'，数据列是'confirm','dead','heal'）
df = pd.read_excel('your_data.xlsx', sheet_name='data_history')  # 替换为你的Excel路径
df['日期'] = pd.to_datetime(df['日期'])  # 确保日期列是datetime格式

# 2. 绘制折线图
plt.figure(figsize=(12, 6))
# 绘制确诊、死亡、治愈数据折线，区分颜色和样式
plt.plot(df['日期'], df['confirm'], label='确诊', color='red', linestyle='-', marker='o', markersize=3)
plt.plot(df['日期'], df['dead'], label='死亡', color='black', linestyle='--', marker='s', markersize=3)
plt.plot(df['日期'], df['heal'], label='治愈', color='green', linestyle='-.', marker='^', markersize=3)

# 坐标轴处理
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # 日期格式
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))    # 每月显示刻度
plt.xticks(rotation=45)  # 日期标签旋转45度避免重叠
plt.yticks(range(0, int(df[['confirm', 'dead', 'heal']].max().max()) + 10000, 10000))  # y轴刻度间隔

plt.title('新冠疫情趋势折线图')
plt.xlabel('日期')
plt.ylabel('人数')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()  # 调整布局
plt.show()

# 3. 绘制散点图
plt.figure(figsize=(12, 6))
# 绘制散点，区分颜色和标记
plt.scatter(df['日期'], df['confirm'], label='确诊', color='red', marker='o', s=10)
plt.scatter(df['日期'], df['dead'], label='死亡', color='black', marker='s', s=10)
plt.scatter(df['日期'], df['heal'], label='治愈', color='green', marker='^', s=10)

# 坐标轴处理（同折线图）
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
plt.xticks(rotation=45)
plt.yticks(range(0, int(df[['confirm', 'dead', 'heal']].max().max()) + 10000, 10000))

plt.title('新冠疫情数据散点图')
plt.xlabel('日期')
plt.ylabel('人数')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()