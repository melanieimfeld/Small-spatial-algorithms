import random

#create a bunch of random points as frozenset
def Cities(n, width = 400, height = 400, seed = 42):
	City = complex
	random.seed(seed * n)
	return frozenset((random.randrange(width), random.randrange(height)) for c in range(n))

#test = Cities(4)
#print(test)