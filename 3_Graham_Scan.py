import numpy as np
import math
import operator

data = [(-1,0),(1,2),(2,1),(-1,-4),(0.5,0.5),(-0.5,0.5)]


def isCcw(point1, point2):
	area = np.cross(point1, point2)

	if area > 0:
		return "counterclockwise"
	elif area < 0:
		return "clockwise"
	else:
		return "collinear" #collinear

class Points:
	def __init__(self, coords, angle):
		self.coords = coords
		self.angle = angle
		self.ccw = "none"
		self.order = 0

def sortAngles(data, minIdx):
	angleList = []

	#Calculate angles
	for i in range(len(data)):
		if data[i] != data[minIdx]:
			yDist = data[i][1] - data[minIdx][1]
			xDist = data[i][0] - data[minIdx][0]
			if xDist == 0: #point is perpendicular to minpoint
				angle = math.pi / 2
			else:
				angle = np.arctan(yDist / xDist)
			
			angleList.append(Points(data[i], angle))
			angleList.sort(key=operator.attrgetter('angle'))

	return angleList


def GrahamScan(data):
	#Select point with lowest y
	gift = []
	minY = data[0][1]
	midIdx = 0
	
	for i,point in enumerate(data):
		if point[1] < minY:
			minY = point[1]
			minIdx = i
			gift.append(data[minIdx]) 

	
	angles = sortAngles(data, minIdx)
	#valueList=sorted(angles.values())
	for i in range(1,len(angles)-1):
		angles[i].ccw = isCcw(angles[i].coords, angles[i+1].coords)
		print(f"from {angles[i].coords} to {angles[i+1].coords}  is {angles[i].ccw}")
		if angles[i].ccw == "clockwise":
			gift.append(angles[i].coords)
		else:
			pass

	print(gift)
	return gift

#print("cross", np.cross((0,0),(-1,-4)))

GrahamScan(data)



#https://www.youtube.com/watch?v=YNyULRrydVI&feature=youtu.be
#https://www.youtube.com/watch?v=B2AJoQSZf4M
#Select point with lowest y
#Calculate angles
#Sort points by angle relative to lowest point
#go through list
#add points if there is a counterclockwise turn to previous point (cross product)
#if there is not, go back and try another point