def all_pairs_shortest_path(graph):
    # Number of vertices in the graph
    n = len(graph)

    # Initialize the distance matrix with the given graph
    dist = [row[:] for row in graph]

    # Iterate through all vertices as intermediate nodes
    for k in range(n):
        # Pick all vertices as source one by one
        for i in range(n):
            # Pick all vertices as destination for the above source
            for j in range(n):
                # If vertex k is on the shortest path from i to j,
                # then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example usage:
graph = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]

result = all_pairs_shortest_path(graph)
print("All-Pairs Shortest Path Matrix:")
for row in result:
    print(row)
