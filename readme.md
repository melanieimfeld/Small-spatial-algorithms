# Algorithms toolbox - Your everyday spatial algorithm

Note: this toolbox is meant to illustrate the principle behind methods that power your everyday GIS software rather than finding the least computationally intensive algorithm!

Index:  
[Ramer-Douglas-Peucker](https://github.com/melanieimfeld/Small-spatial-algorithms/blob/master/01_Ramer_Douglas_Peucker.py)  
[Haussdorf Distance](https://github.com/melanieimfeld/Small-spatial-algorithms/blob/master/02_Haussdorf.py)  
[Graham Scan Convex Hull](https://github.com/melanieimfeld/Small-spatial-algorithms/blob/master/03_Graham_Scan.py)  
[Traveling Salesperson](https://github.com/melanieimfeld/Small-spatial-algorithms/blob/master/04_Traveling_Salesperson_brute.py)  
[Quadtrees](https://github.com/melanieimfeld/Small-spatial-algorithms/blob/master/05_quadtrees_rtrees.py)

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
The Traveling Salesperson problem itself is simple to explain: Imagine a salesperson who needs to travel to different cities and back to the home city - in which order do the cities visited make up the shortest overall distance? When it comes to applications, the TSP does not have to be strictly geospatial: The distance can be replaced by any value, such as cost (e.g flight tickets) or time. The solution to the problem is far less simple: In fact, there are many solutions, some heuristic (i.e. approximations) and some exact, some computationally more or less intensive. Here, I want to explore the simplest way to solve the TSP in an exact manner and compare it with an approximation.


### Implementing the algorithm: Brute force version (Exact)
The basic way to solve this problem is to find all possible combinations of cities and select the combination - or tour - of cities that makes up the shortest overall distance. This idea illustrated for 4 cities named A,B,C and D in Fig. 1. In the script `04_Traveling_Salesperson_brute_nn.py`, the main function `tsp_brute()` takes an array of tuples as input and shuffles the array around using Python’s `itertools` module, while the helper functions `dist()`, `calcDist()`, `shortest()` calculate the total distance of each tour.

![TSP](/images/tsp.png)

### Implementing the algorithm: Nearest neighbor version (Approximation)
For the sake of speed, it might not always be necessary to find the shortest tour but rather a tour that is close to the shortest tour. There are exact algorithms that perform better than our brute force approach, but let’s also look at an approximation that will find a, but not necessarily the shortest tour: The nearest neighbor algorithm does pretty much exactly what you think it would do. For each city, it will simply find it's the nearest neighbor and stitch them together to create a tour.


### Time complexity
Brute force: O(n!) / Nearest neighbor: O(n2)

## 5) Geospatial queries: Quadtrees
### What do we need it for and how does it work?
Imagine you wanted to build an application that allows a user to find out what coffee shops that are within a given radius of the user's location. Intuitively, you would probably want to check if the lat/long positions of all coffee shops in your dataset fall within the given radius. You could do this easily, but in an array of n items, you would have to visit n-1 items, which is will essentially take you O(n) time. Spatial databases, such as Postgis, use more efficient methods for spatial queries such as the one just described. One method among many is the Quadtree algorithm. Like many algorithms, the Quadtree is used for applications beyond geospatial, such as collision detection in games, image processing, or data visualization. The Quadtree is also the conceptual basis for Geohashes, a common public domain geocoding system that encodes a geographic location into a short string of letters and digits.

### Implementing the algorithm
As the name implies, this algorithm works with four ("quad") trees. Instead of looking at each point as in the above example, we recursively scan through four quads to check if either of them overlaps with our search range. Before going through the code, it might make sense to define some conventions. In the [code](https://github.com/melanieimfeld/Small-spatial-algorithms/blob/master/05_quadtrees_rtrees.py), the chosen naming for each quadrant is NW, NE, SW, SE. The algorithm is implemented for a 2d plane, where x:0 and y:0 are at the top left corner (see Fig. 1.1).

![Quadtree](/images/quadtree.png)

Let's go through the most important steps of the algorithm:
1. In a first step, we will have to insert a given array of points, e.g. our coffee shops, into the Quadtree structure:
 	1. Define a maximum capacity `self.capacity`. The algorithm will recursively add points to a the quad that contains the point and the max. capacity will tell us how many points a quad is allowed to hold.
 	2. Below is the function that inserts a point into a Quadtree class (for more details on how the class is built, check out the source code). It only executes if the point is contained in `self.bound`, which defines our quad boundary. If the point is contained in `self.bound`, we have two options: If the capacity is not yet reached and there are no subdivisions, we append it to the current quad. If the capacity is reached and the quad is not subdivided already, we subdivide the current quad into four new child quads. Here, we'll also have to redistribute the main quads' points to the children and "clean" the main quad. Then, we insert the point in the correct child quad. 

 	```
 	def insert(self, point):
		if self.bound.contains(point): 
			if len(self.points) <= self.capacity and self.isDivided == False: #capacity is not reached
				self.points.append(point)
			else: #capacity is reached
				if not self.isDivided: #make child quads if not available yet
					self.subdivide()
					#here, there must be some points in the main quad that need to be redistributed to children
					for p in self.points:
						self.nw.insert(p)
						self.ne.insert(p)
						self.sw.insert(p)
						self.se.insert(p)
					self.points = [] #clean main
				self.nw.insert(point)
				self.ne.insert(point)
				self.sw.insert(point)
				self.se.insert(point)
	```

	3. Repeat the above procedure for each point in your array. Fig 2.1 and 2.2 show two different ways of visualizing the entire insert procedure for 32 points and a capacity of 3. 

![Quadtree Fig. 2.1 and 2.2](/images/quadtree1.png)

2. Implement a query function to find points within a search range:
	1. Now that we have inserted the points, we can query them. Fig. 3 illustrates an example of a rectangular search area in red. As you can see, the points within the search area can be on different quads, meaning that we will have to retrieve all points from different quads. Thus, our query function will input x, y, and size inputs for a rectangular search area that we call `myrange`. To find a point, we check if the search range intersects with the quad we are looking at. If it does not, we return an empty `found` array. If it does, we collect the points in our `found` array. To do this, we first check if the quad has children. If it does, we continue searching the children. If it doesn't, we append the points from the current quad. Note that there are two ways to append points in the current quad: If the `myrange` contains the quad, we append all points. Else, we will have to check each point on the quad to see if it overlaps.
	```	def query(self, myrange):
		found = []
		if not self.bound.intersects(myrange): #no intersection between bounding box and quad
			return found
		else:
			if self.isDivided: #and check if there are any children
				found.append(self.nw.query(myrange))
				found.append(self.ne.query(myrange))
				found.append(self.sw.query(myrange))
				found.append(self.se.query(myrange))
			else:
				if myrange.contains(self.bound):
					found.append(self.points)
				else:
					for p in self.points:
						if myrange.contains(p):
							found.append(p)
			return found
	```

![Quadtree Fig. 3](/images/quadtree2.png) 

### Time complexity
Similarly to binary search algorithms, this technique allows us to cut the searching time down to O(log(n)). I tested the above code with 100 points. For different search area sizes, it took between 1 to 3 seconds to retrieve the points within the search area, which is not blazingly fast, but undoubtedly faster than an algorithm scanning through all 99 points.


## 6) Geospatial queries: Rtrees and Uber's H3 
*tbd*
 

