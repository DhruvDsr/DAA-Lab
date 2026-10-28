class Node:
    def __init__(self, key):
        self.val = key
        self.left = self.right = None

def largest_bst(root):
    def dfs(node):
        if not node:
            return True, 0, float('inf'), float('-inf')
        l_bst, l_size, l_min, l_max = dfs(node.left)
        r_bst, r_size, r_min, r_max = dfs(node.right)
        if l_bst and r_bst and l_max < node.val < r_min:
            return True, l_size + r_size + 1, min(l_min, node.val), max(r_max, node.val)
        return False, max(l_size, r_size), 0, 0
    return dfs(root)[1]

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)

print(largest_bst(root))