#线条类型、网格线控制
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,2*np.pi,0.2)
#宽度为2的蓝色实线条
plt.plot(x,np.sin(x),linewidth=2,color='b') 
#宽度为2的红色虚线条，*标记每个数据点
plt.plot(x,np.cos(x),linewidth=1,color='r',linestyle='--',marker='*')
#显示网格
plt.grid(True)
#显示图形
plt.show()
