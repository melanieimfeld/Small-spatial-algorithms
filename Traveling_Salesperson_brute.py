import random
import itertools
import numpy
import time

#measure performance
def performance(func, inputs):
	t1 = time.process_time()
	result = map(func, inputs)
	t2 = time.process_time()
	avg_time = (t2 - t1) / len(inputs)
	return (avg_time, list(result))


#create 4 random points. There is a small chance that we create duplicate points, therefore we'll add a set inbetween
def createPoints(n, width = 200, height = 200):
	return [*set([(random.randint(0,width), random.randint(0,height)) for i in range(n)]),]

#get distance between 2 points
def dist(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5

#total distance for each permutation
def calcDist(points, startPoint):
	points.insert(0, startPoint)
	totalDist = sum([dist(points[i], startPoint) if i == len(points)-1 else dist(points[i], points[i + 1]) for i in range(len(points))])
	return totalDist

##### TSP brute force
def tsp_brute(points):
	startPoint = points[0]
	print(points)
	points.remove(startPoint)
	return (min([calcDist(list(points), startPoint) for points in itertools.permutations(points)]))

inputs = createPoints(6)

#print(performance(tsp_brute, inputs))

print(tsp_brute(inputs))
