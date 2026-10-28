import heapq

def max_bottleneck_path(graph, start, end):
    bottleneck = {node: float('-inf') for node in graph}
    bottleneck[start] = float('inf')
    pq = [(-float('inf'), start)]
    
    while pq:
        curr_cap, u = heapq.heappop(pq)
        curr_cap = -curr_cap
        if u == end:
            return curr_cap
        if curr_cap < bottleneck[u]:
            continue
        for v, capacity in graph[u]:
            new_cap = min(curr_cap, capacity)
            if new_cap > bottleneck[v]:
                bottleneck[v] = new_cap
                heapq.heappush(pq, (-new_cap, v))
                
    return 0

graph = {0: [(1, 10), (2, 20)], 1: [(3, 30)], 2: [(3, 10)], 3: []}
print(max_bottleneck_path(graph, 0, 3))