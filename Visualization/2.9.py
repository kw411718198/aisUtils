#边框和水平线条
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
ax1.plot([1,2,3],[3,7,2],label = 'price', color= 'b')
#左边框设为青色
ax1.spines['left'].set_color('c')
#删除右、上边框
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
#让左边框变粗
ax1.spines['left'].set_linewidth(5)
#橙色的x轴数值
ax1.tick_params(axis='x', colors='#f06215')
#直接画一条水平线
ax1.axhline(5, color='y', linewidth=3)
plt.grid(True)
plt.show()
