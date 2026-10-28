def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k - 1]
        
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sub)[len(sub) // 2] for sub in sublists]
    pivot = median_of_medians(medians, len(medians) // 2 + 1)
    
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if k <= len(left):
        return median_of_medians(left, k)
    elif k <= len(left) + len(mid):
        return pivot
    else:
        return median_of_medians(right, k - len(left) - len(mid))

print(median_of_medians([7, 10, 4, 3, 20, 15], 3))