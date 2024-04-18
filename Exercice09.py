class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def display(self):
        for vertex in self.graph:
            print(vertex, '->', ' -> '.join(map(str, self.graph[vertex])))

# Creating an instance of the Graph class
graph = Graph()

# Adding edges to the graph
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)

# Displaying the graph
print("Graph Representation:")
graph.display()
