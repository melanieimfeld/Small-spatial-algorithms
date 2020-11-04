import spatialhelpers
from rtree import index

idx = index.Index()
cities = spatialhelpers.Cities(100)

@spatialhelpers.timerfunc
def insertPoints():
    for i,city in enumerate(cities):
        #print(i, city)
        idx.insert(i, (city[0],city[1]))

@spatialhelpers.timerfunc
def findPointsRtree(range):
    result = list(idx.intersection(range))
    return result


insertPoints()
findPointsRtree((0, 0, 100, 100))