import heapq
import math

def minimize_sum(arr, k):
    pq = [-x for x in arr]
    heapq.heapify(pq)
    for _ in range(k):
        if not pq: break
        val = -heapq.heappop(pq)
        heapq.heappush(pq, -math.ceil(val / 2))
    return -sum(pq)

print(minimize_sum([10, 20, 7], 4))