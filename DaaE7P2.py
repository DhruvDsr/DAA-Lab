def relative_sort(arr1, arr2):
    order = {v: i for i, v in enumerate(arr2)}
    return sorted(arr1, key=lambda x: (order.get(x, len(arr2)), x))

print(relative_sort([2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8], [2, 1, 8, 3]))