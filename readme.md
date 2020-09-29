# Algorithms toolbox - Your everyday spatial algorithm!

Note: this toolsbox is meant to illustrate the priciple behind these methods rather than finding the least computationally intensive algorithm.

Jump to:  
[Ramer-Douglas-Peucker](#Ramer-Douglas-Peucker)  
[Haussdorf Distance](#Haussdorf)  
[Graham Scan Convex Hull](#Graham)  
[Rtrees](#Rtrees)


## Ramer-Douglas-Peucker algorithm
### What do we need it for and how does it work?
The Ramer-Douglas-Peucker algorithm is used in cartographic generalization to simplify vector lines - in any standard GIS software, there will be a command to execute the RDP or a similar algorithm without having to know how it works under the hood. Though it was developed for GIS problems, it can also be applied to computer vision problems, such as simplifying contours.

### Step 1) Getting the distance between baseline and furthest point `checkdistance()`
First, we need to find the function for the baseline, which is defined by:  
` y = mx + b `

We can find the slope m by subtracting x_start from x_end and y_start from y_end and dividing the resulting distances:  
`m = (y_end - y_start) / (x_end - x_start)`

From that, we'll be able to derive `b` by simply plugging in `m`, `x` or `x_start`, and `y` or `y_start`:  
`b = y - mx` -> `b = y_start - m * x_start`

Next, we'll have to transform the slope intercept notation of our baseline to the standard form ax + by + c = 0:  
y = mx + b -> 0 = mx - (1)y - b

Therefore:  
`m = a  
b = -1  
c = -b`  

We can then use the following formula to get the distance between a line and a point.  
`d = abs(a * x_point - b * y_point + c / sqrt(a^2 + b^2)`


### Step 2) Implementing the algorithm
The function for the algorithm takes in an array of points (i.e. the line we want to simplify) as well as a "threshold" variable called epsilon. It starts by connecting the first and the last point of the original line with a "baseline". It then finds the point that is furthest away from that baseline. If that point is greater than epsilon, it will be kept and the function continues to recursively split the line into two segments and repeat the procedure. If the point is nearer from the baseline than epsilon, then all the points along the baseline can be discarded as they will be smaller than epsilon too. The output will be an array containing only those points that were marked as kept. Implemented in Python, the RDP function looks like this:

![RDP](/images/rdp.jpg)

```
def RDP(line, epsilon, results):
	 startIdx = 0
	 endIdx = len(line)-1
	 maxDist = 0 #var to store furthest point dist
	 maxId = 0 #var to store furthest point index

	 for i in range(startIdx+1,endIdx):
	 	d = perpendicularDistance(line[i], line[startIdx], line[endIdx])
	 	if d > maxDist:
	 		maxDist = d #overwrite max distance
	 		maxId = i #overwrite max index

	 if maxDist > epsilon: #
	 	result1 = RDP(line[startIdx:maxId+1], epsilon, results)
	 	result2 = RDP(line[maxId:], epsilon, results)
	 
	 	results = [result1,result2]

	 else:
	 	results = [line[0], line[endIdx]]

	 return results
```

### Time complexity
O(n * log(n))


## Hausdorff Distance between polygons
### What do we need it for and how does it work?
The Hausdorff distance is concerned with describing the nearness of two polygons. Rather than just looking at the two nearest points between two polygons, the definition of "closeness" in Hausdorff considers the entire polygon. Hausdorff distance is the «maximum distance of a set to the nearest point in the other set». It can be used in computer vision, e.g to find similar items.

### Step 1) Implementing the algorithm
For every point in polygon A, we compute the Euclidian distance to every point in polygon B and keep the shortest distance. Out of the collected shortest distances, we keep the longer one with is the Hausdorff distance h(A,B). It is important to note that h(A,B) is unequal to h(B,A).


### Time complexity
O(n * m) or O(n + m) for the linear time implementation, see here: https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1362&context=cstech

## Convex Hull Gift wrapping (jarvis / Graham)
A convex shape is one where all angles are less than 180 degrees.

### Step 1) Implementing the algorithm
- Select point with lowest y
- Calculate angles
- Sort points by angle relative to lowest point
- add points if there is a counterclockwise turn to previous point (cross product)
- if there is not, go back and try another point

### Time complexity
O(n * log(n))

## Rtrees
https://github.com/VictorDavis/GeoConvexHull
