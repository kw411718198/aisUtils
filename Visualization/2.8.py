#中文和字体
import matplotlib.pyplot as plt

x = range(1,13,1)
y = range(1,13,1)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.plot(x,y)
plt.title('中文测试')
plt.show()
