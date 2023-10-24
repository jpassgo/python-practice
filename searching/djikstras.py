from typing import List

graph = {}
graph['a'] = ['b','c','d','z','k']
graph['b'] = ['c','z','l']
graph['g'] = ['f','w','z','k']
graph['m'] = ['s','q','i']

print(graph)

def djikstras_algorithm(graph, source):
    unvisited = []
    for node in graph:
        