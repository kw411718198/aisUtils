#非线性尺度
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)
# 生成(0,1)之间的数据
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))
plt.plot(x, y)
#调整y轴刻度为log，也可
#使用symmetric log，logit等
plt.yscale('log') 
plt.title('log')
plt.grid(True)
plt.show()
