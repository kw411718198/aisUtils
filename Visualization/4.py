#直方图

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801) #将随机种子固定
mu = 100
sigma = 15
x = mu + sigma * np.random.randn(437)
num_bins = 50
n, bins, patches = plt.hist(x, num_bins, density=1)
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
plt.plot(bins, y, '--')
plt.xlabel('Smarts')
plt.ylabel('Probability density')
plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$') #表示字符串不用转意
plt.tight_layout() # 调整显示间距
plt.show()
