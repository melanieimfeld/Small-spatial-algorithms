# Algorithms toolbox - Your everyday spatial algorithm

Note: this toolbox is meant to illustrate the principle behind methods that power your everyday GIS software rather than finding the least computationally intensive algorithm!

Index:  
[Ramer-Douglas-Peucker](https://github.com/melanieimfeld/Small-spatial-algorithms/blob/master/1_Ramer_Douglas_Peucker.py)  
[Haussdorf Distance](https://github.com/melanieimfeld/Small-spatial-algorithms/blob/master/2_Haussdorf.py)  
[Graham Scan Convex Hull](https://github.com/melanieimfeld/Small-spatial-algorithms/blob/master/3_Graham_Scan.py)  
[Traveling Salesperson](https://github.com/melanieimfeld/Small-spatial-algorithms/blob/master/4_Traveling_Salesperson_brute.py)  
Quadtrees *tbd*  

## 1) Ramer-Douglas-Peucker algorithm
### What do we need it for and how does it work?
The Ramer-Douglas-Peucker algorithm is used in cartographic generalization to simplify vector lines - in any standard GIS software, there will be a command to execute the RDP or a similar algorithm without having to know how it works under the hood. Though it was developed for GIS problems, it can also be applied to computer vision problems, such as simplifying contours.

### Getting the distance between baseline and furthest point `checkdistance()`
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


### Implementing the algorithm
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


## 2) Hausdorff Distance between polygons
### What do we need it for and how does it work?
The Hausdorff distance is concerned with describing the nearness of two polygons. Rather than just looking at the two nearest points between two polygons, the definition of "closeness" in Hausdorff considers the entire polygon. Hausdorff distance is the «maximum distance of a set to the nearest point in the other set». It can be used in computer vision, e.g to find similar items.

### Implementing the algorithm
For every point in polygon A, we compute the Euclidian distance to every point in polygon B and keep the shortest distance. Out of the collected shortest distances, we keep the longer one with is the Hausdorff distance h(A,B). It is important to note that h(A,B) is unequal to h(B,A).


### Time complexity
O(n * m) or O(n + m) for the linear time implementation, see here: https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1362&context=cstech

## 3) Convex Hull Gift Wrapping - Graham Scan
### What do we need it for and how does it work?
In computational geometry, gift wrapping algorithms are a family of algorithms that compute the convex hull of a given set of points. What is a convex hull? Basically, it is a shape that encloses a set of points, such that no corners of the shape are bent inwards, hence the name “gift wrapping”. But why would you want to find this shape? Although the technique seems to have a variety of applications outside of GIS, such as image processing, I am most familiar with GIS applications. For example, a convex hull can be used as a way to better describe patterns, such as animal movements that were collected as point features.

![GC](/images/gc.jpg)

### Implementing the algorithm
1. Given a set of points, select point with lowest y value (Fig. 1)
2. Calculate angles between the lowest point and all the other points (Fig. 1)
3. The size of the angle will determine in which order to iterate through points. Thus, sort points by angle relative to lowest point in ascending order
4. Iterate through points. Add a point to an output array if there is a counterclockwise turn to previous point. To figure out if a turn is clockwise or counterclockwise, we can leverage the cross product of two vectors (Fig. 2 and 3).
5. If a point is located clockwise relative to the previous point, we pop it off the output array.
6. When we are done with scanning the points, return the result (Fig. 4)


### Time complexity
O(n * log(n))

Most sorting algorithms take n log(n) time, while the actual scan takes n time. We select the dominant function, therefore the overall time complexity is O(n log (n)). How could we optimize the Graham scan? We could for example wipe out points in the interior that we for sure know are not in the convex hull by finding the farthest points in the SW, NW, NE, and SE direction and eliminte the points that are enclosed by these 4 points. I will try to update the Repo with an example the above optimization process in the next weeks!


## 4) Traveling Salesperson Problem
### What do we need it for and how does it work?
The TSP problem isn't hard to explain: Imagine a salesperson who needs to travel to different cities and back to the home city - in which order do the cities visited make up the shortest overall distance? Unfortunately, the solution to this problem isn't as simple. In fact, there are many solutions, some heuristic ( = approximations) and some exact, some computationally more or less intensive. In graph theory lingo, we would call our cities "nodes" or "vertices" and our distances between cities "edges". The distance itself is called "weight" in graph theory. When it comes to applications, the TSP does not have to be geospatial at all: The weight of the edges can be replaced by any value, such as cost (e.g flight tickets).



### Implementing the algorithm: Exact, brute force version
- a weighted, undirected graph
- Exact and not approximate solution

### Implementing the algorithm: Exact, Held-Karp
- only the shortest subpath


### Time complexity
O(n!)

## 5) Quadtree
*tbd*


