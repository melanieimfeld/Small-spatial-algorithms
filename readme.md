# Algorithms toolbox - Your everyday spatial algorithm!

## Ramer-Douglas-Peucker Line Simplification
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
The function for the algorithm takes in an array of points (i.e. the line we want to simplify) as well as a "threshold" variable, epsilon. The algorithm starts by connecting the first and the last point of the original line with a "baseline". It then finds the point that is furthest away from that baseline. If that point is greater than epsilon, it will be kept and the function continues recursively by splitting the line into two segments and repeating the procedure. If the point is nearer from the baseline than epsilon, then all the points along the baseline can be discarded as they will be smaller than epsilon too. The output will be an array containing only those points that were marked as kept. The function looks like this:


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
	 	result1 = RDP(line[startIdx:maxId], epsilon, results)
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
The Hausdorff distance is concerned with the fact, that two polygons that are considered "near" means that all their vertices (points) are near, rather than just looking at the two nearest points between two polygons. Unlike the "shortest path distance", the "nearness" in Hausdorff considers the entire polygon. Hausdorff distance is the «maximum distance of a set to the nearest point in the other set». It can be used in computer vision, e.g to find similar items.

### Step 1) Implementing the algorithm


## Rtrees
## Convex Hull
https://github.com/VictorDavis/GeoConvexHull
