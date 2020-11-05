import spatialhelpers
from rtree import index


print(__name__)

idx = index.Index()
cities = spatialhelpers.Cities(1000)

@spatialhelpers.timerfunc
def insertPoints():
    for i,city in enumerate(cities):
        #print(i, city)
        idx.insert(i, (city[0],city[1]))

@spatialhelpers.timerfunc
def findPointsRtree(range):
    result = list(idx.intersection(range))
    return result

for i in range(10):
	insertPoints()
	findPointsRtree((50, 50, 50, 50))


#print(cities)