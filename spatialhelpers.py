import random
import time

#create a bunch of random points as frozenset
def Cities(n, width = 400, height = 400, seed = 42):
	City = complex
	random.seed(seed * n)
	return frozenset((random.randrange(width), random.randrange(height)) for c in range(n))

#timer decorator
def timerfunc(func):
    def function_timer(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        print(f"The runtime for {func.__name__} took {runtime} seconds to find {value}")

        return value
    return function_timer