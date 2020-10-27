import spatialhelpers
import matplotlib.pyplot as plt

#create a bunch or random points
#cities = spatialhelpers.Cities(100, width = 400, height = 400)
cities = [(2,2),(3,3),(4,4),(5,5), (150,50),(300,100), (200,200),(200,300)]
#cities = [(2,2),(3,3),(4,4)]
print("original array", cities)

#create a rectangle
class Rectangle():
	def __init__(self, x, y, width, height):
		self.x = x #topleft
		self.y = y #topleft
		self.width = width
		self.height = height

	def contains(self, point):
		if not isinstance(point, Rectangle):
			return (point[0] >= self.x and self.x + self.width > point[0] and point[1] >= self.y and point[1] < self.y + self.height)
		else:
			#print("item is rect too!")
			return (point.x >= self.x and point.x + point.width <= self.x + self.width and point.y >= self.y and point.y + point.height <= self.y + self.height)
			

	def intersects(self, myrange): #for rectangles
		return not (self.x + self.width < myrange.x or self.x > myrange.x + myrange.width or self.y > myrange.y + myrange.height or self.y + self.height < myrange.y)


class Quadtree():
	def __init__(self, boundary, n):
		self.bound = boundary
		self.capacity = n #when do we make a new quadtree?
		self.points = []
		self.isDivided = False

	def subdivide(self): #create 4 new quadtrees
		w = self.bound.width/2
		h = self.bound.height/2
		print(f"subdivide ne: {self.bound.x + w, self.bound.y} nw: {self.bound.x, self.bound.y} sw: {self.bound.x, self.bound.y + h} se: {self.bound.x + w, self.bound.y + h}")

		self.ne = Quadtree(Rectangle(self.bound.x + w, self.bound.y, w, h), self.capacity)
		self.nw = Quadtree(Rectangle(self.bound.x, self.bound.y, w, h), self.capacity)
		self.sw = Quadtree(Rectangle(self.bound.x, self.bound.y + h, w, h), self.capacity) 
		self.se = Quadtree(Rectangle(self.bound.x + w, self.bound.y + h, w, h), self.capacity)
		self.isDivided = True

	def query(self, myrange): #does this range and a quadtree overlap?
		found = []
		if not self.bound.intersects(myrange): #no intersection between bounding box and quad
			return found
		else: #else collect points
			if myrange.contains(self.bound):
				print("range is bigger than quadtree")
				found.append(self.points)
			else:
				for p in self.points:
					if myrange.contains(p):
						found.append(p)

			if self.isDivided: #and check if there are any children
				found.append(self.nw.query(myrange))
				found.append(self.ne.query(myrange))
				found.append(self.sw.query(myrange))
				found.append(self.se.query(myrange))

			return found


	def insert(self, point):
		# if not self.bound.contains(point):
		# 	return
		# else:
		if self.bound.contains(point):
			if len(self.points) < self.capacity: #capacity is not reached
				print("capacity not reached", self.points)
				self.points.append(point)
			else: #capacity is reached
				print("capacity reached", self.points)
				if not self.isDivided: #make child quads if not available yet
					self.subdivide()

				self.nw.insert(point)
				self.ne.insert(point)
				self.sw.insert(point)
				self.se.insert(point)

boundary = Rectangle(0, 0, 400, 400)
qt = Quadtree(boundary, 3)

'''This part will take care of inserting our points in the quadtree structure before we can return it'''
for city in cities:
	qt.insert(city)

#print("qt", qt.nw, qt.ne.points, qt.sw.points, qt.se.points)
print("MAIN quad", qt.points, "NW points", qt.nw.points, "SW points",qt.sw.points, "SE points", qt.se.points,  "NE points", qt.ne.points)
#print(f"nw points {qt.nw.points}, ne points {qt.ne.points}, sw points {qt.sw.points}, se points {qt.se.points}")

#plt.scatter(*zip(*cities)) #* -> reversed zip (unzip)
#plt.show()


'''Once inserted, we can query the points. We could look at different spatial query method, like nearest neighbors or range (rectangle or circle)'''
bbbox = Rectangle(200,200,200,200)

#print(boundary.contains(bbbox))
#qt.query(bbbox)
print(qt.query(bbbox))

'''
TODO:
- what if point is not contained by any quadtree because it lies on intersection of two trees?
- Examples seem to suggest that only leaf nodes contain points
'''




