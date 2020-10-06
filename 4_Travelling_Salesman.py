import random
import itertools
import numpy


numPoints = 4
points = []

#create 4 random points
for i in range(numPoints):
	points.append([random.randint(0,5), random.randint(0,5)])

#total distance for each permutation
def calcDist(points):
	totalDist = sum([dist(points[i], points[0]) if i == len(points)-1 else dist(points[i], points[i + 1]) for i in range(len(points))])
	return totalDist

#get distance between 2 points
def dist(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5

##### TSP brute force
def tsp_brute(points):
	return (min([calcDist(list(points)) for points in itertools.permutations(points)]))
