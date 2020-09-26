import math
import numpy as np

#data = [(0,1),(1,1),(-1,2),(1,2),(3,3)]
data = [(0,0),(1,3),(2,-0.5),(4,0)]

def perpendicularDistance(point, start, end):
  m = (end[1] - start[1]) / (end[0] - start[0])
  b = start[1] - m * start[0] #plug in either start or end
  a = m 
  b = -1
  c = b
  d = abs(a * point[0] + b * point[1] + c) / math.sqrt(a**2 + b**2) #formula line - point distance

  return d


def RDP(line, epsilon):
   startIdx = 0
   endIdx = len(line)-1
   maxDist = 0 #var to store furthest point dist
   maxId = 0 #var to store furthest point index

   for i in range(startIdx+1,endIdx):
    d = perpendicularDistance(line[i], line[startIdx], line[endIdx])
    if d > maxDist:
      maxDist = d #overwrite max distance
      maxId = i #overwrite max index

   if maxDist > epsilon:
    print("d larger than epsilon at index", maxId, line[maxId])
    l = RDP(line[startIdx:maxId+1], epsilon)
    r = RDP(line[maxId:], epsilon)

    results = np.vstack((l[:-1], r))
    return results

   else:
    print(f"no d smaller that epsilon, keep first {line[0]} and last {line[endIdx]}")
    #results = [line[0], line[endIdx]]
    results = np.vstack((line[0], line[endIdx]))
    return results
    #print("results:", results)

   #return results

test = RDP(data, epsilon = 1.8)
