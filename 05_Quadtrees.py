import spatialhelpers
import matplotlib.pyplot as plt
import cProfile

#create a bunch or random points
cities = spatialhelpers.Cities(1000)

#create a rectangle
class Rectangle():
	'''Class for the quad rectangles. The function contains takes in points and rectangles, to see if a point or a search range is fully within a quad.
	Intersects detects if two rectangles, the quad and the search range partially overlap'''
	def __init__(self, x, y, width, height):
		self.x = x #topleft
		self.y = y #topleft
		self.width = width
		self.height = height

	def contains(self, point):
		if not isinstance(point, Rectangle):
			return (point[0] >= self.x and self.x + self.width > point[0] and point[1] >= self.y and point[1] < self.y + self.height)
		else:
			return (point.x >= self.x and point.x + point.width <= self.x + self.width and point.y >= self.y and point.y + point.height <= self.y + self.height)
			
	def intersects(self, myrange): #for rectangles
		return not (self.x + self.width < myrange.x or self.x > myrange.x + myrange.width or self.y > myrange.y + myrange.height or self.y + self.height < myrange.y)

class Quadtree():
	def __init__(self, boundary, n):
		self.bound = boundary
		self.capacity = n
		self.points = []
		self.isDivided = False

	def subdivide(self): #create 4 new quadtrees
		w = self.bound.width/2
		h = self.bound.height/2

		self.ne = Quadtree(Rectangle(self.bound.x + w, self.bound.y, w, h), self.capacity)
		self.nw = Quadtree(Rectangle(self.bound.x, self.bound.y, w, h), self.capacity)
		self.sw = Quadtree(Rectangle(self.bound.x, self.bound.y + h, w, h), self.capacity) 
		self.se = Quadtree(Rectangle(self.bound.x + w, self.bound.y + h, w, h), self.capacity)
		self.isDivided = True

	def query(self, myrange):
		'''To find a point, we check if the search range intersects with the quad we are looking at. If it does not, we return an empty array. 
		If it does, we need to collect the pointss. We first check if the quad has children. If it does, we continue searching the children. If it doesn't, we append the points'''
		found = []
		if not self.bound.intersects(myrange): #no intersection between bounding box and quad
			return found
		else: #else collect points
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


	def insert(self, point):
		'''Below only executes if point is contained in bound. Else, nothing happens. If the point is contained in bound, we have two options. If the capacity is not yet reached and there are no subdivisions, 
		we append it to the current quad. If not subdivided already, we subdivide the current quad into four new quads. Here, we'll also have to redistribute the main quads to the subdivisions and "clean" the main quad.
		Then, we insert the point in the correct subdivision '''

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
					self.points = []

				self.nw.insert(point)
				self.ne.insert(point)
				self.sw.insert(point)
				self.se.insert(point)



'''This part will take care of inserting our points in the quadtree structure before we can return it'''
boundary = Rectangle(0, 0, 400, 400)
qt = Quadtree(boundary, 3)

@spatialhelpers.timerfunc
def insertPoints():
	for city in cities:
		qt.insert(city)


'''Once inserted, we can query the points. This function only supports a rectangular range as query method, but we could also use nearest neighbors or a circular buffer range'''
@spatialhelpers.timerfunc
def findPoints(range):
	result = qt.query(range)
	return result

for i in range(1000):
	insertPoints()
	findPoints(Rectangle(50,50,50,50))

#print(cities)


