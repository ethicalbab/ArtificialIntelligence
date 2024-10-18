import heapq

def branch_and_bound(graph, start_node, target_node, heuristic_func):
    priority_queue = [(heuristic_func(start_node, target_node), [start_node])]
    explored = set()
    
    while priority_queue:
        _, current_path = heapq.heappop(priority_queue)
        current_node = current_path[-1]
        
        if current_node == target_node:
            return current_path
        
        if current_node not in explored:
            explored.add(current_node)
            for neighbor in graph.get(current_node, []):
                if neighbor not in explored:
                    updated_path = current_path + [neighbor]
                    priority = heuristic_func(neighbor, target_node)
                    heapq.heappush(priority_queue, (priority, updated_path))
    
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

result_path = branch_and_bound(graph, start_node, target_node, heuristic)
print("Branch and Bound path:", result_path)
