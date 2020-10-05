import random
import math
import itertools
import numpy


numPoints = 4
points = []

for i in range(numPoints):
	points.append([random.randint(0,5), random.randint(0,5)])


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


##### Completely Brute Force and not great
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

	return points


##### Also brute force but way less lines of code
def main2(points):
	return (min([calcDist(list(points)) for points in itertools.permutations(points)]))


print(f"function 1: {main(points)}")
print(f"function 2 {main2(points)}")

