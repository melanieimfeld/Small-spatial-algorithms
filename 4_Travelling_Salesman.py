import random
import math
import itertools

##### Completely Brute Force and not great
#do it more like this!
#https://codereview.stackexchange.com/questions/81865/travelling-salesman-using-brute-force-and-heuristics

import numpy

##find the number of permutations for distinct items: n!

numPoints = 4
points = []

for i in range(numPoints):
	points.append([random.randint(0,5), random.randint(0,5)])

def main(points):
	i = 0
	minDistance = calcDist(points)

	for points in itertools.permutations(points):
		points = list(points)
		print(minDistance)
		#print(points, random.randint(0,len(points)-1))
		#points = swap(points, random.randint(0,len(points)-1),random.randint(0,len(points)-1))
		distance = calcDist(points)
		if distance < minDistance:
			minDistance = distance
		i += 1
	return f"min dist {minDistance}" 

def swap(points, idx1, idx2):
	temp = points[idx1]
	points[idx1] = points[idx2]
	points[idx2] = temp

	#do it more like this!
#https://codereview.stackexchange.com/questions/81865/travelling-salesman-using-brute-force-and-heuristics

	return points

def calcDist(points):
	sum = 0
	for i in range(len(points)):
		if i == len(points)-1:
			dist = distance(points[i], points[0])
		else:
			dist = distance(points[i], points[i + 1])
		sum += dist
	return sum


def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5

print(main(points))



