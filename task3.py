import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LogLocator, LogFormatterSciNotation

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取Excel数据
df = pd.read_excel(r'D:\数据可视化实验\实验一\covid19_data.xls', sheet_name='current_prov')

# 查看列名，确保匹配实际数据（需根据实际调整）
print("数据列名：", df.columns.tolist())

# 按确诊人数降序排序后反转（确保确诊最多的在最上方）
top_provs = df.sort_values(by='confirm', ascending=False).iloc[::-1]  # 降序后反转
provinces = top_provs['province'].astype(str).tolist()

# 2. 创建子图（1行2列：直方图+横向条形图）
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))  # 调整画布宽度，适配横向条形图

# --------- 直方图：仅展示确诊人数分布（X轴对数刻度） ---------
# 准备确诊数据（供直方图使用，使用原始排序数据）
raw_conf_all = df['confirm'].fillna(0).astype(float).values
hist_conf = np.where(raw_conf_all <= 0, 1, raw_conf_all)  # 替换0/负数为1

# 生成对数尺度的bins（从10^0到确诊数据最大值的对数上限）
max_log = np.log10(hist_conf.max())
bins = np.logspace(0, max_log + 0.5, 15)  # 对数间距的bins

# 仅绘制确诊数据的直方图
ax1.hist(
    hist_conf,
    bins=bins,
    color='red',
    alpha=0.8,
    edgecolor='black',
    label='确诊'
)

# 设置X轴为对数刻度
ax1.set_xscale('log')
ax1.set_title('确诊人数分布直方图（X轴对数刻度）', fontsize=12)
ax1.set_xlabel('人数（对数刻度）')
ax1.set_ylabel('省份数量（计数）')
ax1.legend(title='数据类型')
ax1.grid(axis='y', alpha=0.3)
ax1.grid(axis='x', alpha=0.3, linestyle='--')  # 添加X轴网格

# --------- 横向条形图：确诊多的省份在最上方 ---------
y = np.arange(len(provinces))  # 省份位置（Y轴）
height = 0.25  # 横向柱子的高度（对应原宽度）

# 准备各指标数据（已反转顺序，确诊多的在上方）
raw_conf = top_provs['confirm'].fillna(0).astype(float).values
raw_dead = top_provs['dead'].fillna(0).astype(float).values
raw_heal = top_provs['heal'].fillna(0).astype(float).values
conf_vals = np.where(raw_conf <= 0, 1, raw_conf)
dead_vals = np.where(raw_dead <= 0, 1, raw_dead)
heal_vals = np.where(raw_heal <= 0, 1, raw_heal)

# 绘制横向条形图（barh替代bar，y轴位置调整）
bars1 = ax2.barh(y - height, conf_vals, height, label='确诊', color='red', alpha=0.8)
bars2 = ax2.barh(y, dead_vals, height, label='死亡', color='green', alpha=0.8)
bars3 = ax2.barh(y + height, heal_vals, height, label='治愈', color='blue', alpha=0.8)

# 美化横向条形图（X轴设为对数刻度）
ax2.set_title('各省疫情多指标对比（确诊人数多的省份在上）', fontsize=12)
ax2.set_ylabel('省份')  # Y轴为省份
ax2.set_xlabel('人数（对数刻度）')  # X轴为人数
ax2.set_yticks(y)
ax2.set_yticklabels(provinces)  # Y轴标签为反转后的省份名（确诊多的在上）
ax2.legend()
ax2.set_xscale('log')  # X轴设为对数刻度
# 主刻度使用以10为底的对数刻度
ax2.xaxis.set_major_locator(LogLocator(base=10.0))
ax2.xaxis.set_major_formatter(LogFormatterSciNotation())
ax2.grid(axis='x', which='major', alpha=0.3)

# 调整布局并显示
plt.tight_layout()
plt.show()