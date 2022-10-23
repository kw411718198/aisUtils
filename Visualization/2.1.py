#plot函数
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2 * np.pi, 0.01)
y = np.sin(x)

plt.plot(x, y, 'b')
plt.show()