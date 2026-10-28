class HashChain:
    def __init__(self, size):
        self.table = [[] for _ in range(size)]
        
    def insert(self, key):
        self.table[key % len(self.table)].append(key)
        
    def search(self, key):
        return key in self.table[key % len(self.table)]

class HashProbe:
    def __init__(self, size):
        self.table = [None] * size
        
    def insert(self, key):
        idx = key % len(self.table)
        while self.table[idx] is not None:
            idx = (idx + 1) % len(self.table)
        self.table[idx] = key
        
    def search(self, key):
        idx = start = key % len(self.table)
        while self.table[idx] is not None:
            if self.table[idx] == key:
                return True
            idx = (idx + 1) % len(self.table)
            if idx == start:
                break
        return False

hc = HashChain(10)
for k in [15, 25, 35]: 
    hc.insert(k)
print(hc.search(25))