class Node:
    def __init__(self, key):
        self.val = key
        self.left = self.right = None

def lca(root, n1, n2):
    if root is None:
        return None
    if root.val > max(n1, n2):
        return lca(root.left, n1, n2)
    if root.val < min(n1, n2):
        return lca(root.right, n1, n2)
    return root.val

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)

print(lca(root, 20, 40))