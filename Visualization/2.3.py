#画布大小调整
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r'./unrate.csv')
plotData = data[0:12]
plt.figure(figsize=(50, 40))
plt.plot(plotData.DATE, plotData['VALUE'])
plt.title('Monthly Unemployment Trends, 1948')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate')
plt.show()  