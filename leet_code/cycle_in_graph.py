def cycleInGraph(edges):
    numberOfNodes = len(edges)
	visited = [False for _ in range(numberOfNodes)]
	currentlyInStack = [False for _ in range(numberOfNodes)]

	for node in range(numberOfNodes):
		if visited[node]:
			continue
			
		containsCycle = isNodeInCycle(node, edges, visited, currentlyInStack)
		if containsCycle:
			return True
		
		return False
	
	
def isNodeInCycle(node, edges, visited, currentlyInStack):
	visited[node] = True
	currentlyInStack[node] = True
	
	neigbors = edges[node]
	for neigbor in neighbors:
		if not visited[neighbor]:
			containsCycle = isNodeInCycle(neighbor, edges, visited, currentlyInStack)
			if containsCycle:
				return True
		elif currentlyInStack[neighbor]:
				return True
			
	currentlyInStack[node] = False
	return False