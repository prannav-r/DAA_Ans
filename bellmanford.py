#Time Complexity: O(V × E)
import math

def bellman_ford(graph: list[list[int]], source: int) -> tuple[list[int], bool]:
    """
    Finds the shortest path distances from a single source vertex to all
    other vertices in a weighted directed graph using the Bellman-Ford algorithm.

    Args:
        graph: Adjacency matrix where graph[i][j] is the weight from i to j.
               Use math.inf to represent no edge.
        source: Index of the source vertex.

    Returns:
        A tuple:
        - List of shortest distances from the source to each vertex.
        - Boolean indicating if a negative weight cycle exists (True if yes).
    """
    V = len(graph)
    dist = [math.inf] * V
    dist[source] = 0

    # Relax all edges (V - 1) times
    for _ in range(V - 1):
        for u in range(V):
            for v in range(V):
                if graph[u][v] != math.inf:
                    if dist[u] + graph[u][v] < dist[v]:
                        dist[v] = dist[u] + graph[u][v]

    # Check for negative-weight cycles
    has_negative_cycle = False
    for u in range(V):
        for v in range(V):
            if graph[u][v] != math.inf:
                if dist[u] + graph[u][v] < dist[v]:
                    has_negative_cycle = True

    return dist, has_negative_cycle

graph = [
    [0,     1,     4,     math.inf],
    [math.inf, 0,     4,     2],
    [math.inf, math.inf, 0,     3],
    [math.inf, math.inf, math.inf, 0]
]

distances, has_neg_cycle = bellman_ford(graph, source=0)

print("Distances:", distances)
print("Negative Cycle Detected:", has_neg_cycle)
