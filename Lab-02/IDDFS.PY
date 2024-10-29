def dls(node, goal, graph, depth, visited):
    if depth == 0 and node == goal:
        return True  
    if depth > 0:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dls(neighbor, goal, graph, depth - 1, visited):
                    return True
    return False

def iddfs(graph, start_node, goal):
    """IDDFS: Iterative Deepening DFS"""
    depth = 0
    while True:
        visited = set()  
        if dls(start_node, goal, graph, depth, visited):
            print(f"Goal '{goal}' found at depth {depth}")
            return
        depth += 1
        print(f"Depth {depth} completed, goal not found.")
        if depth > len(graph): 
            print("Goal not found within depth limits.")
            return

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F', 'A'],  
    'F': []
}

iddfs(graph, 'A', 'F')
