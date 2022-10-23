from haversine import haversine
lyon = (45.7597, 4.8422)
paris = (48.8567, 2.3508)
haversine(lyon, paris)

from scipy.spatial.distance import cdist
cdist(x1, x2, metric = ' euclidean') # Euclidean distance
cdist(x1, x2, metric = 'minkowski')
cdist(x1, x2, metric = ' jaccard')