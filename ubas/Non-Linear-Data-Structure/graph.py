"""
Graph - UBAS

Vertices: U, B, A, S
Edges: U-B, U-A, B-S, S-A

Expected traversals (starting at U):
BFS: U - B - A - S
DFS: U - B - S - A
"""
from collections import deque


class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_vertex(self, vertex):
        self.adjacency.setdefault(vertex, [])

    def add_edge(self, a, b):
        self.adjacency[a].append(b)
        self.adjacency[b].append(a)

    def build(self):
        """Build the graph from the yellow-pad diagram."""
        for vertex in ["U", "B", "A", "S"]:
            self.add_vertex(vertex)
        self.add_edge("U", "B")
        self.add_edge("U", "A")
        self.add_edge("B", "S")
        self.add_edge("S", "A")

    def bfs(self, start):
        """Breadth-first search using a queue."""
        visited = [start]
        queue = deque([start])
        while queue:
            current = queue.popleft()
            for neighbor in self.adjacency[current]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        return visited

    def dfs(self, start):
        """Depth-first search using recursion."""
        visited = []
        self._dfs(start, visited)
        return visited

    def _dfs(self, vertex, visited):
        visited.append(vertex)
        for neighbor in self.adjacency[vertex]:
            if neighbor not in visited:
                self._dfs(neighbor, visited)


if __name__ == "__main__":
    graph = Graph()
    graph.build()
    print("BFS:", " - ".join(graph.bfs("U")))
    print("DFS:", " - ".join(graph.dfs("U")))
