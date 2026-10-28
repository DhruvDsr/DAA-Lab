import heapq
from collections import Counter

def rearrange_string(s):
    count = Counter(s)
    max_heap = [[-freq, char] for char, freq in count.items()]
    heapq.heapify(max_heap)
    prev = None
    res = []
    
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        res.append(char)
        if prev and prev[0] < 0:
            heapq.heappush(max_heap, prev)
        freq += 1
        prev = [freq, char]
        
    return "".join(res) if len(res) == len(s) else ""

print(rearrange_string("aaabbc"))