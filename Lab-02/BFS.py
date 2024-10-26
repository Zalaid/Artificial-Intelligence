from collections import deque

def bfs(graph, start_node):
    visited = set()  
    queue = deque([start_node])  

    while queue:
        node = queue.popleft()  

        if node not in visited:
            print(node, end=" ")  
            visited.add(node) 

            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F', 'A'],  
    'F': []
}

bfs(graph, 'A')
