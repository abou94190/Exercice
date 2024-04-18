def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented by a dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F','G'],
    'D': [],
    'E': ['I','G'],
    'F': [],
    'G': []
}

# Starting node for DFS traversal
start_node = 'A'

print("Depth-First Traversal:")
dfs(graph, start_node)
