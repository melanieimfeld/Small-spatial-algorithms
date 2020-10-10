import random
import itertools
import time

#timer decorator
def timerfunc(func):
    def function_timer(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        print(f"The runtime for {func.__name__} took {runtime} seconds to find {value}")

        return value
    return function_timer

#create 4 random points. There is a small chance that we create duplicate points, therefore we'll add a set inbetween
def createPoints(n, width = 200, height = 200):
	return [*set([(random.randint(0,width), random.randint(0,height)) for i in range(n)]),]

#get distance between 2 points
def dist(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5

#total distance for each tour
def calcDist(points):
	#points.insert(0, startPoint)
	totalDist = sum([dist(points[i], points[i - 1]) for i in range(len(points))])
	return totalDist

#get tour with shortest distance from an array of tours
def shortest(points, p):
	print(p)
	return min(points, key = calcDist)

def find_nn(p, unvisited):
	return min(unvisited, key = lambda x: dist(x , p))

##### TSP brute force
@timerfunc
def tsp_brute(points):
	return f"shortest path: {shortest([points for points in itertools.permutations(points)], 1)}"

def find_nn(p, unvisited):
	return min(unvisited, key = lambda x: dist(x , p))

### TSP nearest neighbor
@timerfunc
def tsp_nn(points, startPoint):
	visited = [startPoint]
	unvisited = points
	unvisited.remove(startPoint)
	
	totalDist = 0

	while(len(unvisited) >= 1):
		nn = find_nn(visited[-1], unvisited)
		unvisited.remove(nn)
		visited.append(nn)
	return visited


inputs = createPoints(9)
print(inputs)

tsp_brute(inputs)
tsp_nn(inputs, inputs[0])
