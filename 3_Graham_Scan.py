import numpy as np
import math

data = [(-1,0),(1,2),(2,1),(-1,-4),(-0.5,0.5)]


def isCcw(point1, point2):
	area = np.cross(point1, point2)

	if area > 0:
		return "counterclockwise"
	elif area < 0:
		return "clockwise"
	else:
		return "collinear" #collinear

def sortAngles(data, minIdx):
	angleList2 = {}
	angleList2[0] = data[minIdx]
	angleList = []
	
	#Calculate angles
	for i in range(len(data)):
		if data[i] != data[minIdx]:
			yDist = data[i][1] - data[minIdx][1]
			xDist = data[i][0] - data[minIdx][0]
			#print(yDist, xDist)
			if xDist == 0: #point is perpendicular to minpoint
				angle = math.pi / 2
			else:
				angle = np.arctan(yDist / xDist)
			
			angleList2[angle] = data[i]
			angleList.append(angle)

	angleList.sort()

	temp = sorted(angleList2.values())
	return angleList2


def GrahamScan(data):
	#Select point with lowest y
	gift = []
	minY = data[0][1]
	midIdx = 0
	
	for i,point in enumerate(data):
		if point[1] < minY:
			minY = point[1]
			minIdx = i

	print(f"index of min point: {minIdx}")
	#a = data[1][1] - data[0][1]
	
	angles = sortAngles(data, minIdx)
	keyList=sorted(angles.keys())
	print(angles)
	
	for index, value in enumerate(keyList):
		if (index>0) & (index<len(keyList)-1):
			print(value, angles[keyList[index]], angles[keyList[index+1]])
			ccw = isCcw(angles[keyList[index]], angles[keyList[index+1]])
			print(ccw)
	#print(temp)
	#print(angleList2)

	# for point, angle in angleList2.items():
	# 	ccw = isCcw(data[minIdx],point)
	# 	print(ccw)
	# 	print(point, angle)

	#print(f"angle list {angleList2}")


#print("cross", np.cross((0,0),(-1,-4)))

GrahamScan(data)




#https://www.youtube.com/watch?v=B2AJoQSZf4M
#Select point with lowest y
#Calculate angles
#Sort points by angle relative to lowest point
#go through list
#add points if there is a counterclockwise turn to previous point (cross product)
#if there is not, go back and try another point