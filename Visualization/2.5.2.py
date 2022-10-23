#坐标轴调整 xticks/yticks
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-np.pi,np.pi)
y=np.cos(x)
#生成x轴-pi到pi之间的5个坐标点，坐标字体大小设为15
plt.xticks(np.linspace(-np.pi, np.pi, 5), fontsize=15)
#生成y轴-1到1之间的5个坐标点
plt.yticks(np.linspace(-1, 1, 5), fontsize=15)
plt.plot(x,y,color='r')
plt.show()
