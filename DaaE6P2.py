def bucket_sort(arr):
    if not arr: return []
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for num in arr:
        buckets[int(n * num)].append(num)
    for bucket in buckets:
        bucket.sort()
    idx = 0
    for bucket in buckets:
        for num in bucket:
            arr[idx] = num
            idx += 1
    return arr

print(bucket_sort([0.42, 0.32, 0.23, 0.52]))