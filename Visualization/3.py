#条形图
import matplotlib.pyplot as plt
plt.barh([1,3,5,7,9],[5,2,7,8,2], label="Example one")
plt.barh([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='g')
plt.legend()
plt.xlabel('bar height')
plt.ylabel('bar number ')
plt.title('Epic Graph\nAnother Line! Whoa')
plt.show()
