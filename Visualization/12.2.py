#多个子图共享x轴
import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0.01, 10.0, 0.01)
data1 = np.sin(np.pi*t) 
data2 = np.sin(2 * np.pi * t)
data3=np.cos(2*np.pi*t)
data4=np.cos(2.5*np.pi*t)
fig,ax=plt.subplots(2, 2, sharex='col')#设置sharex参数为True或者all或者col来实现
#分别绘制四个子图空间的图形
ax1=ax[0,0]
ax1.plot(t,data1)
ax2=ax[0,1]
ax2.plot(t,data2)
ax3=ax[1,0]
ax3.plot(t,data3)
ax4=ax[1,1]
ax4.plot(t,data4)
plt.show()
