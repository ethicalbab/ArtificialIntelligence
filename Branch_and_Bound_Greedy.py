import heapq

def branch_and_bound_greedy(graph, start_node, target_node, cost_function, heuristic_function):
    priority_queue = [(0 + heuristic_function(start_node, target_node), 0, [start_node])]
    minimum_cost = float('inf')
    optimal_path = None
    
    while priority_queue:
        _, current_cost, current_path = heapq.heappop(priority_queue)
        current_node = current_path[-1]
        
        if current_node == target_node:
            if current_cost < minimum_cost:
                minimum_cost = current_cost
                optimal_path = current_path
            continue
        
        for neighbor in graph.get(current_node, []):
            if neighbor not in current_path:
                updated_path = current_path + [neighbor]
                path_cost = current_cost + cost_function(current_node, neighbor)
                if path_cost < minimum_cost:
                    priority = path_cost + heuristic_function(neighbor, target_node)
                    heapq.heappush(priority_queue, (priority, path_cost, updated_path))
    
    return optimal_path

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

def cost_function(node1, node2):
    return 1

def heuristic_function(node, goal):
    return ord(goal) - ord(node)

start_node = 'A'
target_node = 'G'

result_path = branch_and_bound_greedy(graph, start_node, target_node, cost_function, heuristic_function)
print("Branch and Bound Greedy path:", result_path)
