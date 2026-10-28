def subarrays_with_k_distinct(arr, k):
    def at_most_k(k):
        count = left = right = 0
        freq = {}
        while right < len(arr):
            freq[arr[right]] = freq.get(arr[right], 0) + 1
            while len(freq) > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1
            count += right - left + 1
            right += 1
        return count
    return at_most_k(k) - at_most_k(k - 1)

print(subarrays_with_k_distinct([1, 2, 1, 2, 3], 2))