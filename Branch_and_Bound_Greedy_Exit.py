import heapq

def branch_and_bound_greedy_exit(graph, start_node, target_node, cost_function, heuristic_function, max_iterations):
    priority_queue = [(0 + heuristic_function(start_node, target_node), 0, [start_node])]
    optimal_cost = float('inf')
    optimal_path = None
    count = 0
    
    while priority_queue:
        count += 1
        if count > max_iterations:
            return optimal_path
        
        (_, current_cost, current_path) = heapq.heappop(priority_queue)
        current_node = current_path[-1]
        
        if current_node == target_node:
            if current_cost < optimal_cost:
                optimal_cost = current_cost
                optimal_path = current_path
            return optimal_path
        
        for neighbor in graph.get(current_node, []):
            if neighbor not in current_path:
                new_path = current_path + [neighbor]
                new_cost = current_cost + cost_function(current_node, neighbor)
                if new_cost < optimal_cost:
                    priority = new_cost + heuristic_function(neighbor, target_node)
                    heapq.heappush(priority_queue, (priority, new_cost, new_path))
    
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
max_iterations = 10

result_path = branch_and_bound_greedy_exit(graph, start_node, target_node, cost_function, heuristic_function, max_iterations)
print("Branch and Bound Greedy with Exit path:", result_path)
