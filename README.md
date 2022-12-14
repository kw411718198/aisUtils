# aisUtils

A tool package for MITS AIS users.

## Install

`pip install aisUtils`

## Develop

`git clone https://github.com/aisUtils.git`

## Usage

The package can satisfy fundamental demand for the use of AIS, which is  what I usually do. 

### Preprocessing

Suppose we start with AIS messages. We need to decode, crawl static information and perform filtering operations.

####  decoder

The decoder process requires the package—[libais](https://pypi.org/project/libais/).

Parameters include source file path, destination file path and original timestamp, no return value. If you want to decode multiple files, it is easy to use a loop outside the call. 

```python
from aisUtils import Preprocessing as pp
sourcePath = r'D:/data/2021-08-28_CST.txt' # source file path
desPath = r'D:/data/2021-08-28_output.csv' # destination file path
timestr = '2021-08-28:00:00:00;' # AIS initial timestamp

pp.decode(sourcePath, desPath, timestr)
```

#### crawl

If you need some static data such as length, ship type, crawl them from a mmsi list. Then you will get a static data table.

```python
from aisUtils import Preprocessing as pp

sourcePath = r'D:/python/data' # a directory stored all ais files
mmsiPath = r'D:/python/mmsiall.csv' # store mmsilist
staticDataPath = r'D:/python/staticData.csv' # store ais static data

# get the mmsilist
mmsiList = pp.getMmsiList(sourcePath)
# write the mmsilist
pp.writeMmsiList(mmsiPath, mmsiList)
# crawl
pp.crawl(mmsiPath, staticDataPath)
```

#### matching

Match the static data — length and ship type with the ais files.

```python
from aisUtils import Preprocessing as pp

staticDataPath  = r'D:/python/staticData.csv'
aisPath = r'D:/data/2021-08-28_output.csv'
desPath = r'D:/data/2021-08-28_matching.csv'

pp.match(staticDataPath, aisPath, desPath)
```

#### others

This part includes area, speed and ship type filtering.

```python
from aisUtils import Preprocessing as pp

sourcePath = r'D:/data/2021-08-28_matching.csv'
desPath = r'D:/data/2021-08-28_prep.csv'

max_Lon = 122.757
min_Lon = 122.145
max_Lat = 30.749
min_Lat = 30.409
speed = [2, 20]
shiptype_list = [6, 7, 8]

pp.filtering(sourcePath, desPath, max_Lon, min_Lon, max_Lat, min_Lat, speed, shiptype_list)
```

if you want to read the file, you can use the code block, which returns a array type.

```python
import pandas as pd
data = pd.read_csv(r'D:/data/2021-08-28_prep.csv')
data_p = data.values
#print(type(data_p)) #numpy.ndarray
```

### Interpolation

Package scipy has powerful statistical tools. [CSDN link](https://blog.csdn.net/weixin_45008173/article/details/107094422?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-0-107094422-blog-96724279.pc_relevant_sortByStrongTime&spm=1001.2101.3001.4242.1&utm_relevant_index=2)

```python
from scipy import interpolate as inter
from scipy.interpolate import lagrang
import numpy as np
# sort the data according the index
# data = data[np.lexsort((data[:,1], data[:,0]))]
xli = np.arange(0,constants.pi*2,0.1)   #   Interval points
yli = inter.interp1d(x,y,kind ="linear")(xli) # Linear interpolation
ycub = inter.interp1d(x,y,kind ="cubic")(xli) # Cubic spline interpolation
yquadratic = inter.interp1d(x,y,kind ="quadratic")(xli)     #  Quadratic spline interpolation
ynear = inter.interp1d(x,y,kind ="nearest")(xli) # Nearest neighbor interpolation

# Lagrange interpolation
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

poly = lagrange(x, y)   
length = len(x)
ylagrange = lagrangePoly(poly, xli, length)
```

### Calculation

#### Haversine

```python
from haversine import haversine
lyon=(45.7597,4.8422)# (lat, lon)
paris=(48.8567,2.3508)
haversine(lyon,paris)
```

#### scipy spatial

```python
from scipy.spatial.distance import cdist
cdist(x1, x2, metric = ' euclidean') # Euclidean distance
cdist(x1, x2, metric = 'minkowski')
cdist(x1, x2, metric = ' jaccard')
```



### Project

Some codes for project, including section flow statistics, ship types statistics and track point drawing.

## Description

Although I have created  many functions in the package according my own ideas, there are still many possible requirements that can be improved later. I am tired. Thanks to senior fellow apprentice Chunshen for supporting the development of the crawl function. 



*** 最后写依赖的时候整理一下