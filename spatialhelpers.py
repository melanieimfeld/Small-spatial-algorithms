import random
import time

print(__name__)

#create a bunch of random points as frozenset
def Cities(n, width = 400, height = 400, seed = 42):
	City = complex
	random.seed(seed * n)
	return frozenset((random.randrange(width), random.randrange(height)) for c in range(n))


#timer decorator
def timerfunc(func):
    def function_timer(*args, **kwargs):
        start = time.time_ns()
        value = func(*args, **kwargs)
        end = time.time_ns()
        runtime = (end - start) / 100000000 #convert ns to secs
        print(f"The runtime for {func.__name__} took {runtime} seconds to find {value}")
        #print(func.__name__, "," ,runtime, file=open("output_rtree.csv", "a"))

        return value
    return function_timer