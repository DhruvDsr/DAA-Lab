import heapq

def prims_mst(graph, start):
    mst_cost = 0
    visited = set()
    min_heap = [(0, start)]
    
    while min_heap and len(visited) < len(graph):
        cost, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        mst_cost += cost
        for v, weight in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (weight, v))
    return mst_cost

graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}
print(prims_mst(graph, 0))