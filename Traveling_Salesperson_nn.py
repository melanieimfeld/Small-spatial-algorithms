from Traveling_Salesperson_brute import dist, createPoints

'''Approximate algorithm. Select a starting point, append to partial tour list, subtract from unvisited list and 
find nearest neighbor out of unvisited list that is nearest to end of partial tour list'''

def tsp_nn(points, startPoint):
	visited = [startPoint]
	unvisited = points
	unvisited.remove(startPoint)
	
	totalDist = 0

	while(len(unvisited) >= 1):
		nn = find_nn(visited[-1], unvisited)
		unvisited.remove(nn)
		visited.append(nn)
	return visited

def find_nn(p, unvisited):
	return min(unvisited, key = lambda x: dist(x , p))
		
inputs = createPoints(6)
print(tsp_nn(inputs, inputs[0]))