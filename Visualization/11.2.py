#add_subplot
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212)
def create_plots():
    xs = range(10)
    ys = np.random.randint(0,9,10)
    return xs, ys
ax1.plot(create_plots()[0],create_plots()[1])
ax2.plot(create_plots()[0],create_plots()[1])
ax3.plot(create_plots()[0],create_plots()[1])
plt.show()
