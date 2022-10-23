#散点图
import numpy as np
import matplotlib.pyplot as plt
n=100
#生成n行2列的数据
x=np.random.randn(n,2)
#第一列作为x轴，第二列作为y轴
plt.scatter(x[:,0],x[:,1])
plt.show()

plt.figure(figsize=(9,6))
n=1000
#rand 均匀分布和 randn高斯分布
x=np.random.randn(1,n)
y=np.random.randn(1,n)
T=np.arctan2(x,y)
plt.scatter(x,y,c=T,s=25,alpha=0.4,marker='o')
#T:散点的颜色
#s：散点的大小
#alpha:透明程度
plt.show()

#泡泡图
np.random.seed(19680801)
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

