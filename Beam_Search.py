import heapq

def beam_search(graph, start_node, target_node, beam_size, heuristic_func):
    beam = [(heuristic_func(start_node, target_node), [start_node])]
    
    while beam:
        next_beam = []
        
        for _, current_path in beam:
            current_node = current_path[-1]
            
            if current_node == target_node:
                return current_path
            
            for neighbor in graph.get(current_node, []):
                extended_path = current_path + [neighbor]
                next_beam.append((heuristic_func(neighbor, target_node), extended_path))
        
        beam = heapq.nsmallest(beam_size, next_beam)
        
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

def heuristic(node, goal):
    return ord(goal) - ord(node)

start_node = 'A'
target_node = 'G'
beam_size = 2

result_path = beam_search(graph, start_node, target_node, beam_size, heuristic)
print("Beam Search path:", result_path)
