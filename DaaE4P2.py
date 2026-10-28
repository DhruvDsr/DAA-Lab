def quick_select(arr, k):
    def partition(l, r):
        pivot = arr[r]
        i = l
        for j in range(l, r):
            if arr[j] >= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[r] = arr[r], arr[i]
        return i

    left, right = 0, len(arr) - 1
    while left <= right:
        pi = partition(left, right)
        if pi == k - 1:
            return arr[pi]
        elif pi < k - 1:
            left = pi + 1
        else:
            right = pi - 1

print(quick_select([3, 2, 1, 5, 6, 4], 2))