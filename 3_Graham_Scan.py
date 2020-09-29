import numpy as np
import math
import operator

data = [(-1, 0), (1, 2), (2, 1), (-1, -4), (0.5, 0.5), (-0.5, 0.5)]


def isCcw(point1, point2, pointCurrent):
    #point 1 - current
    vec2x = point1[0] - pointCurrent[0]
    vec2y = point1[1] - pointCurrent[1]
    #point 1 - point 2
    vec1x = point1[0] - point2[0]
    vec1y = point1[1] - point2[1]
    area = np.cross([vec1x, vec1y], [vec2x, vec2y])

    return area


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
            if xDist == 0:  #point is perpendicular to minpoint
                angle = math.pi / 2
            else:
                angle = np.arctan(yDist / xDist)

#dot product instead of arctan

            angleList.append(Points(data[i], angle))
            angleList.sort(key=operator.attrgetter('angle'))

    return angleList


def GrahamScan(data):
    #Select point with lowest y
    gift = []
    minY = data[0][1]
    #midIdx = 0

    for i, point in enumerate(data):
        if point[1] < minY:
            minY = point[1]
            minIdx = i
            gift.append(data[minIdx])

    angles = sortAngles(data, minIdx)

    for i in range(len(angles)):
        p = angles[i].coords
        while (len(gift) >= 2) and (isCcw(gift[-2], gift[-1], p) < 0):
            gift.pop()

        gift.append(p)

        #for i in len(angles):
        # p = angles[i].coords
        # while isCcw(gifts[-2],gifts[-1],p) < 0:
        #   gifts.pop()
        # gifts.append(p)  =

    return gift


print(GrahamScan(data))

#https://www.youtube.com/watch?v=B2AJoQSZf4M
#Select point with lowest y
#Calculate angles
#Sort points by angle relative to lowest point
#go through list
#add points if there is a counterclockwise turn to previous point (cross product)
#if there is not, go back and try another point
