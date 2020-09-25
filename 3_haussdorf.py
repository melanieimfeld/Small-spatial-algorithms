import math

data = [(0,0), (1,1)]
data2 = [(2,4), (3,3), (4,1)]

def distance(point1, point2):
	a = point2[0] - point1[0]
	b = point2[1] - point1[1]
	c = math.sqrt(a**2 + b**2)
	return c

#find the largest of shortest distances 
def haussdorf(A, B):
	h = 0
	for i in A:
		shortest = float("inf")
		for j in B:
			dist = distance(i,j)
			print(dist)
			if dist < shortest:
				shortest = dist
	if shortest > h:
		h = shortest
	return shortest

test = haussdorf(data, data2)
print(f"shortest distance {test} ")


#find the largest of shortest distances 
def haussdorf2(A, B):
	h = 0
	shortest = float("inf")
	for i in A:
		for j in B:
			dist = distance(i,j)
			print(dist)
			if dist < shortest:
				shortest = dist
	if shortest > h:
		h = shortest
	return shortest

test = haussdorf(data, data2)
print(f"shortest distance2 {test} ")