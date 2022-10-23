#添加文字说明
import numpy as np
import matplotlib.pyplot as plt

plt.plot(np.random.random(30).cumsum(), color='k', linestyle='dashed', marker='^')
plt.text(5, 10, r'$\mu=100,\ \sigma=15$')
plt.show()
