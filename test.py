import math

data = [(0,1),(1,1),(-1,2),(1,2),(3,3)]

#data = [(0,1),(3,3)]

def perpendicularDistance(point, start, end):
	print(f"startX; {start[0]}, endX: {end[0]}, startY {start[1]}, endY {end[1]}")

	m = (end[1] - start[1]) / (end[0] - start[0])
	b = start[1] - m * start[0] #plug in either start or end
	a = m 
	b = -1
	c = b
	d = abs(a * point[0] + b * point[1] + c) / math.sqrt(a**2 + b**2) #formula line - point distance

	return d

def RDP(line, epsilon, results):
	 startIdx = 0
	 endIdx = len(line)-1
	 maxDist = 0 #var to store furthest point dist
	 maxId = 0 #var to store furthest point index

	 for i in range(startIdx+1,endIdx):
	 	print(i)
	 	d = perpendicularDistance(line[i], line[startIdx], line[endIdx])
	 	if d > maxDist:
	 		maxDist = d #overwrite max distance
	 		maxId = i #overwrite max index

	 if maxDist > epsilon:
	 	print("distance larger than epsilon")
	 	result1 = RDP(line[startIdx:maxId], epsilon, results)
	 	result2 = RDP(line[maxId:], epsilon, results)
	 
	 	results = [result1,result2]

	 else:
	 	print("no d > epsilon, keep first and last")
	 	results = [line[0], line[endIdx]]

	 return results

test = RDP(data, epsilon = 3, results = [])

print("test", test)