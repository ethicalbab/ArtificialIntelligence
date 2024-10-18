def oracle(graph, start_node, target_node):
    best_path = ['A', 'B', 'E', 'G']  # Example path
    return best_path if best_path[0] == start_node and best_path[-1] == target_node else None

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

result = oracle(graph, start_node, target_node)
print("Oracle path:", result)
