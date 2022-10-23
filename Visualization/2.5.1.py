#坐标轴调整xlim/ylim
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-5,5,0.1)
y=x**2
plt.xlim(-10,10)   #设置横坐标范围
plt.ylim(0,50)   #设置纵坐标范围
plt.xlabel('x',fontsize=15)  #设置横轴标识，并将字体大小设为15
plt.ylabel('y',fontsize=15)  #设置纵坐标标识
plt.title('Plot y=x^2',fontsize=15)  #设置图标题，不推荐使用
plt.plot(x,y)
plt.show()
