#图例、标题和标签
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r'./unrate.csv')
print(data.head())

plotData = data[0:12]
plt.plot(plotData.DATE,plotData['VALUE'], label = 'aa')
plt.title('Monthly Unemployment Trends, 1948')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate')
plt.legend(loc='upper left')
#将 X 轴刻度线标签旋转 45(60,90等) 度，这样它们就
#不会重叠,可以使用浮点或整数值指定旋转度。
plt.xticks(rotation=100)
plt.show()
