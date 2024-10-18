import heapq

def branch_and_bound_with_heuristic(graph, start_node, target_node, cost_function, heuristic_function):
    priority_queue = [(0 + heuristic_function(start_node, target_node), 0, [start_node])]
    explored = set()
    
    while priority_queue:
        (_, current_cost, current_path) = heapq.heappop(priority_queue)
        current_node = current_path[-1]
        
        if current_node == target_node:
            return current_path
        
        if current_node not in explored:
            explored.add(current_node)
            for neighbor in graph.get(current_node, []):
                if neighbor not in explored:
                    updated_path = current_path + [neighbor]
                    updated_cost = current_cost + cost_function(current_node, neighbor)
                    priority_value = updated_cost + heuristic_function(neighbor, target_node)
                    heapq.heappush(priority_queue, (priority_value, updated_cost, updated_path))
    
    return None

graph_structure = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

def uniform_cost(node1, node2):
    return 1

def simple_heuristic(node, goal):
    return ord(goal) - ord(node)

start_node = 'A'
target_node = 'G'

result_path = branch_and_bound_with_heuristic(graph_structure, start_node, target_node, uniform_cost, simple_heuristic)
print("Branch and Bound with Heuristic path:", result_path)
