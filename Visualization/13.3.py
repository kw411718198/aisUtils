#三维曲面

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
x=np.linspace(-7.5,7.5)
y=np.linspace(-7.5,7.5)
X,Y=np.meshgrid(x,y)
A=np.sqrt(X**2+Y**2)
Z=np.sin(A)/A
#创建3d图形
fig=plt.figure()
ax=Axes3D(fig)
#绘制三维曲面,使用彩虹色
ax.plot_surface(X,Y,Z,cmap=plt.get_cmap('rainbow'))
plt.show()
