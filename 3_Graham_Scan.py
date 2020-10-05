import numpy as np
import math
import operator

data = [(-1, 0), (1, 2), (2, 1), (-1, -4), (0.5, 0.5), (-0.5, 0.5)]


def isCcw(point1, point2, pointCurrent):
    #vector between point 1 - current point
    vec2x = point1[0] - pointCurrent[0]
    vec2y = point1[1] - pointCurrent[1]
    #vector between point 1 - point 2
    vec1x = point1[0] - point2[0]
    vec1y = point1[1] - point2[1]
    area = np.cross([vec1x, vec1y], [vec2x, vec2y])

    return area


class Points:
    def __init__(self, coords, angle):
        self.coords = coords
        self.angle = angle


def sortAngles(data, minPoint):
    angleList = []

    #Calculate angles
    for i in range(len(data)):
        if data[i] != minPoint:
            yDist = data[i][1] - minPoint[1]
            xDist = data[i][0] - minPoint[0]
            if xDist == 0:  #point is perpendicular to minpoint
                angle = math.pi / 2
            else:
                angle = np.arctan(yDist / xDist)

#dot product instead of arctan

            angleList.append(Points(data[i], angle))
    angleList.sort(key=operator.attrgetter('angle'))

    return angleList


def GrahamScan(data):
    #Select point with lowest y and append it to output array
    gift = []
    minPoint = min(data, key = lambda x : x[1])
    gift.append(minPoint)

    #get array of sorted angles
    angles = sortAngles(data, minPoint)

    for i in range(len(angles)):
        p = angles[i].coords
        while (len(gift) >= 2) and (isCcw(gift[-2], gift[-1], p) < 0): 
            gift.pop()  #negative, therefore remove point from output array
        gift.append(p)

    return gift

print(GrahamScan(data))

