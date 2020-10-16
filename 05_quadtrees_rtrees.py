import spatialhelpers

#create a bunch or random points
cities = spatialhelpers.Cities(5)
print(cities)

#create a rectangle
class Rectangle():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.width = 200
		self.height = 200

class Quadtree():
	def __init__(self, boundary, n):
		self.bound = boundary
		self.capacity = n #when do we make a new quadtree?
		self.points = []

	def subdivide(self): #create new quadtree


	def insert(self, point):
		if len(self.points) < self.capacity: #capacity is not reached
			self.points.append(point)
		else: #capacity is reached
			self.subdivide()
			pass


boundary = Rectangle(0,0)
qt = Quadtree(boundary, 4)
print(qt.bound.x)


#for point in points:
#qt.insert(point)




