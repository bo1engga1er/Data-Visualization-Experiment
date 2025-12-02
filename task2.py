import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_excel(r'D:\数据可视化实验\实验一\covid19_data.xls', sheet_name='data_world')

# 筛选确诊前4国家并按确诊人数降序排序（确保顺序）

top4_countries = df.sort_values(by='confirm', ascending=False).head(4).reset_index(drop=True)

# 定义指标和样式
indicators = ['confirm', 'dead', 'heal', 'suspect']  # 替换为实际列名
labels = ['确诊', '死亡', '治愈', '疑似']
colors = ['red', 'green', 'blue', 'orange']

# 自定义百分比显示函数（占比<1.5%时不显示百分比）
def autopct_filter(pct):
    return f'{pct:.1f}%' if pct >= 1.5 else ''

# 5. 绘制子图（2x2布局，顺时针映射索引：0→左上,1→右上,3→右下,2→左下）
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes_flat = axes.flatten()  # 扁平化索引：[0(左上),1(右上),2(左下),3(右下)]
# 顺时针排序的子图索引映射（确诊从高到低对应：左上→右上→右下→左下）
clockwise_indices = [0, 1, 3, 2]

for i, country_idx in enumerate(clockwise_indices):
    # 获取对应确诊排名的国家数据（i=0→第1名, i=1→第2名, i=2→第3名, i=3→第4名）
    row = top4_countries.iloc[i]
    country_name = row['country']  # 替换为实际国家列名
    
    # 处理缺失值并转换为数值类型
    values = []
    for ind in indicators:
        val = row[ind] if pd.notna(row[ind]) else 0
        values.append(float(val) if val != '' else 0)
    
    # 绘制饼图（使用顺时针映射的子图索引）
    ax = axes_flat[country_idx]
    # 按数值大小排序（降序），并按顺时针方向绘制（largest first clockwise）
    paired = list(zip(values, labels, colors))
    paired_sorted = sorted(paired, key=lambda x: x[0], reverse=True)
    sorted_values, sorted_labels, sorted_colors = zip(*paired_sorted)

    wedges, texts, autotexts = ax.pie(
        sorted_values,
        colors=sorted_colors,
        autopct=autopct_filter,  # 过滤更小占比的标签
        startangle=90,           # 从顶部开始
        counterclock=False,      # 顺时针方向绘制
        pctdistance=0.75,        # 百分比文本更靠近圆心，减少重叠
        textprops={'fontsize': 8}
    )
    
    for text in texts:
        text.set_visible(False)
    
    # 添加图例
    # 图例使用排序后的标签对应排序后的楔形
    ax.legend(
        wedges, sorted_labels,
        title="数据类型",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
        fontsize=10
    )
    
    # 美化百分比文本（更小字体+居中）
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_weight('bold')
        autotext.set_fontsize(8)
        autotext.set_horizontalalignment('center')
    
    ax.set_title(f'{country_name}疫情数据构成', fontsize=12, pad=15)
    ax.axis('equal')  # 保证饼图正圆

# 调整布局
plt.suptitle('确诊人数前4国家疫情数据构成饼图（顺时针排序）', fontsize=16, y=1.02)
plt.tight_layout()
plt.subplots_adjust(right=0.85)
plt.show()