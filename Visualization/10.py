#雷达图
import numpy as np
import matplotlib.pyplot as plt
# 中文和负号的正常显示
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
# 数据处理和准备
values = [98, 45, 124, 83, 90, 94] # 数值
labels = ['语文', '英语', '数学', '物理', '化学', '生物']  # 标签
# 设置雷达图的角度，用于平分切开一个圆面
angles = np.linspace(0, 2 * np.pi, len(values), endpoint=False)  # 角度
# 为了使雷达图一圈封闭起来，需要下面的步骤, 首尾相连
values = np.concatenate((values,[values[0]]))  
angles = np.concatenate((angles,[angles[0]]))  
labels = np.concatenate((labels,[labels[0]]))  
print('\n>>>', values, '\n>>>', angles)
# 绘图
fig = plt.figure()
''' 雷达图的核心 '''
# polar=True 这里一定要设置为极坐标格式
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, values, marker='o', color='r', linewidth=2)  # 绘制折线图
ax.fill(angles, values, color='b', alpha=0.25)  # 填充蓝色颜色
ax.set_thetagrids(angles * 180/np.pi, labels)  # 添加每个特征的标签
# 其他设置
ax.set_ylim(0,150)  # 设置雷达图的范围
plt.title('单个学生成绩展示')  # 添加标题
ax.grid(True)  # 添加网格线
plt.show()
