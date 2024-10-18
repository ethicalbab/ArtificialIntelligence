import heapq

def branch_and_bound(graph, start_node, goal_node, cost_function):
    queue = [(0, [start_node])]
    optimal_cost = float('inf')
    optimal_path = None
    
    while queue:
        current_cost, current_path = heapq.heappop(queue)
        current_node = current_path[-1]
        
        if current_node == goal_node:
            if current_cost < optimal_cost:
                optimal_cost = current_cost
                optimal_path = current_path
            continue
        
        for neighbor in graph.get(current_node, []):
            if neighbor not in current_path:
                new_path = current_path + [neighbor]
                new_cost = current_cost + cost_function(current_node, neighbor)
                if new_cost < optimal_cost:
                    heapq.heappush(queue, (new_cost, new_path))
    
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

start_node = 'A'
goal_node = 'G'

result_path = branch_and_bound(graph, start_node, goal_node, cost_function)
print("Branch and Bound path:", result_path)
