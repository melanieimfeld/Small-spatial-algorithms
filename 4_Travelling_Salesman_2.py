import random
import math
#https://medium.com/basecs/speeding-up-the-traveling-salesman-using-dynamic-programming-b76d7552e8dd
#https://codereview.stackexchange.com/questions/81865/travelling-salesman-using-brute-force-and-heuristics

##### Brute Force
import numpy

##find the number of permutations for distinct items: n!

array = "WYXZW"
numPoints = 4
points = []

permutations = 3 * 2 * 1


for i in range(numPoints):
	points.append([random.randint(0,5), random.randint(0,5)])

def main(points):
	i = 0
	while(i < 5):
		points = swap(points, random.randint(0,len(points)-1),random.randint(0,len(points)-1))
		print(points, random.randint(0,len(points)-1))
		distance = calcDist(points)
		i += 1
		print(distance)

def swap(points, idx1, idx2):
	temp = points[idx1]
	points[idx1] = points[idx2]
	points[idx2] = temp
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


### recursion case (3 recursive calls)
#print(calcDist(points))
print(main(points))


### base case = no more nodes left to visit
# -> return costs of all six cases



