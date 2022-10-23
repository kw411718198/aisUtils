### 引入库函数
import numpy as np 
from scipy import interpolate as inter
from scipy.interpolate import lagrange  #   拉格朗日插值库函数

import matplotlib.pyplot as plt
from scipy import constants

def lagrangePoly(poly, x, length):
    result = []
    for i in range(len(x)):
        subresult = 0
        for j in range(length):
            subresult += poly[j] * (x[i] ** j)
        result.append(subresult)
    return result

x = np.linspace(0,constants.pi*2,4)
y = np.cos(x**2/3+4)
xli = np.arange(0,constants.pi*2,0.1)   #   定义插值间隔点
fli = inter.interp1d(x,y,kind ="linear")    #   线性插值
yli = fli(xli)
ycub = inter.interp1d(x,y,kind ="cubic")(xli)   #   三次样条插值
ynear = inter.interp1d(x,y,kind ="nearest")(xli)    #   最近邻插值
yquadratic = inter.interp1d(x,y,kind ="quadratic")(xli)     #   二次样条插值
#   拉格朗日插值
poly = lagrange(x, y)   #   系数拟合
length = len(x)
ylagrange = lagrangePoly(poly, xli, length)   #   序列求解

#   多维插值见__init__文件链接

plt.plot(x,y,'o',xli,yli,'-')
plt.plot(xli,ycub,':',xli,ynear,'--',xli,yquadratic,'+', xli, ylagrange, '*')
plt.legend(['data','linear','cubic','nearest','quadratic','lagrange'],loc='best')
plt.show()