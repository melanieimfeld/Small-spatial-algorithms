import spatialhelpers

#create a bunch or random points
cities = spatialhelpers.Cities(100, width = 400, height = 400)
print(cities)

#create a rectangle
class Rectangle():
	def __init__(self, x, y, width, height):
		self.x = x #topleft
		self.y = y #topleft
		self.width = width
		self.height = height

	def contains(self, point):
		return (point[0] > self.x and self.x + self.width > point[0] and point[1] > self.y and point[1] < self.y + self.height)

class Quadtree():
	def __init__(self, boundary, n):
		self.bound = boundary
		self.capacity = n #when do we make a new quadtree?
		self.points = []
		self.isDivided = False

	def subdivide(self): #create 4 new quadtrees
		w = self.bound.width/2
		h = self.bound.height/2
		print(f"subdivide nw: {self.bound.x + w, self.bound.y} ne: {self.bound.x, self.bound.y} sw: {self.bound.x, self.bound.y + h}")

		self.nw = Quadtree(Rectangle(self.bound.x + w, self.bound.y, w, h), self.capacity)
		self.ne = Quadtree(Rectangle(self.bound.x, self.bound.y, w, h), self.capacity)
		self.sw = Quadtree(Rectangle(self.bound.x, self.bound.y + h, w, h), self.capacity) 
		self.se = Quadtree(Rectangle(self.bound.x + w, self.bound.y + h, w, h), self.capacity)
		self.isDivided = True

	def insert(self, point):
		if not self.bound.contains(point):
			return
		else:
			if len(self.points) < self.capacity: #capacity is not reached
				self.points.append(point)
			else: #capacity is reached
				if not self.isDivided: #make child quads if not available yet
					self.subdivide()

				self.nw.insert(point)
				self.ne.insert(point)
				self.sw.insert(point)
				self.se.insert(point)

boundary = Rectangle(0, 0, 400, 400)
qt = Quadtree(boundary, 4)

print(qt.bound.width)

for city in cities:
	qt.insert(city)

print(f"nw points {qt.nw.points}, ne points {qt.ne.points}, sw points {qt.sw.points}, se points {qt.se.points}")


#for point in points:
#qt.insert(point)




