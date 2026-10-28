def floyd_warshall(graph, v):
    dist = [[graph[i][j] for j in range(v)] for i in range(v)]
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

INF = float('inf')
graph = [[0, 5, INF, 10], [INF, 0, 3, INF], [INF, INF, 0, 1], [INF, INF, INF, 0]]
print(floyd_warshall(graph, 4))