import random

def random_walk_search(graph, start_node, target_node):
    path = [start_node]
    while path[-1] != target_node:
        current_node = path[-1]
        if current_node in graph:
            next_node = random.choice(graph[current_node])
            path.append(next_node)
    return path

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

start_node = 'A'
target_node = 'G'

result_path = random_walk_search(graph, start_node, target_node)
print("Random Walk Search path:", result_path)
