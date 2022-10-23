#文本注释
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

plt.plot(np.random.random(30).cumsum(), color='k', linestyle='dashed', marker='^')
plt.annotate('local max', xy=(15, 8), xytext=(8, 12),
            arrowprops=dict(facecolor='r', shrink=0.05))
plt.show()

style.use('ggplot')   #设置背景样式
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0)) #画子图，这里只有一个子图
ax1.plot([1,2,3],[3,7,2],label = 'price')
ax1.plot([3,7,2],[1,2,3],label = 'price2')
font_dict = {'family':'serif', 'color':'darkred', 'size':15}#使用ax1.text添加文本，坐标为（4，4）
#使用fontdict参数添加一个数据字典，来使用所用的字体。 
#在我们的字体字典中，我们将字体更改为serif，颜色为『深红色』，然后将字体大小更改为 15。
ax1.text(4, 4,'Text Example(4,4)', fontdict=font_dict)
#用另一种方式进行注解,xytext为比例
ax1.annotate('2nd annotation',(2.9,2.9), xytext=(0.4, 0.6), textcoords='axes fraction',
arrowprops = dict(facecolor='white',color='grey'))
plt.legend()
plt.show()
