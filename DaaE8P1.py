class Node:
    def __init__(self, key):
        self.val = key
        self.left = self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

root = None
for key in [50, 30, 70, 20, 40]:
    root = insert(root, key)