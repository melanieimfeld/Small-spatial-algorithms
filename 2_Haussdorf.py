import math

data = [(1,1), (0,0)]
data2 = [(2,4), (3,3), (4,1)]

def distance(point1, point2):
	a = point2[0] - point1[0]
	b = point2[1] - point1[1]
	c = math.sqrt(a**2 + b**2)
	return c

#find the largest of shortest distances 
def haussdorf(A, B):
	h = 0
	arr = []
	
	for i in A:
		print("switch")
		shortest = float('inf')
		for j in B:
			dist = distance(i,j)
			print(f"distance between: {dist}")
			if dist < shortest:
				shortest = dist
		print("shortest: ", shortest)
		arr.append(shortest)

	return max(arr)

h = haussdorf(data, data2)
h2 = haussdorf(data2, data)
print(f"shortest distance {h} {h2}")


##https://stackoverflow.com/questions/13692801/distance-matrix-of-curves-in-python
