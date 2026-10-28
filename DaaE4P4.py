def first_missing_positive(arr):
    n = len(arr)
    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
            nxt = arr[i] - 1
            arr[i], arr[nxt] = arr[nxt], arr[i]
    
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1
    return n + 1

print(first_missing_positive([3, 4, -1, 1]))

import time
import random

def run_benchmark():
    sizes = [1000, 5000, 10000, 20000, 50000]
    for n in sizes:
        arr = [random.randint(-n, n) for _ in range(n)]
        start = time.perf_counter_ns()
        first_missing_positive(arr)
        end = time.perf_counter_ns()
        print(f"{n}\t{end - start}")

run_benchmark()