#饼图
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 300 #提高图像分辨率
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # 0.1表示突出程度
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.show()

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # 0.1表示突出程度
colors = ['coral','yellowgreen','violet','deepskyblue']
wedges, texts, autotexts=plt.pie(sizes, colors=colors,explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
plt.legend(wedges, labels,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()

