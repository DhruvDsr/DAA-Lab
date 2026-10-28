import heapq

def merge_k_arrays(arrays):
    min_heap = []
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))
            
    res = []
    while min_heap:
        val, arr_idx, ele_idx = heapq.heappop(min_heap)
        res.append(val)
        if ele_idx + 1 < len(arrays[arr_idx]):
            next_tuple = (arrays[arr_idx][ele_idx + 1], arr_idx, ele_idx + 1)
            heapq.heappush(min_heap, next_tuple)
            
    return res

print(merge_k_arrays([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))