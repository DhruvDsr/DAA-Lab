from collections import Counter

def min_window(s, t):
    need = Counter(t)
    missing = len(t)
    i = I = J = 0
    
    for j, char in enumerate(s, 1):
        missing -= need[char] > 0
        need[char] -= 1
        if not missing:
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            if not J or j - i <= J - I:
                I, J = i, j
                
    return s[I:J]

print(min_window("ADOBECODEBANC", "ABC"))