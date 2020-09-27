import numpy as np


#clockwise turn - > negative
test = np.cross((1,2),(2,1))

#counterclockwise turn -> positive
test2 = np.cross((2,1),(1,2))


print(test, test2)


def isCcw(point1, point2):
	area = np.cross(point1, point2)

	if area > 0:
		return "counterclockwise"
	elif area < 0:
		return "clockwise"
	else:
		return "zero" #collinear


#Select point with lowest y
#Calculate angles
#Sort points by angle relative to lowest point
#add points if there is a counterclockwise turn to previous point (cross product)
#if there is not, go back and try another point